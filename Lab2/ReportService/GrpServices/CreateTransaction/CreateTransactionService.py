from concurrent import futures
import logging
import json

import grpc
import CreateTransaction_pb2
import CreateTransaction_pb2_grpc

path_to_users_info = "ReportService/UsersInfo.json"
methods = {"add": lambda x, y: x + y,
           "buy": lambda x, y: x - y}

class CreareTransaction(CreateTransaction_pb2_grpc.CreateTransactionServicer):
    def Create(self, request, context):
        try:
            file = open(path_to_users_info)
            users_info = json.load(file)
            file.close()

            user_balance = users_info[str(request.id_user)]["balance"]
            result = methods[request.method](int(user_balance), request.balance)

            if result >= 0:
                users_info[str(request.id_user)]["balance"] = result
                status = True
                report = "Транзакция произведена успешно"
            else:
                status = False
                report = "На балансе недостаточно средств"

            file = open(path_to_users_info, 'w')
            json.dump(users_info, file, indent=4)
            file.close()
            
            return CreateTransaction_pb2.ResponseAboutTransaction(status=status, report=report)
        except:
            return CreateTransaction_pb2.ResponseAboutTransaction(status=False,
                                                                  report=report)


def serve():
    port = "50004"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    CreateTransaction_pb2_grpc.add_CreateTransactionServicer_to_server(CreareTransaction(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
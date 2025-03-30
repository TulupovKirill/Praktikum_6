from concurrent import futures
import logging
import json

import grpc
import RequestAboutNewUser_pb2
import RequestAboutNewUser_pb2_grpc

path_to_users_info = "../../UsersInfo.json"

class CreareNewUser(RequestAboutNewUser_pb2_grpc.SaveAuthUserServicer):
    def Create(self, request, context):
        try:
            file = open(path_to_users_info)
            users_info = json.load(file)
            file.close()

            users_info[request.id] = {"name": request.name, "balance": 0}

            file = open(path_to_users_info, 'w')
            json.dump(users_info, file, indent=4)
            file.close()
            
            return RequestAboutNewUser_pb2.ReportResponce(status=True)
        except:
            return RequestAboutNewUser_pb2.ReportResponce(status=False)


def serve():
    port = "50003"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    RequestAboutNewUser_pb2_grpc.add_CreateNewUserServicer_to_server(CreareNewUser(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
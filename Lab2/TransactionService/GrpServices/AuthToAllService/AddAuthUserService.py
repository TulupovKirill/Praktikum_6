from concurrent import futures
import logging

import grpc
import AuthToAllService_pb2
import AuthToAllService_pb2_grpc

path_to_auth_user = "Lab2/TransactionService/auth_user.txt"

class Save(AuthToAllService_pb2_grpc.SaveAuthUserServicer):
    def Save(self, request, context):
        try:
            file = open(path_to_auth_user, "a+")
            file.write(f"{request.id} ")
            file.close()
            return AuthToAllService_pb2.Response(status=True)
        except:
            return AuthToAllService_pb2.Response(status=False)


def serve():
    port = "50002"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    AuthToAllService_pb2_grpc.add_SaveAuthUserServicer_to_server(Save(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
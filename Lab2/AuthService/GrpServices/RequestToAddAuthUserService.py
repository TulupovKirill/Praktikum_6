# from __future__ import print_function

import grpc
from Lab2.AuthService.GrpServices import AuthToAllService_pb2
from Lab2.AuthService.GrpServices import AuthToAllService_pb2_grpc


def RequestToAuthUserInAnotherService(id_user, port):
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = AuthToAllService_pb2_grpc.SaveAuthUserStub(channel)
        response = stub.Save(AuthToAllService_pb2.AuthRequest(id=id_user))
    return response

# if __name__ == "__main__":
#     RequestUserToService(5, 50001)
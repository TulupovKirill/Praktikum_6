import grpc
from Lab2.AuthService.GrpServices.RequestAboutNewUser import RequestAboutNewUser_pb2
from Lab2.AuthService.GrpServices.RequestAboutNewUser import RequestAboutNewUser_pb2_grpc


def RequestToAuthUserInAnotherService(id_user, name, port):
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = RequestAboutNewUser_pb2_grpc.CreateNewUserStub(channel)
        response = stub.Save(RequestAboutNewUser_pb2.InfoAboutNewUser(id_user, name))
    return response

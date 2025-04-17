import grpc
from Lab2.AuthService.GrpServices.RequestAboutNewUser import RequestAboutNewUser_pb2
from Lab2.AuthService.GrpServices.RequestAboutNewUser import RequestAboutNewUser_pb2_grpc


def RequestToAddNewUser(id_user, name, port):
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = RequestAboutNewUser_pb2_grpc.CreateNewUserStub(channel)
        response = stub.Create(RequestAboutNewUser_pb2.InfoAboutNewUser(id=id_user, name=name))
    return response

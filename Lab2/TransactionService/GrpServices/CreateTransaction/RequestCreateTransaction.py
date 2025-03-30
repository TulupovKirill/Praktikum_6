import grpc
from Lab2.TransactionService.GrpServices.CreateTransaction import CreateTransaction_pb2
from Lab2.TransactionService.GrpServices.CreateTransaction import CreateTransaction_pb2_grpc


def RequestCreateTransaction(method:str, id_user:int, balance:int, port:int):
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = CreateTransaction_pb2_grpc.CreateTransactionStub(channel)
        response = stub.Create(CreateTransaction_pb2.RequestForTransaction(
            method=method,
            id_user=id_user,
            balance=balance
        ))
    return response

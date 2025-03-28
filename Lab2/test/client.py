from __future__ import print_function

import logging

import grpc
import Lab2_pb2
import Lab2_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = Lab2_pb2_grpc.SayHelloStub(channel)
        response = stub.Recommed(Lab2_pb2.HelloRequest(message="you"))
    print("Клиент готов!")


if __name__ == "__main__":
    logging.basicConfig()
    run()
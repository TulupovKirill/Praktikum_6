from concurrent import futures
import logging

import grpc
import Lab2_pb2
import Lab2_pb2_grpc


class SayHello(Lab2_pb2_grpc.SayHelloServicer):
    def Recommed(self, request, context):
        return Lab2_pb2.HelloResponse(message="Hello, %s!" % request.message)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Lab2_pb2_grpc.add_SayHelloServicer_to_server(SayHello(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
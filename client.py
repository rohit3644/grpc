import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)
while True:
    try:
        # create a valid request message
        num1 = calculator_pb2.Request(num1=int(input("Enter number1: ")))
        num2 = calculator_pb2.Request(num2=int(input("Enter number2: ")))
    # make the call
        response = stub.Sum(num1, num2)

        print(response.value)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        channel.unsubscribe(close)
        exit()
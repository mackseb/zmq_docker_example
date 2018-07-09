import zmq
import os

context = zmq.Context()
address = os.environ['ADDRESS']
print(address)
#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect(address)

#  Do 10 requests, waiting each time for a response
for request in range(100):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
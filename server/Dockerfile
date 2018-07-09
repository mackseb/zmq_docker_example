FROM python:3.6

RUN pip install zmq

COPY . .

EXPOSE 80

EXPOSE 5555

CMD [ "python", "server.py"]
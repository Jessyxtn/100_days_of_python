from socket import *
from datetime import datetime
import sys
import random

if len(sys.argv) != 3:
    print("Required arguments: host port")

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
random_number = random.randint(10000, 20000)

clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1, 21):    
    time_stamp1 = datetime.now()    
    message = "PING " + str(i + random_number) + time_stamp1.strftime("%m/%d/%Y, %H:%M:%S")

    clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))
    clientSocket.settimeout(0.6)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_stamp2 = datetime.now()
        rtt = round((time_stamp2 - time_stamp1).total_seconds() * 1000)
        print(modifiedMessage.decode('utf-8') + " rtt: " + str(rtt))
    except timeout:
        print("didn't work: timeout")

clientSocket.close()

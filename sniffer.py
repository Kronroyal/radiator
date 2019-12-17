import pyshark          #import pyshark
class bcolors:
    BLACK='\u001b[30m'
    RED = '\u001b[31m'
    GREEN='\u001b[92m'
    BLUE='\u001b[94m'
    YELLOW='\u001b[93m'
    RESET='\u001b[0m'
    
def sniffer():
    counter=1
    print(f"{bcolors.RED}Please enter the required information below.\n{bcolors.RESET}")     #ask for needed information
    toscan=str(input("interface:"))     #get interface to sniff
    amount=int(input("amount of packets to capture:"))      #get amount of packets to capture
    askfile=str(input("Do you want to save the output to a file? [yes | no] :"))
    if(askfile=="yes"):     #if wish to save to file is yes
        capture=pyshark.LiveCapture(interface=toscan) #initialize capture
        capture.sniff(packet_count=amount)   #starting sniffing
        for pkt in capture:
            filename=str(input("How should the .txt file be named [example: capture.txt]")) 
            out_file=open(filename,"w")
            out_string=""       #initialize string for input in file 
            out_string+="Packet["+str(counter)+"]\n"    #Add to string
            out_string+=str(pkt)+"\n"
            out_file.write(out_string)  #write string in file
            counter=counter+1   #count up for packet count
        capture.close()
    
    elif(askfile=="no"):
        capture=pyshark.LiveCapture(interface='wlp3s0') #initialize capture
        capture.sniff(packet_count=amount)   #starting sniffing
        for pkt in capture: # for every sniffed packet in capture
            print(pkt)  #print out packet
            print("####################################")
    else:
        print("This is no available option!")
        print("restarting sniffer...")
        sniffer()
def main():     #defining main function of sniffer
    print("Executing Sniffer...\n")
    sniffer()     #execute sniffer


if __name__=="__main__":      #execute main() 
    main()

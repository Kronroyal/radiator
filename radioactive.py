import sniffer
import logo
import dos
# --------MAIN OF ALL SCRIPTS-----------------
Host="127.0.0.1"
Port=80

def main():
    print("SCRIPT BY KRONROYAL")
    logo.print_logo()
    option=int(input(":"))

def exec_script(inp):
    if(inp==0):
        sniffer.main()
    
    elif(inp==1):
        dos.main()
    
    else:
        pass

if __name__=="__main__":
    logo.print_logo2()       # Print Script Logo
    opt_counter=0
    menu=["Sniffer","DOS","coming soon..."]
    print(f"{logo.bcolors.RED}MENU{logo.bcolors.RESET}\n")
    for element in menu:
        print("[",opt_counter,"]",element)
        opt_counter=opt_counter+1
    chosen=int(input("Choose one of the previously mentioned Options by typing its number!\n"))
    exec_script(chosen)
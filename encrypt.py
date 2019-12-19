from cryptography.fernet import Fernet
import os
def exec_option(chosen):
    if(chosen==0):
        generate_key()
        print("Key generated.")
    if(chosen==1):
        encrypt_string()
    if(chosen==2):
        encrypt_text()
    if(chosen==3):
        decrypt_string()
    if(chosen==4):
        decrypt_text()
def get_filename(option):
    if(option=="encrypt"):
        filename=str(input("Which File do you want to encrpyt [*.txt] ?: "))
    elif(option=="decrypt"):
        filename=str(input("Which File do you want to decrpyt [*.txt] ?: "))
    else:
        print("Could not get filename.")
    
    return filename

def loop(options=[]):
    counter=0
    print("Do you want to:")
    for element in options:
        print("[",counter,"]",element)
        counter=counter+1
    chosen=int(input("Choose a option!:"))
    exec_option(chosen)

def generate_key():
    keyfile=open("key.txt","wb+")   #open file key.txt and create it if doesnt exist already
    key=Fernet.generate_key()   #generate the key
    keyfile.write(key)      #write key to file

def get_key():
    key=open("key.txt","rb").read()
    return key

def encrypt_text():
    filename=get_filename("encrypt")
    key=get_key()
    f=Fernet(key)
    with open(filename, "rb") as file:
        file_data=file.read()
    encrypted_data=f.encrypt(file_data)
    with open(filename,"wb") as file:
        file.write(encrypted_data)
    print("File encrypted.")

def decrypt_text():
    filename=get_filename("decrypt")
    key=get_key()
    f=Fernet(key)
    with open(filename, "rb") as file:
        file_data=file.read()
    decrypted_data=f.decrypt(file_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)
    print("File decrypted.")

def encrypt_string():
    string=str(input("Please enter the string to be encrypted..."))
    key=get_key()
    f=Fernet(key)
    encrypted_string=f.encrypt(string.encode('utf-8'))
    print("String encrypted: ",encrypted_string)

def decrypt_string():
    encrypted_string=str(input("Please enter string to be decrypted..."))
    key=get_key()
    f=Fernet(key)
    decrypted_string=f.decrypt(encrypted_string.encode('utf-8'))
    print("String decrypted: ",decrypted_string)
def main():
    print("Starting Encryptor...\n")
    options=["Generate Key","Encrypt string","Encrypt file","Decrypt string","Decrypt file"]
    print("You need a key for encrypting and decrypting. If you didnt generate key first u cant use the other functions")
    go_on=""
    while(go_on==""):
        loop(options)
        go_on=str(input("Press enter to get back to the Encrypt-Menu:"))
    print("End")
if __name__=="__main__":
    main()
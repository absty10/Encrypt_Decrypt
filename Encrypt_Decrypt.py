from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key","wb") as keyfile:
        keyfile.write(key)

def load_key():
    return open("Secret.key","rb").read()

def encrypt_data(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename,"wb") as file:
        file.write(encrypted_data) 

def decrypt_data(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except Exception as e:
            print("Invalid Key")
    with open(filename,"wb") as file:
        file.write(decrypted_data)

choice = input("Enter 'e' to Encrypt and 'd' to Decrypt the file: ").lower()
if choice == 'e':
    filename = input("Enter the filename with the extension: ")
    if os.path.exists(filename):
        generate_key()
        key=load_key()
        encrypt_data(filename, key)
        print("File encrypted successfully")
    else : 
        print(f"Filename {filename} not found.")

elif choice == 'd':
    filename = input("Enter the filename with the extension: ")
    if os.path.exists(filename):
        key=load_key()
        decrypt_data(filename, key)
        print("File dencrypted successfully")
    else : 
        print(f"Filename {filename} not found.")

else: 
    print("Please select from above choices. ")

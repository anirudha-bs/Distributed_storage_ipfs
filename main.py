from files import write_key, load_key, encrypt, decrypt
import os
from ipfs import add,pin,get_file

def switch(option):
    return switcher.get(option, default)()

# Encrypts file and adds to ipfs
def encrypt_ipfs_add():
    file=input("Enter the file name to be added - ")
    # Look for saved key, if not found then create one
    try:
        key = load_key()
    except:
        write_key()
    key = load_key()
    #encrypt file
    encrypt(file,key)
    #returns file details added to ipfs
    res = add(file)
    print("Encrpted file was added to ipfs")
    print(res)


def ipfs_add():
    file=input("Enter the file name to be added - ")
    res = add(file)
    print("The file was added to ipfs")
    print(res)

def decrypt_ipfs():
    #hash of the file added to ipfs earlier
    hash = input("Enter the hash of the file you want to retrive - ")
    res = get_file(hash)
    # Look for saved key, if not found then create one
    try:
        key = load_key()
    except:
        print("No key found")
        exit(0)
    decrypt(res,key)
    #decrypted file will be saved as res.txt
    print("THe file " + hash + " was successfully decrpted")

#function to get a file added to ipfs
def ipfs_get():
    hash = input("Enter the hash of the file you want to retrive - ")
    get_file(hash)
    print("The file has been stored at res.txt ")

def default():
    return "Please select a valid option"

switcher = {
        1: encrypt_ipfs_add,
        2: ipfs_add,
        3: decrypt_ipfs,
        4: ipfs_get,
        }

if __name__ == "__main__":

    while(1):
        print("\nDistributed storage\n -------Menu------ \n 1. Encrypt file and add to IPFS \n 2. Add file to ipfs without encryption \n 3. Decrypt a file from IPFS \n 4. Get file from IPFS \n 5. Exit \n")
        option = int(input())
        switch(option)
        if option==5:
            break
        
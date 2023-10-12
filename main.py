from cryptography.fernet import Fernet
import sys
import os

def enc(file, mode) :
    if len(sys.argv) < 5 and mode :
        key = Fernet.generate_key()
    elif mode :
        key = sys.argv[4]
    else :
        return "No se ha proporcionado una llave"
    with open(file, "rb") as x :
        cont = x.read()
    with open(file+".enc", "wb") as z :
        if mode :
            z.write(Fernet(key).encrypt(cont))
        else :
            z.write(Fernet(key).decrypt(cont))
    with open(file+".key", "wb") as y :
        y.write(key)
    return file+".enc > "+file+".key > "+str(key)

def don(dir) :
    for x in os.listdir(dir):
        if os.path.isdir(x) :
            print("[DIR]", x)
            don(dir+"/"+x)
        else :
            print("[FILE]", x)

if sys.argv[1] == "enc":
    print(enc(sys.argv[2], sys.argv[3]))

elif sys.argv[1] == "don" :
    don(sys.argv[2])

logo = """
   __ _ _
  / _(_) |
 | |_ _| | ___ ______ ___ ___  _ __ ___
 |  _| | |/ _ \______/ __/ _ \| '__/ _  -> Maneja archivos fácilmente
 | | | | |  __/     | (_| (_) | | |  __/
 |_| |_|_|\___|      \___\___/|_|  \___|
                                        
"""

name = "file-core NAT"

msg = """
Uso de los paquetes de file-core

1. - enc -> (archivo, modo)
2. - don -> (directorio)

Enc -> Encriptación y desencriptación de archivos con y sin llave
Don -> Generador de esquemas de directorio y sus archivos

"""

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

if __name__ == "__main__":
	if sys.argv[1] == "enc":
    		print(enc(sys.argv[2], sys.argv[3]))

	elif sys.argv[1] == "don" :
    		don(sys.argv[2])

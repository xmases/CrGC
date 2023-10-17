#!/usr/bin/python3

import sys, os

exec("import "+sys.argv[1]+" as pck")
print(pck.logo, "Nombre del paquete: "+pck.name)


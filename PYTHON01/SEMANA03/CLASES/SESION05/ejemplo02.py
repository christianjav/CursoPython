import sys
import hashlib

def main():
    t=len(sys.argv[1])
    if (t>1):
        print("cantidad de argumentos invalida")
        sys.exit()
    else:
        cadena=sys.argv[1:]
        h=hashlib.sha1()
        h.update(cadena.encode("utf-8"))
        print(h.hexdigest())

if (__name__=='__main__'):
    main()

#################################
#para llamar en linea de comandos
#python ejemplo02.py admin
#################################



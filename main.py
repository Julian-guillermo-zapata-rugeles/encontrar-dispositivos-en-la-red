import os
import threading
import time


def manual(x,y):
    host_found=[]
    os.system("clear")
    """ Funcion Manual para hallar buscar Uno A Uno (puede tardar unos minutos )"""
    for value in range(x,y):
        os.system("clear")
        print("**************************************************")
        print("analizando  : 192.168.1."+str(value))
        print("")
        print("Encontrados : ")
        for x in host_found:
            print("\t     ",x)
        print("**************************************************")
        currently_ip="ping -c 1 192.168.1."+str(value)+" -A"
        response=os.popen(currently_ip).read()
        if response.find("1 received")!= -1:
            print("host found 192.168.1."+str(value))
            add="192.168.1."+str(value)
            host_found.append(add)

def automatic(comando,mode):
    if mode==True:
        way=" -A"
    else:
        way=""
    comando_full="ping -c 1 "+str(comando)+way
    #print(comando_full)
    response=os.popen(comando_full).read()
    if response.find("1 received")!= -1:
        print("found! ",comando)

def mode_automatic(value):
    for i in range(1,252):
        ip_probe="192.168.1."+str(i)
        #print(ip_probe)
        run=threading.Thread(target=automatic,args=(ip_probe,value,))
        run.start()

if __name__ == '__main__':
    os.system("clear")
    print("**********************************************************")
    print("Script para buscar dispositivos conectados en nuestra red\n")
    print("1) para busqueda manual (bastante lento)")
    print("2) busqueda automatica por hilos (super rapido)")
    print("3) busqueda automatica por hilos (rapida)")
    print("\n")
    election=str(input(">>> "))
    if election=="1":
        print("rango inicial (inicia en )")
        x=int(input("x >>"))
        print("rango final (finaliza en)")
        y=int(input("y >>"))
        manual(x,y)
    if election=="2":
        mode_automatic(True)
    if election=="3":
        mode_automatic(False)
    if election not in ["1","2","3"]:
        print("Invalido. ejecute nuevamente")
        exit()

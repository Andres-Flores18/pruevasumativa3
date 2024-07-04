import csv
import os
import time
cls="clear"

def registro():
    nombre=input(print("ingrese un nombre y apellido"))
    comuna=input(print("ingresa nombre de la comuna"))
    return(nombre,comuna)

def guardardatos(nombre,comuna,archivo_csv='datos_csv'):
    with open(archivo_csv, 'a', newline='') as archivo:
        campo=['nombre','comuna']
        escritor_csv= csv.DictWriter(archivo,fieldnames=campo)
        if archivo.tell()==0:
            escritor_csv.writeheader()
            escritor_csv.writerow({
                'nombre':nombre,
                'comuna':comuna
                })
 
def mostar1(archivo_csv='datos_csv'):
    with open(archivo_csv, 'r',newline='') as archivo:
        lector_csv=csv.reader(archivo)
        next(lector_csv)
        for fila in lector_csv:
            print(f"nombre del cliente {fila[0]}")
    

      







def menu():
    while True:
        print("Bienvenido al menu")
        print("1.Registrar pedido")
        print("2.Listar todos los pedidos")
        print("3.Imprimir hoja de ruta")
        print("4.salir")
        opc=int(input("ingresa una opcion del 1 al 4:"))
        if opc==1: 
            time.sleep(2) 
            os.system("cls")
            print("registre el pedido")
            nombre,comuna= registro()
            guardardatos(nombre, comuna)
            time.sleep(2) 
            os.system("cls")

        elif opc==2:
            time.sleep(2) 
            os.system("cls")
            print("mostrar todos los pedidos")
            mostar1()
            time.sleep(2) 
            os.system("cls")

        elif opc==3:
            print("imprimir hoja de ruta")
        
        elif opc==4:
            print("cerrar programa")
            break

        
           
        
menu()


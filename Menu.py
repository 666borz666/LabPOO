################################################################################
#Elaborado por: Daniel Campos y Alejandro Madrigal
#Creacion: 20-10-2023
#Ultima modificacion: 20-10-2023
#Version: 3.12.0
################################################################################
#Importacion de librerias
from LabPOO import *
#Menu

#Programa principal
def menu4():
    try:
        print("1. Mostrar todas las reservas.")
        print("2. Mostrar las funciones de un mes.")
        print("3. Mostrar las reservas de una cédula.")
        print("4. Voler al menú principal.")
        opcion = int(input("Ingrese la opción que desea: "))
        if opcion >0 and opcion < 5:
            if opcion == 1:
                return
            if opcion == 2:
                return
            if opcion == 3:
                return
            if opcion == 4:
                return menu()
    except ValueError:
        print("Debe ingresar un número entero.")
        return menu4()
def menu():
    try:
        print("1. Reserevar una butaca.")
        print("2. Modificar función.")
        print("3. Eliminar reservación.")
        print("4. Mostrar.")
        print("5. Salir.")
        opcion = int(input("Ingrese la opción que desea: "))
        if opcion >0 and opcion < 6:
            if opcion == 1:
                return
            if opcion == 2:
                return
            if opcion == 3:
                return
            if opcion == 4:
                return menu4()
            if opcion == 5:
                return
    except ValueError:
        print("Debe ingresar un número entero.")
        return menu()
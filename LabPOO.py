################################################################################
#Elaborado por: Daniel Campos y Alejandro Madrigal
#Creacion: 20-10-2023
#Ultima modificacion: 20-10-2023
#Version: 3.12.0
################################################################################
#Importacion de librerias
import pickle
import os
import random
#Definicion de clases
class Reserva:
    idReserva = 0
    sala = 0
    funcion = ""
    asiento = []
    cedula = 0
    reservado = False
    def __init__(self):
        self.idReserva = 0
        self.sala = 0
        self.funcion = ""
        self.asiento = []
        self.cedula = 0
        self.reservado = False
    def idReserva (self, ID):
        self.idReserva = ID
        return
    def sala (self, sala):
        self.sala = sala
        return
    def funcion (self, funcion):
        self.funcion = funcion
        return
    def asiento (self, asiento):
        self.asiento = asiento
        return
    def cedula (self, cedula):
        self.cedula = cedula
        return
    def reservado (self, reservado):
        self.reservado = reservado
        return
#definicion de funciones
reservaciones = Reserva()

def graba(archivo, objeto):
    try:
        f = open(archivo, "wb")
        pickle.dump(objeto, f)
        f.close()
    except:
        print("Error al grabar el archivo")
    return

def lee(archivo):
    try:
        f = open(archivo, "rb")
        objeto = pickle.load(f)
        f.close()
    except:
        objeto = None
    return objeto

def asignarAsiento():
    """
    """
    asiento = []
    print("Eliga el asiento que desea reservar: ")
    letraAsiento = input("Ingrese la letra del asiento: ")
    numeroAsiento = int(input("Ingrese el número del asiento: "))
    asiento.append(letraAsiento)
    asiento.append(numeroAsiento)
    return asiento

def reservarButaca():
    """
    """
    return  

def modificarFuncion():
    """
    """
    return

def eliminarReservacion():
    """
    """
    return

def mostrarTodasFunc():
    """
    """
    return

def mostrarFuncMes():
    """
    """
    return

def mostrarFuncCedula():
    """
    """
    return
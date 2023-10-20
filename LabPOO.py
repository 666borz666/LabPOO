################################################################################
#Elaborado por: Daniel Campos y Alejandro Madrigal
#Creacion: 20-10-2023
#Ultima modificacion: 20-10-2023
#Version: 3.12.0
################################################################################
#Importacion de librerias
import pickle
import os
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

def reservarButaca():
    """
    """
    return
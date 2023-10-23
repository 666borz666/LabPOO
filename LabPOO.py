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

def reservarButaca():
    reserva = Reserva()
    reserva.idReserva = int(input("Ingrese el ID de la reserva: "))
    reserva.sala = int(input("Ingrese el número de sala: "))
    reserva.funcion = input("Ingrese la función: ")
    asientos = input("Ingrese los asientos separados por comas: ")
    reserva.asiento = [int(a) for a in asientos.split(",")]
    reserva.cedula = int(input("Ingrese el número de cédula: "))
    reserva.reservado = True
    graba("reservas.dat", reserva)
    print("Reserva exitosa.")

def modificarFuncion():
    id_reserva = int(input("Ingrese el ID de la reserva que desea modificar: "))
    reserva = lee("reservas.dat")
    if reserva:
        if reserva.idReserva == id_reserva:
            nueva_funcion = input("Ingrese la nueva función: ")
            reserva.funcion = nueva_funcion
            graba("reservas.dat", reserva)
            print("Función modificada con éxito.")
        else:
            print("ID de reserva no encontrado.")
    else:
        print("No hay reservas disponibles.")

def eliminarReservacion():
    id_reserva = int(input("Ingrese el ID de la reserva que desea eliminar: "))
    reserva = lee("reservas.dat")
    if reserva:
        if reserva.idReserva == id_reserva:
            reserva.idReserva = 0
            reserva.sala = 0
            reserva.funcion = ""
            reserva.asiento = []
            reserva.cedula = 0
            reserva.reservado = False
            graba("reservas.dat", reserva)
            print("Reserva eliminada con éxito.")
        else:
            print("ID de reserva no encontrado.")
    else:
        print("No hay reservas disponibles.")

def mostrarTodasReservas():
    reserva = lee("reservas.dat")
    if reserva:
        print("ID de Reserva:", reserva.idReserva)
        print("Número de Sala:", reserva.sala)
        print("Función:", reserva.funcion)
        print("Asientos:", reserva.asiento)
        print("Cédula:", reserva.cedula)
        print("Reservado:", reserva.reservado)
    else:
        print("No hay reservas disponibles.")

def mostrarFuncMes():
    mes_deseado = input("Ingrese el número de mes a mostrar (1=Enero, 2=Febrero, etc.): ")
    reservas = lee("reservas.dat")
    if reservas:
        for reserva in reservas:
            if reserva.funcion.find(f"{mes_deseado}/") != -1:
                print("ID de Reserva:", reserva.idReserva)
                print("Número de Sala:", reserva.sala)
                print("Función:", reserva.funcion)
                print("Asientos:", reserva.asiento)
                print("Cédula:", reserva.cedula)
                print("Reservado:", reserva.reservado)
    else:
        print("No hay reservas disponibles.")
        
def mostrarFuncCedula():
    cedula = int(input("Ingrese el número de cédula a buscar: "))
    reserva = lee("reservas.dat")
    if reserva and reserva.cedula == cedula:
        print("ID de Reserva:", reserva.idReserva)
        print("Número de Sala:", reserva.sala)
        print("Función:", reserva.funcion)
        print("Asientos:", reserva.asiento)
        print("Cédula:", reserva.cedula)
        print("Reservado:", reserva.reservado)
    else:
        print("No se encontraron reservas para la cédula especificada.")
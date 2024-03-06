"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import threading 
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Ejecutar Requerimiento 9")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    jobs, multilocations, skills, employments = controller.load_data(control)
    return jobs, multilocations, skills, employments
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    Number=int(input("Introduzca la cantidad de ofertas que desea ver"))
    country_code=str(input("Introduzca el codigo del país"))
    level=str(input("Introduzca el nivel de experiencia"))
    resultado=controller.req_1(Number, country_code, level, control)
    print("El numero de ofertas mostradas es ", Number , ", el nivel requerido pedido es " , level , " y el codigo de pais es " , country_code)
    print(tabulate(resultado))
    return resultado
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("Introduzca la empresa que quieres buscar: ")
    nombre_empresa = str(input())
    print("Introduzca la fecha inicial del periodo de busqueda: ")
    anio_inicial = str(input("Año: "))
    mes_inicial = str(input("Mes: "))
    dia_inicial = str(input("Dia: "))
    fecha_inicial = anio_inicial+"-"+mes_inicial+"-"+dia_inicial
    print("Introduzca la fecha final del de busqueda: ")
    anio_final = str(input("Año: "))
    mes_final = str(input("Mes: "))
    dia_final = str(input("Dia: "))
    fecha_final = anio_final+"-"+mes_final+"-"+dia_final
    print("Buscando ofertas de trabajo... ")
    ofertas, numero_ofertas, junior, mid, senior = controller.req_3(nombre_empresa, fecha_inicial, fecha_final, control)
    if not ofertas:
        print("No se encontraron ofertas de trabajo de la empresa que buscas en el periodo de tiempo seleccionado")
    else:
        print("Se encontraron ", numero_ofertas," empleos, de los cuales",junior,"son junior,", mid, "son mid, y", senior,"son senior:")
        for item in ofertas:
            print(item["fecha"], item["empleo"], item["habilidad"], item["ciudad"], item["pais"], item["tamaño"], item["tipo_lugar"], item["ucranianos"])

    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    country_code=str(input("Introduzca el codigo de pais que quiere buscar "))
    fecha_inicial=str(input("introduzca la fecha inicial por faovr introducirla en formato %Y-%m-%d "))
    fecha_inicial+="T00:00:00.0Z"
    fecha_final=str(input("Ahora la fecha final %Y-%m-%d "))
    fecha_final+="T00:00:00.0Z"
    ofertas, size,ciudades, num_ciudades, num_empresas, mayor, menor=controller.req_4(control, country_code, fecha_inicial, fecha_final)
    print("la cantidad de ofertas encontradas fue de", size)
    print("La cantidad de empresas que publicaron fue de ", num_empresas)
    print("El numero total de ciudades que publicaron fue de ", num_ciudades)
    print("La ciudad con mas ofertas fue: ", mayor, " con un numero de ", ciudades[mayor])
    print("La ciudad con menos ofertas fue: ", menor, " con un numero de ", ciudades[menor])
    print("las ofertas son: ")
    print(tabulate(ofertas))
    
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("Dame la cantidad de ciudades que quieres consultar: ")
    top = int(input())
    print("Dame el codigo del pais que quieres consultar: ")
    encontrar_habilidad = True
    while encontrar_habilidad:
        print("1. Junior")
        print("2. Mid")
        print("3. Senior")
        print("Dame el nivel de habilidad que quieres buscar: ")
        entrada = int(input())
        if entrada == 1:
            habilidad = "Junior"
            encontrar_habilidad = False
        elif entrada == 2:
            habilidad = "Mid"
            encontrar_habilidad = False
        elif entrada == 3:
            habilidad = "Senior"
            encontrar_habilidad = False
        else:
            print("Selecciona un nevel de habilidad que este permitido")
    print("Introduzca la fecha inicial del periodo de busqueda: ")
    anio_inicial = int(input("Año: "))
    mes_inicial = int(input("Mes: "))
    dia_inicial = int(input("Dia: "))
    fecha_inicial = anio_inicial+"-"+mes_inicial+"-"+dia_inicial
    print("Introduzca la fecha final del de busqueda: ")
    anio_final = int(input("Año: "))
    mes_final = int(input("Mes: "))
    dia_final = int(input("Dia: "))
    fecha_final = anio_final+"-"+mes_final+"-"+dia_final
    req6 = controller.req_6(control, top, habilidad, fecha_inicial, fecha_final)
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass



# Se crea el controlador asociado a la vista

control = new_controller()

default_limit=1000

# main del reto

"""
Menu principal
"""

def menu_cycle():
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            t1 = lt.iterator(lt.subList(control["model"]["jobs"],1,3))
            t2 = lt.iterator(lt.subList(control["model"]["jobs"],-3,3))
            print("Primero 3 datos de jobs:\n")
            print(tabulate(t1))
            print("Ultimos 3 datos de jobs:\n")
            print(tabulate(t2))
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
            

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
if __name__ == "__main__":
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle())
    thread.start()

"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model":None
    }
    control["model"]=model.new_data_structs()
    return control

# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog= control["model"]
    jobs = loadjobs(catalog)
    skills = loadskills(catalog)
    multilocations = loadmultilocations(catalog)
    employments=loademployments(catalog)
    return jobs, skills, multilocations, employments

def loadjobs(catalog):
    jobsfile = cf.data_dir + "small-jobs.csv"
    input_file = csv.DictReader(open(jobsfile, encoding="utf-8"), delimiter=";")
    for job in input_file:
        model.addjob(catalog, job)
    return model.jobssize(catalog)

def loadskills(catalog):
    skillsfile = cf.data_dir + "small-skills.csv"
    input_file = csv.DictReader(open(skillsfile, encoding="utf-8"), delimiter=";")
    for skill in input_file:
        model.addskill(catalog, skill)
    return model.skillssize(catalog)

def loadmultilocations(catalog):
    multilocationsfile = cf.data_dir + "small-multilocations.csv"
    input_file = csv.DictReader(open(multilocationsfile, encoding="utf-8"), delimiter=";")
    for multilocations in input_file:
        model.addmultilocations(catalog, multilocations)
    return model.multilocationssize(catalog)

def loademployments(catalog):
    employmentsfile = cf.data_dir + "small-employments_types.csv"
    input_file = csv.DictReader(open(employmentsfile, encoding="utf-8"), delimiter=";")
    for employments in input_file:
        model.addemployments(catalog, employments)
    return model.employmentssize(catalog)

def loadjobs(catalog):
    jobsfile = cf.data_dir + "small-jobs.csv"
    input_file = csv.DictReader(open(jobsfile, encoding="utf-8"), delimiter=";")
    for job in input_file:
        model.addjob(catalog, job)
    return model.jobssize(catalog)
    


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(Number, country_code, level, control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    Ofertas = model.req_1(control["model"], Number, country_code, level)
    return Ofertas


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(nombre_empresa, fecha_inicial, fehca_final, control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    ofertas = model.req_3(nombre_empresa, fecha_inicial, fehca_final, control["model"])
    numero_ofertas = len(ofertas)
    junior = 0
    mid = 0
    senior = 0
    for item in ofertas:
        if item["habilidad"] == "junior":
            junior += 1
        elif item["habilidad"] == "mid":
            mid += 1
        elif item["habilidad"] == "senior":
            senior +=1
    return ofertas, numero_ofertas, junior, mid, senior


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, top, habilidad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req6 = model.req_6(control["model"], top, habilidad, fecha_inicial, fecha_final)
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

def req_9(control):
    """
    Retorna el resultado del requerimiento 9
    """
    
    # TODO: Modificar el requerimiento 9
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

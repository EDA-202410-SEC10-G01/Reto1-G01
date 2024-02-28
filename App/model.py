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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {"jobs": None,
               "multilocations": None,
               "skills": None,
               "employments": None}
    catalog["jobs"] = lt.newList("ARRAY_LIST", delimiter = ";")
    catalog["multilocations"] = lt.newList("ARRAY_LIST", delimiter = ";")
    catalog["skills"] = lt.newList("ARRAY_LIST", delimiter = ";")
    catalog["employments"] = lt.newList("ARRAY_LIST", delimiter = ";")
    
    return catalog


# Funciones para agregar informacion al modelo

def addjob(catalog, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    j = newJob(data["id"], 
                  data["published_at"], 
                  data["title"], 
                  data["company_name"], 
                  data["experience_level"], 
                  data["country_code"], 
                  data["city"])
    lt.addLast(catalog["jobs"],j)
    return catalog

def addskill(catalog, data):
    s = newSkill(data["name"], data["level"], data["id"])
    lt.addLast(catalog["skills"],s)
    return catalog

def addemployments(catalog, data):
    e = newEmployments(data["type"], data["id"], data["currency_salary"], data["salary_from"], data["salary_to"])
    lt.addLast(catalog["employments"],e)
    
    return catalog

def addmultilocations(catalog, data):
    m = newMultilocations(data["city"], data["street"], data["id"])
    lt.addLast(catalog["multilocations"],m)
    return catalog

# Funciones para creacion de datos

def newJob(id, published_at, title, company_name, experience_level, country_code, city):
    job = {"id":id,
           "published_at":published_at,
           "title":title,
           "company_name":company_name,
           "experience_level": experience_level,
           "country_code": country_code,
           "city": city
    }
    return job
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    
def newSkill(name, level, id):
    skill = {"name":name,
             "level":level,
             "id":id}
    return skill

def newEmployments(type, id, currency_salary, salary_from, salary_to):
    employments = {"type":type,
                   "id":id,
                   "currency_salary":currency_salary,
                   "salary_from":salary_from,
                   "salary_to":salary_to}
    return employments

def newMultilocations(city, street, id):
    multilocations = {"city": city,
                      "street": street,
                      "id": id}
    return multilocations

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def jobssize(catalog):
    return lt.size(catalog["jobs"])
def skillssize(catalog):
    return lt.size(catalog["skills"])
def multilocationssize(catalog):
    return lt.size(catalog["multilocations"])
def employmentssize(catalog):
    return lt.size(catalog["employments"])    

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def req_9(data_structs):
    """
    Función que soluciona el requerimiento 9
    """
    # TODO: Realizar el requerimiento 9
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

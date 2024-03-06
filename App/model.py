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
import pandas as pd
from datetime import datetime as dt
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
                  data["company_size"],
                  data["workplace_type"],
                  data["open_to_hire_ukrainians"],
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

def newJob(id, published_at, title, company_name, experience_level, country_code, company_size, workplace_type, open_to_hire_ukrainians, city):
    job = {"id":id,
           "published_at":published_at,
           "title":title,
           "company_name":company_name,
           "experience_level": experience_level,
           "country_code": country_code,
           "company_size": company_size,
           "workplace_type": workplace_type,
           "open_to_hire_ukrainians": open_to_hire_ukrainians,
           "city": city
    }    
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    return job

    
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

def req_1(data_structs, Number, country_code, level):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    oferta=[]
    for item in data_structs["jobs"]["elements"]:
        if country_code in item["country_code"] and level in item["experience_level"]:
            oferta.append(item)
            if len(oferta) == Number:
                return oferta
    if len(oferta)<Number:
        return oferta


def req_2(data_structs, ciudad_oferta, nombre_empresa, n_ofertas):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    oferta = []
    for value in data_structs["jobs"]["elements"]:
        if ciudad_oferta in value["city"] and nombre_empresa in value["company_name"]:
            oferta.append(value)
            if len(oferta) == n_ofertas:
                return oferta
    if len(oferta)<n_ofertas:
        return oferta


def req_3(nombre_empresa, fecha_inicial, fecha_final, data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    ofertas = []
    def nueva_oferta(fecha, empleo, habilidad, ciudad, pais, tamaño, tipo_lugar, ucranianos):
        dict_oferta = {"fecha": fecha,
                       "empleo": empleo,
                       "habilidad": habilidad,
                       "ciudad": ciudad,
                       "pais": pais,
                       "tamaño": tamaño,
                       "tipo_lugar": tipo_lugar,
                       "ucranianos": ucranianos}
        return dict_oferta
    anio_inicial = int(fecha_inicial[:4])
    mes_inicial = int(fecha_inicial[6:7])
    dia_inicial = int(fecha_inicial[9:10])
    anio_final = int(fecha_final[:4])
    mes_final = int(fecha_final[6:7])
    dia_final = int(fecha_final[9:10])
    for item in data_structs["jobs"]["elements"]:
        fecha_oferta = item["published_at"]
        anio_oferta = int(fecha_oferta[:4])
        mes_oferta = int(fecha_oferta[6:7])
        dia_oferta = int(fecha_oferta[9:10])
        if (nombre_empresa == item["company_name"] and anio_oferta >= anio_inicial and anio_oferta <= anio_final and 
            mes_oferta >= mes_inicial and mes_oferta <= mes_final and dia_oferta >= dia_inicial and dia_oferta <= dia_final):
            oferta = nueva_oferta(fecha_oferta, item["title"], item["experience_level"], item["city"], item["country_code"], item["company_size"],
                   item["workplace_type"], item["open_to_hire_ukrainians"])
            ofertas.append(oferta)
    ofertas_ordenadas = sorted(ofertas, key=lambda x: (x["fecha"], x["pais"]))
    return ofertas_ordenadas


def req_4(data_structs, country_code, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    oferta=[]
    fecha_inicial=dt.strptime(fecha_inicial, "%Y-%m-%dT%H:%M:%S.%fZ")
    fecha_final=dt.strptime(fecha_final, "%Y-%m-%dT%H:%M:%S.%fZ")
    for item in data_structs["jobs"]["elements"]:
        if country_code in item["country_code"]:
            a=item["published_at"]
            a=dt.strptime(a, "%Y-%m-%dT%H:%M:%S.%fZ")
            if a>fecha_inicial and a<fecha_final:
                oferta.append(item)
    ciudades={}
    empresas={}
    a=len(oferta)
    for item in oferta:
        if item["city"] not in ciudades:
            ciudades[item["city"]]=1
        else:
            ciudades[item["city"]]+=1
    for item in oferta:
        if item["company_name"] not in empresas:
            empresas[item["company_name"]]=1
    num_empresas=len(empresas)
    num_ciudades=len(ciudades)
    mayor= max(ciudades, key=ciudades.get)
    menor= min(ciudades, key=ciudades.get)
    return oferta , a, ciudades, num_ciudades, num_empresas, mayor, menor
            


def req_5(data_structs, ciudad, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    datetime.strptime(fecha_inicial, "%Y-%m-%dT%H:%M:%S.%fZ")
    datetime.strptime(fecha_final, "%Y-%m-%dT%H:%M:%S.%fZ")
    lista_temporal = []
    for item in data_structs["jobs"]["elements"]:
        if item["city"] == ciudad:
            a = item["company_name"]
            b = item["city"]
            c = item["published_at"]
            d = item["title"]
            e = item["workplace_type"]
            f = item["company_size"]
            tupla_general = (c, d, a, e, f)
            lista_temporal.append(tupla_general)
            
    index = 0
    return_lista = []
    for index in range (0, len(lista_temporal)):
        fecha = datetime.strptime(lista_temporal[index][0], "%Y-%m-%dT%H:%M:%S.%fZ")
        if fecha_final.year + fecha_final.month + fecha_final.day + fecha_final.hour + fecha_final.minute + fecha_final.second > fecha.year + fecha.month + fecha.day + fecha.hour + fecha.minute + fecha.second > fecha_inicial.year + fecha_inicial.month + fecha_inicial.day+ fecha_inicial.hour+ fecha_inicial.minute+ fecha_inicial.second:
            return_lista.append(lista_temporal[index])
            
    index = 0
    counter_n_empresas = 0
    for anothervalues in return_lista:
        if anothervalues[index][2] not in return_lista[index + 1]:
            counter_n_empresas +=1
            index +=1
    index = 0
    dict_empresas = {}
    for notanothercounter in return_lista:
        if return_lista[notanothercounter][index][2] in dict_empresas:
            dict_empresas[return_lista[notanothercounter][2]] += 1
            index += 1
        else:
            dict_empresas[return_lista[notanothercounter][2]] = 1
            index += 1
            
    mayor_n = max(dict_empresas, key=dict_empresas.get)
    menor_n = min(dict_empresas, key=dict_empresas.get)
    
    return0_lista = []
    for i in len(return_lista):
        return0_lista.append(return_lista[i][0], return_lista[i][1], return_lista[i][2], return_lista[i][3], return_lista[i][4])
    return return0_lista, len(return0_lista), counter_n_empresas, mayor_n, menor_n


def req_6(data_structs, top, habilidad, fecha_inicial, fecha_final, pais):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    def salario_to_int(salario):
        if salario == "":
            return None
        return int(salario)
    data_trabajos = pd.DataFrame(data_structs["jobs"]["elements"])
    data_habilidades = pd.DataFrame(data_structs["employments"]["elements"])
    data_habilidades["salary_from"] = data_habilidades["salary_from"].apply(salario_to_int)
    data_habilidades["salary_to"] = data_habilidades["salary_to"].apply(salario_to_int)
    data_habilidades = data_habilidades.dropna()
    data_trabajos["average_maximum_salary"] = sum(data_habilidades["salary_to"]) / data_habilidades.shape[0]
    data_trabajos["average_minimum_salary"] = sum(data_habilidades["salary_from"]) / data_habilidades.shape[0]
    if pais != "":
        trabajos_ordenados = data_trabajos[(data_trabajos["experience_level"] == habilidad) & (data_trabajos["published_at"] >= fecha_inicial) & (data_trabajos["published_at"] <= fecha_final) & (data_trabajos["country_code"] == pais)]
    else:
        trabajos_ordenados = data_trabajos[(data_trabajos["experience_level"] == habilidad) & (data_trabajos["published_at"] >= fecha_inicial) & (data_trabajos["published_at"] <= fecha_final)]
    ciudades = trabajos_ordenados.groupby("city")["city"].nunique()
    print(ciudades)


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

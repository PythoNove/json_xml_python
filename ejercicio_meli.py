#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import matplotlib.pyplot as plt
import matplotlib.axes
import mplcursors


def fetch(query):
    response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20'+query+'%20&limit=50')
    dataset = response.json()
    dataset = dataset.get("results")

    dataset = [{"price": dataset[x].get("price"), "condition": dataset[x].get("condition")} 
                for x in range(len(dataset)) if dataset[x].get("currency_id") == "ARS"]
    
    return dataset


def transform(dataset, minimo, maximo):
    
    
    # precio 
    min_count = len([1 for x in range(len(dataset)) if dataset[x].get("price") < minimo])
    min_max_count = len([1 for x in range(len(dataset)) 
                    if dataset[x].get("price") >= minimo and dataset[x].get("price") <= maximo])
    max_count = len([1 for x in range(len(dataset)) if dataset[x].get("price") > maximo])
    
    return [min_count, min_max_count, max_count]


def report(data, minimo, maximo):

    index = ['< '+str(minimo), 'entre '+str(minimo)+' y '+str(maximo), '> '+str(maximo)]

    # grafico de torta
    fig = plt.figure()
    fig.suptitle('Precios de alquileres', fontsize=16)
    ax = fig.add_subplot()
    ax.pie(data, labels=index, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    print("Ejercicio_Meli")

    query = "Mendoza" # input('Indique una provincia a consultar: ')
    dataset = fetch(query)
    
    minimo = int(input("indicar valor minimo: "))
    maximo = int(input("Indicar valor maximo: "))
    
    data = transform(dataset, minimo, maximo)
    report(data, minimo, maximo)

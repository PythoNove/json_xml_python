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


def fetch(page_number, location_id):
    
    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=' + page_number

    response = requests.get(url)
    dataset = response.json()
    dataset = dataset.get("data") # solo se utilizara los valores de la key "data"
    
    dataset = [{"userId": dataset[x].get("userId"), "amount": dataset[x].get("amount")} 
                for x in range(len(dataset)) if dataset[x].get("location").get("id") == location_id]

    return dataset


def transform(dataset):

    # eliminar $ y , (no me funcionó el strim en la descripción del ejercicio (o no lo supe implementar))
    dataset = [[dataset[x].get('userId'), float(dataset[x].get("amount").replace('$','').replace(',',''))] 
                for x in range(len(dataset))]
    
    # extraer usuarios sin repeticiones 
    usuarios = set([usuario[0] for usuario in dataset])

    # sumar valores de los usuarios (intenté con comprensión de listas pero no me salió)   
    data = []
    for usuario in usuarios:
        acum = 0
        for lista in dataset:
            if lista[0] == usuario:
                acum += lista[1]
        data.append([usuario, acum])
    
    return data


def report(data):
 
    # formar listas para gráfico [x] e [y]
    x = ["Usuario " + str(lista[0]) for lista in data]
    y = [lista[1] for lista in data]
 
    # gráfico de barras (seguramente mejorable el aspector del gráfico)
    fig = plt.figure()
    fig.suptitle('Gastos de usuarios', fontsize=16)
    ax = fig.add_subplot()
    ax.bar(x, y, label='Usuarios')
    ax.set_facecolor('lightgray')
    ax.set_xlabel('Usuarios')
    ax.set_ylabel('Compras en pesos')
    ax.grid(ls='dashed')
    plt.show()

    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
     
    page_number = input('ingrese numero de pagina entre 1 y 16: ') # preguntar numero de pagina
    location_id = int(input('ingrese location_id): ')) # preguntar la location_id que se desea consultar
    
    dataset = fetch(page_number, location_id)          
    data = transform(dataset)
    report(data)
    
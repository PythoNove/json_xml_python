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
import xml.etree.ElementTree as ET
import collections
import matplotlib.pyplot as plt
import matplotlib.axes

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    json_data = {
                 "nombre": "Diego", 
                 "Apellido": "Farias", 
                 "DNI": "26740185",
                 "Prenda": [
                     {
                     "zapatillas": "2",
                     "campera": "1",
                     "buzo": "1",
                     "medias": "2",
                     "pantalon": "1"
                     }
                 ] 
    } 

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    with open("json_data.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    # Observe el archivo y verifique que se almaceno lo deseado

    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    with open("json_data.json", "r") as jsonfile:
        nuevo_archivo = json.load(jsonfile)

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    
    nuevo_archivo = json.dumps(nuevo_archivo, indent=4)
    print(nuevo_archivo)
    
    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.
    
    '''
    Archivo legajos.xml
    
    <DATOS>
        <legajo>000125-20</legajo>
        <nombre>CARLOS ANDRES MORALES</nombre>
        <fecha_nac>10-12-1965</fecha_nac>
        <provincia_res>Mendoza</provincia_res>
        <estado_civil>casado</estado_civil>
        <familiares name='Hijos'>
            <nombre>CARLA MORALES</nombre>
            <edad>20</edad>
            <nombre>SEBASTIAN MORALES</nombre>
            <edad>17</edad>
        </familiares>
        <familiares name='Padres'>
            <nombre>PEDRO MORALES</nombre>
            <edad>72</edad>
            <nombre>ROSA LINARES</nombre>
            <edad>68</edad>
        </familiares>
        <legajo>000126-20</legajo>
        <nombre>CARINA ROSAS</nombre>
        <fecha_nac>07-05-1972</fecha_nac>
        <provincia_res>San Luis</provincia_res>
        <estado_civil>casado</estado_civil>
        <familiares name='Hijos'>
            <nombre>YANINA NUNEZ</nombre>
            <edad>24</edad>
        </familiares>
        <familiares name='Padres'>
            <nombre>ROGELIO ROSAS</nombre>
            <edad>67</edad>
            <nombre>ELSA MIRAS</nombre>
            <edad>63</edad>
            </familiares>
    </DATOS>
    '''
    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('legajos.xml')
    root =tree.getroot()

    for empleado in root:
        print('tag:', empleado.tag, 'attr', empleado.attrib, 'text:', empleado.text)
        for familiares in empleado:
            print('tag:', familiares.tag, 'attr', familiares.attrib, 'text:', familiares.text)

    pass

def ej5():
    # Ejercicio de consumo de datos por API
    # url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
    
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()

    iserId_completed = [data[x].get('userId') for x in range(len(data)) 
                        if data[x].get("completed") == True]
    iserId_completed = collections.Counter(iserId_completed)

    # gráfico tipo torta
    fig = plt.figure('Archivo data')
    fig.suptitle('Titulos completos por usuario', fontsize=12)
    ax = fig.add_subplot()
    explode = (0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0.1)

    ax.pie(iserId_completed.values(), autopct='%1.1f%%', startangle=90, 
            labels=iserId_completed.keys(), shadow=True, explode=explode)
    ax.axis('equal')
    plt.show()    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    ej5()

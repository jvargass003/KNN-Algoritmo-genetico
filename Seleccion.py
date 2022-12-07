# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Algoritmos Genéticos
TEMA: Proyecto
Alumno: Jessica Vargas Sánchez, Luis Fernando Samano Rivera y Joel Ramirez Martinez
Profesor: Dr. Asdrúbal López Chau
Descripción: Un algoritmo de agrupamiento consiste en crear grupos o aglomerados de datos que tienen cierta similitud entre sí. Para crear los grupos, se puede usar como medida de similitud a la distancia de cada punto hacia un centroide dado. Tomar en cuenta que cada grupo es representado por un centroide, por lo que si hay tres grupos, entonces se tendrán tres centroides. 
Diseñar un algoritmo genético para identenficar K grupos de objetos en un conjunto de datos proporcionado.
Consideraciones:
a) Los datos no son etiquetados, y se proporcionan en formato CSV.
b) El número de grupos (K) lo da el usuario
c) Se grafican los datos como puntos, asigando un color diferente a los datos pertenecientes a cada grupo. Es decir, si hay K grupos, entonces habrán puntos de K colores.

@author: jessi
"""
import numpy as np
import random

class Seleccion:
    def selecciona(self, aptitudes, k=2):
        """
        Descripción: Realiza la selección de individuos según se aptitud
            Parametros: 
                aptitudes: Valor que a optenido el individuo según su solución
                k = cantidad de individuos seleccionados
            Return:
                cromosoma: Valor de un individuo
        
        """
        # Darle chance a los feos
        aptitudes = np.array(aptitudes) + .01
        '''        
        denom = np.sum(np.exp(aptitudes))
        probabilidades = []
        for aptitud in aptitudes:
            probabilidades.append(np.exp(aptitud)/denom)
        '''
        #Calcula la probabilidades de todos los individuos, segun su valor de adtitus
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes))for aptitud in aptitudes]
        #Identifica los indices de cada individuo y los alamacea
        indices = list(range(len(aptitudes)))
        #Retorna el indice de k individuos, con mayor probabilidad 
        return random.choices(indices, probabilidades, k=k)
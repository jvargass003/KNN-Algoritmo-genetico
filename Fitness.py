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
class Fitness:
    def __init__(self):
        '''
        Permite calcular que tan buena es una solución.

        Parameters
        ----------

        Returns
        -------
        None.

        '''
        self.lamda = 1
        self.beta = 1
    def evaluate(self,ind):
        '''
        Obtiene el valor de una solución, considerando las distancias.

        Parameters
        ----------
        ind : Individuo
            DESCRIPTION. Se evalua si el valor del grupos que se contine en el gen
            es bueno.

        Returns
        -------
        float
            DESCRIPTION. Resultado de lo obtenido de la funsión exponencial,
            con respecto a la suma de distancia de cada puntos al centroide.
        '''
        distancias = ind.calcularDistancias()
        suma = 0.0
        for i in range(len(distancias)):
            if distancias[i] == None:
                suma += 0
            else:
                suma += distancias[i]
        return self.beta * np.exp(-self.lamda*suma)
        
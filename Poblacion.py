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

from Individuo import Individuo 
class Poblacion: 
    
    def __init__(self,objetos,k,size=100):
        self.k=k
        self.objetos = objetos
        self.size = size

    def inicializa(self):
        '''
        Se inicializa la población, creando individuos e inicializandolos

        Returns
        -------
        None.

        '''
        poblacion = []#Se crea la población
        for i in range(self.size):
            ind = Individuo(self.objetos,int(self.k))#Se crea individuo
            ind.init()#Se inicializa
            poblacion.append(ind)#Se agrega a la población
        self.poblacion = poblacion
    


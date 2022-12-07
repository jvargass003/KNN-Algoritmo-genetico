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

import random
import numpy as np
import math
from Cromosoma import CromosomaEntero as Cromosoma 
class Individuo:
    
    def __init__(self,objetos,k):
        '''
        Crea un individuo nuevo.

        Parameters
        ----------
        objetos : list
            DESCRIPTION. Coorndeadas de los puntos.
        k : int
            DESCRIPTION. Número de grupos.

        Returns
        -------
        None.

        '''
        self.objetos = objetos
        self.k = k
        #Se crea un promosoma
        self.cromosoma= Cromosoma(self.objetos, self.k) 
        
    def init(self):
        '''
        Se inicializa el cromosoma, creado anteriormente.

        Returns
        -------
        None.

        '''
        self.cromosoma.init()

    def cruza(self, madre):
        '''
        Se realiza una cruza entre el individuo actual y el resivido.

        Parameters
        ----------
        madre : Inidividuo
            DESCRIPTION. Individuo con el que se realiza la cruza.

        Returns
        -------
        list
            DESCRIPTION. Dos nuevos individuos.

        '''
        c1 , c2 = self.cromosoma.cruzar(madre.cromosoma)
        ind1 = Individuo(self.objetos, self.k)
        ind2 = Individuo(self.objetos, self.k)
        ind1.cromosoma = c1
        ind2.cromosoma = c2
        return [ind1,ind2]
    
    def mutar(self):
        '''
        Se realiza la mutación del individuo.

        Returns
        -------
        None.

        '''
        self.cromosoma.mutar()
    def getValues(self):
        '''
        Se obtiene el valor decodificado del individuo.

        Returns
        -------
        list
            DESCRIPTION. Valores decodificados del individuo.

        '''
        return self.cromosoma.getValues()
    def __str__(self):
        '''
        Se obtienen los valores codificados del individuo.

        Returns
        -------
        list
            DESCRIPTION. Valores codificados del individuo.

        '''
        return self.cromosoma.__str__()
    def calcularDistancias(self):
        '''
        Se calculas las distancias de cada punto a su respectivo centroide,
        de tal forma que se obtenga las distancias totales a cada centroide,
        con su respectivos puntos.

        Returns
        -------
        distancias : list
            DESCRIPTION. Distancias totalen entre cada centroide y sus puntos.

        '''
        #Se obtienen los centroides
        centroides = self.cromosoma.calcularCentroides()
        #print("Centroides: ",centroides)
        #print("Objetos: ",self.objetos)
        #Se obtienen los genes del indiciduo por medio del cromosoma.
        genes = self.cromosoma.genes
        distancias = []
        distancia = 0
        dSuma = 0
        #Se calcula la distancia entre los puntos y los centroides.
        for i in range(0,self.k):
            dSuma = 0
            for a in range(len(genes)):
                distancia = 0
                if i+1 == genes[a].getValue():
                    #Formula para obtener la distancia entre dos puntos.
                    distancia = math.sqrt(pow(((centroides[i][0])-(genes[a].getObjeto()[0])),2)+pow(((centroides[i][1])-(genes[a].getObjeto()[1])),2))
                    genes[a].distancia = distancia
                    dSuma += distancia
            if dSuma == 0:
                distancias.append(None)
            else:
                distancias.append(dSuma)
        return distancias

                    
                    
                    
            
            
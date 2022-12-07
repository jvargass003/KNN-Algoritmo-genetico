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

Created on Tue May 24 17:12:37 2022

@author: jessi
"""
from Gen import GenEntero as Entero
import random

class CromosomaEntero:
    
    def __init__(self,objetos,k):
        '''
        Permite crear un cromosoma, de tal forma que cada objeto contenga
        un número de grupo.

        Parameters
        ----------
        objetos : list
            DESCRIPTION. Coordenadas de los objetos.
        k : int
            DESCRIPTION. Número de gurpos.

        Returns
        -------
        None.

        '''
        self.objetos=objetos
        self.k = k
        self.genes = []
        
        #Se crean los genes que contrera este cromosoma y se almacenan 
        #en una lista
        for obj in range(len(self.objetos)):
            gen = Entero(self.k,objetos[obj])
            self.genes.append(gen)
            
    def init(self):
        '''
        Permite inicializar el cromosoma, de tal manera que los genes que 
        se han creado anteriormente se inicialicen uno a uno.

        Returns
        -------
        None.

        '''
        for gen in self.genes:
            gen.inicializar()
        

    def __str__(self):
        '''
        Método que permite extraer de cada unos de los genes su valor 
        codificado y agregarlos a una sola cadena, la cual será el valor 
        del cromosoma codificado.

        Returns
        -------
        cad : String 
            DESCRIPTION. Valores codificados de los genes.

        '''
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad
    def getValues(self):
        '''
        Método que permite obtener los valores decodificados del cromosoma,
        obteniendo cada uno de los valores del gen decodificado.

        Returns
        -------
        values : int
            DESCRIPTION. Valores decodificados de los genes.

        '''
        values = []
        for gen in self.genes:
            values.append(gen.getValue())
        return values

    def cruzar(self, madre):
        '''
        Método que permite realizar la cruza entre dos cromosomas, 
        esto se hace a partir del valor de la madre y padre, cruzando
        de tal forma valores de grupos asignados al mismo objeto.

        Parameters
        ----------
        madre : CromosomaEntero
            DESCRIPTION. Valor del cromosoma con el cual se realizara la 
            cruza del cromosoma actual.

        Returns
        -------
        hijos
            DESCRIPTION. Nuevos cromosomas, resultados de la cruza de los 
            dos cromosomas actuales.

        '''
        genesHijos1 = []
        genesHijos2 = []
        for papa, mama in zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genesHijos1.append(g[0])
            genesHijos2.append(g[1])
        h1 = CromosomaEntero(self.objetos,self.k)
        h2 = CromosomaEntero(self.objetos,self.k)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
    
    def mutar(self):
        '''
        Se realiza la mutación del cromosoma actual. 

        Returns
        -------
        None.

        '''
        #Se obtiene el indice de uno de los genes del cromosoma para mutar.
        idx = random.randint(0, len(self.objetos)-1)
        #Se inicializa.
        self.genes[idx].mutar()
    
    def getObjetos(self):
        '''
        Se obtienen los valores de las coordenadas de casa uno de los grupos.

        Returns
        -------
        objs : list
            DESCRIPTION. Valores de coorenadas de los objetos.

        '''
        objs = []
        for gen in self.genes:
            objs.append(gen.getObjeto())
        return objs
    
    def calcularCentroides(self):
        '''
        Calcula los valores de los k grupos. Sumando todas las coordenadas
        de los puntos que se encuentran en ese grupo y dividiendilo entre el
        total de puntos que pertenecen a ese grupo.

        Returns
        -------
        centroides : lits
            DESCRIPTION. Coordenadas del centroide de cada grupo.

        '''
        centroides = []
        sumax = 0
        sumay = 0
        numeroGrupo = 0
        for i in range(self.k):
            sumax = 0
            sumay = 0
            numeroGrupo = 0
            for gen in self.genes:
               if gen.getValue() == i+1:
                   numeroGrupo += 1
                   x, y = gen.getObjeto()#Se obtiene el valor de las cooredanas de ese punto
                   sumax += x #Se agregan a x
                   sumay += y #Se agregan a y
            if sumax == 0 or sumay == 0:
                centroides.append([0,0])#En caso de que el grupo no contenga
                #objetos se asigna un centroide de [0,0]
            else:
                #Se obtiene el promedio de las sumas y los puntos por grupos
                #se asignan en orden de los grupos.
                centroides.append([sumax/numeroGrupo,sumay/numeroGrupo]) 
        return centroides

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
from Seleccion import Seleccion
from Fitness import Fitness
from Poblacion import Poblacion
import numpy as np
import random 
class AlgoritmoEvolutivo:
    
    def __init__(self,objetos,k,size=100):
        self.pob = None
        self.objetos = objetos
        self.k = k
        self.size = size
        
        
    def inicializa(self):
        pob = Poblacion(self.objetos,self.k)
        pob.inicializa()
        self.pob = pob
        self.seleccion = Seleccion()
        self.ff = Fitness()
        
    def mejorIndividuo(self,aptitudes,poblacion,generacion):
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        self.centride = poblacion[idxMejor].cromosoma.calcularCentroides()
        self.mIndividuo = poblacion[idxMejor].getValues()
        
    def evolucion(self,generacion):
        if self.pob is None:
            print("Inicialice la población")
            return
        #1) Evaluar individuos
        poblacion = self.pob.poblacion          
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]
        # # 2) Seleccionar padres para cruza
        k = int(self.size/2)
        if k%2 == 1:
            k += 1
        idx = self.seleccion.selecciona(aptitudes,k)
        #3) Generar hijos (cruza)
        descendencia = []
        for i in list(range(0,k-1,2)):
            ip = idx[i]
            im = idx[i+1]
            papa = poblacion[ip]
            mama = poblacion[im]
            hijos = papa.cruza(mama)
            descendencia.append(hijos[0])
            descendencia.append(hijos[1])
        
        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.5))
        
        for i in range(totalMutar):
            idx = random.choice(range(len(descendencia)))
            descendencia[idx].mutar()
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente 
        #     población
        
        # Junto padres e hijos
        for hijo in descendencia:
            poblacion.append(hijo)
        # calculo aptitudes de todos
        aptitudes = [self.ff.evaluate(ind) 
                     for ind in poblacion]
        # ELITISMO!!!!!
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        # Selecciono indices de 
        # individuos para la siguiente generacion
        idx = self.seleccion.selecciona(aptitudes,
                                  self.size)
        # Creo la lista de individuos de la siguiente
        # generación

        for i in idx:
            siguientePob.append(poblacion[i])
        # Guardo para la siguiente evolución
        self.pob.poblacion = siguientePob
        self.mejorIndividuo(aptitudes,poblacion,generacion)
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
import numpy as np
import random 
import math
class GenEntero:
    def __init__(self,k,objeto):
        '''
        Método que permite crear el gen, en el se define el número de bits
        que el gen podra contener, de igual forma de inicializan diversos 
        atributos que contendrá el gen.

        Parameters
        ----------
        k : int
            DESCRIPTION. Cantidad de grupos en los cuales se dividiran los 
            objetos.
        objeto : list 
            DESCRIPTION. Valor de las coordenadas, que se asignaran a este 
            gen.

        Returns
        -------
        None.

        '''
        self.k = k
        #Se calcula la cantidad de bits que se necesitan para este gen. 
        #se obtiene el techo de la raíz cuadrada del número de grupos.
        self.nbits = math.ceil(math.sqrt(self.k)) 
        self.objeto = objeto #
        #Atributo en el que posteriormente se almacenara la distancia de este
        #objeto al centroide.
        self.distancia = 0
    
    def inicializar(self):
        '''
        Método que permite inicializar el gen.

        Returns
        -------
        None.

        '''
        #Se genera de manera estocastica un número en binario, que se limita
        #por la cantidad de bits que se a calculado al crear el gen.
        self.gen = random.choices([0,1],k=self.nbits)
        #Se verifica que el gen que se ha creado pertenezca al rango de 1 a K
        while(True):
            if self.getValue() > self.k or self.getValue() == 0:
                #En caso que el gen no se encuentre dentro del rango se crea
                #nuevamente y se vuelve a realizar la evaluación.
                self.gen = random.choices([0,1],k=self.nbits)
            else:
                #En caso que el gen se encuentre dentro del rango se define
                #como el definitivo.
                break
       

            
    def cruzar(self, genMadre):
        '''
        Méto que realiza la cruza entre el gen del mismo objeto.

        Parameters
        ----------
        genMadre : GenEntero 
            DESCRIPTION. Gen madre, que permite gracias a sus atributos 
            realizar la cruza.

        Returns
        -------
        list
            DESCRIPTION. Hijos que se generan a partir de la madre y el padre.

        '''
        padre = self.gen.copy()
        madre = genMadre.gen.copy()
        #A continuación, se realiza una cruza con división de de partes, de tal
        #forma que se obtienen 3 boloques que se cruzaran entre si 
        cp1 = int(np.ceil((self.nbits - 1)/3.))
        cp2 = 2 * cp1
        son1 = padre[0:cp1]
        son1.extend(madre[cp1:cp2])
        son1.extend(padre[cp2:])
        

        son2 = madre[0:cp1]
        son2.extend(padre[cp1:cp2])
        son2.extend(madre[cp2:])
        
        #Se crean dos nuevos genes 
        s1 = GenEntero(self.k,self.objeto)
        s2 = GenEntero(self.k,self.objeto)
        
        #Se asignan los datos al gen
        s1.gen = son1
        s2.gen = son2
        
        #Se evalua si el gen es valido, de tal forma que aun cuando se 
        #realiza la cruza cuampla con el rango de 1 a k.
        self.validarGen(s1)
        self.validarGen(s2)
        
        #Retorno de los hijos
        return [s1,s2]
       
    def validarGen(self,gen):
        '''
        Permite validar si un gen se encuentra deltro del rango, en caso de
        no ser así se realiza un ajuste que permita que este se encuntre en 
        rango.

        Parameters
        ----------
        gen : GenEntero
            DESCRIPTION. Gen del cual se realiza una validación.

        Returns
        -------
        None.

        '''
        valor = gen.getValue() #Se obtiene el valor en decimal del gen.
        #En caso de que el valor se más mayor a k o igual a 0.
        if valor > self.k or valor == 0:
            #Se obtiene el modulo del modulo, del valor entre k.
            hn = valor%self.k#Nuevo calor del gen
            #En caso de que el resultado de este modulo sea 0.
            if hn == 0:
                gen.inicializar()#Se inicializa el gen.
            else:
                #Si no.
                #Se obtiene su valor codificado.
                valorBinario = int(bin(hn)[2:])
                valorBinario = [int(x) for x in str(valorBinario)]
                #Se al gen codificado no tiene la misma cantidad de nBist
                #sera necesario agregar 0, que permitan que el gen obtenga 
                #el tamaño adecuado.
                if len(valorBinario) < self.nbits:
                    #Se agregan los 0s, necesarios.
                    nuevogen = [0] * (self.nbits-len(valorBinario))
                    #Se asigna el nuevo valor al gen.
                    gen.gen = nuevogen+valorBinario
                else:
                    #Se asigna el nuevo valor al gen.
                    gen.gen = valorBinario
            
    def mutar(self):
        '''
        Permite cambiar por completo al gen, de tal forma que se muta.

        Returns
        -------
        None.

        '''
        self.inicializar()#Se inicializa el gen.
    
    def __str__(self):
        '''
        Método para obtener el valor codificado del gen.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return str(self.gen)
    
    def getValue(self):
        '''
        Método para obtener el valor decodificado del gen.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return  int(''.join([str(i) for i in self.gen[:]]), 2)
    
    def getObjeto(self):
        """
        Se obtiene el objeto que a sido asignado a este gen.
        
        Returns
        -------
        list
            DESCRIPTION. Coordenadas el objeto. 

        """
        return self.objeto

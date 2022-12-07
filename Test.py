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
import pandas as pd
import matplotlib.pyplot as plt
from AlgoritmoEvolutivo import AlgoritmoEvolutivo 
import matplotlib.colors as mcolors

#Se leen y grafican las coordenadas de los puntos.
objetos= pd.read_csv('Coordenadas.txt')
obj = np.array(objetos).tolist()
x = []
y = []
for i in range(len(obj)):
    x.append(obj[i][0])
    y.append(obj[i][1])
#Se grafican las cooredenadas
plt.plot(x, y,"o")
plt.show()

#Se obtiene una lista de colores, los cualen permitiran dar color a cada uno de los
#puntos segun sea el grupo al que pertenece.
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
nombres = [name for hsv, name in by_hsv]
nombres_colores = ["black","blue","red","green","yellow","pink","oragne","violet","brown"]
nombres_colores = nombres_colores+nombres

#Se genera el algoritmo genetico.
k = int(input("Ingrese la cantidad de grupos: "))
generaciones = 150
ae = AlgoritmoEvolutivo(obj, k)
ae.inicializa()
mejores = []
crentroide = []
for i in range(generaciones):
    print("Generacion: ",i+1)
    ae.evolucion(i+1)
    if i >= generaciones-1:
        crentroide = ae.centride #Se obtiene los centroides del mejor individuo
        mejores = ae.mIndividuo #Se optiene el mejor individuos 
    print(ae.centride)
    print(ae.mIndividuo)

print("\nMejor individuo")
print(crentroide)
print(mejores)

#Se grafican nuevamentos los puntos, pero cada uno con el color que le corresponde
#dependiendo de su grupo.
for n in range(1,k+1):
    for m in range(len(obj)):
        if mejores[m] == n:
            plt.scatter(obj[m][0], obj[m][1],c=nombres_colores[n])
    plt.scatter(crentroide[n-1][0],crentroide[n-1][1],c=nombres_colores[0])
plt.show()           







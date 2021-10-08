#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Instancia 1
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos
def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
posiciones_libres=[[1,38,1],[9,25,1],[10,29,2],[1,18,1],[8,21,2],[7,8,2],[4,33,2],[10,25,1],[6,2,4],[1,4,4],[8,37,1],[2,30,3],[10,38,3],[2,37,4],[9,19,2],[3,14,2]]
llegada_contenedores=[88,112,80,183,127,112,109,87]
tipo=[1,2,1,2,2,1,2,1]
movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+(abs(pos_llegada[2]-pos[2]))+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1])))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))
    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break
    
    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)
    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i ==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
soluciones_buenas=[]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
cogida_contenedores=[2, 7, 0, 6, 1, 5, 4, 3]
posicion_contenedores=[8, 9, 5, 12, 13, 15, 0, 10]
FO=333
[[2, 7, 0, 6, 1, 5, 4, 3],[8, 9, 5, 12, 13, 15, 0, 10],333]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=24
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[0],soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1

# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

i=len(cogida_contenedores)-1
print(la_mejor)
while i>=0:
    vector_bl1=[]
    vector_bl2=[]
    for j in range(0,len(la_mejor[0])):
        vector_bl1.append(la_mejor[0][j])
        vector_bl2.append(la_mejor[1][j])
    j=len(cogida_contenedores)-1
    while j>=0:
        if i==j:
            vector_bl1[j]=la_mejor[0][(j-1)]
            vector_bl2[j]=la_mejor[1][(j-1)]
        elif j==i-1:
            vector_bl1[j]=la_mejor[0][(j+1)]
            vector_bl2[j]=la_mejor[1][(j+1)]
        else:
            vector_bl1[j]=la_mejor[0][j]
            vector_bl2[j]=la_mejor[1][j]
        j=j-1
    FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
    FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
    if FObl<FObl2:
        if FObl<la_mejor[2]:
            la_mejor=[vector_bl1,vector_bl2,FObl]
    else:
        if FObl2<la_mejor[2]:
            la_mejor=[vector_bl1,la_mejor[1],FObl2]
    i=i-1

for i in range(0,len(cogida_contenedores)-1):
    vector_bl1=[]
    vector_bl2=[]
    for j in range(0,len(cogida_contenedores)):
        if i==j:
            vector_bl1.append(la_mejor[0][j+1])
            vector_bl2.append(la_mejor[1][j+1])
        elif j==i+1:
            vector_bl1.append(la_mejor[0][j-1])
            vector_bl2.append(la_mejor[1][j-1])
        else:
            vector_bl1.append(la_mejor[0][j])
            vector_bl2.append(la_mejor[1][j])
    FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
    FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
    if FObl<FObl2:
        if FObl<la_mejor[2]:
            la_mejor=[vector_bl1,vector_bl2,FObl]
    else:
        if FObl2<la_mejor[2]:
            la_mejor=[vector_bl1,la_mejor[1],FObl2]

print(la_mejor)
guardar_sol=[]
guardar_sol.append(la_mejor)
j=0
while j==0:
    j=1
    for i in range(0,len(cogida_contenedores)):
        solucion2=la_mejor[1]
        for j in range(0,len(posiciones_libres)-1):
            vec_aux=[]
            if j not in solucion2:
                for k in range(0,len(la_mejor[1])):
                    if k==i:
                        vec_aux.append(j)
                    else:
                        vec_aux.append(solucion2[k])
                FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                if FO<la_mejor[2]:
                    guardar_sol.append([la_mejor[0],vec_aux,FO])
                    la_mejor=[la_mejor[0],vec_aux,FO]
                    j=0
print(la_mejor)


# In[23]:


#Instancia 2
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos

def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
posiciones_libres=[[7,41,4],[9,12,3],[8,38,1],[7,9,2],[2,23,3],[2,21,4],[3,15,1],[6,24,4],[9,1,4],[10,6,3],[1,38,2],[5,31,2],[2,34,1],[1,3,3],[3,18,3],[10,19,2]]
llegada_contenedores=[158,144,69,158,196,9,34,95]
tipo=[2,2,2,1,1,1,2,2]
movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))+abs(pos_llegada[2]-pos[2]))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))
    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break
        
    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)

    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
soluciones_buenas=[]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
cogida_contenedores=[5, 6, 2, 7, 1, 0, 3, 4]
posicion_contenedores=[8, 0, 10, 2, 12, 11, 13, 9]
FO=264
[[5, 6, 2, 7, 1, 0, 3, 4],[8, 0, 10, 2, 12, 11, 13, 9],264]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])

#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=24
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[0],soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1

# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

print(la_mejor)

for i in range(0,len(cogida_contenedores)-1):
    vector_bl1=[]
    vector_bl2=[]
    for j in range(0,len(cogida_contenedores)):
        if i==j:
            vector_bl1.append(la_mejor[0][j+1])
            vector_bl2.append(la_mejor[1][j+1])
        elif j==i+1:
            vector_bl1.append(la_mejor[0][j-1])
            vector_bl2.append(la_mejor[1][j-1])
        else:
            vector_bl1.append(la_mejor[0][j])
            vector_bl2.append(la_mejor[1][j])
    FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
    FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
    if FObl<FObl2:
        if FObl<la_mejor[2]:
            la_mejor=[vector_bl1,vector_bl2,FObl]
    else:
        if FObl2<la_mejor[2]:
            la_mejor=[vector_bl1,la_mejor[1],FObl2]

guardar_sol=[]
guardar_sol.append(la_mejor)
j=0
while j==0:
    j=1
    for i in range(0,len(cogida_contenedores)):
        solucion2=la_mejor[1]
        for j in range(0,len(posiciones_libres)-1):
            vec_aux=[]
            if j not in solucion2:
                for k in range(0,len(la_mejor[1])):
                    if k==i:
                        vec_aux.append(j)
                    else:
                        vec_aux.append(solucion2[k])
                FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                if FO<la_mejor[2]:
                    guardar_sol.append([la_mejor[0],vec_aux,FO])
                    la_mejor=[la_mejor[0],vec_aux,FO]
                    j=0
print(la_mejor)


# In[22]:


#instancia 3
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos

def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
llegada_contenedores=[17,100,84,148,117,61,121,82,57,94,56,84,127,150,115,162,96,166,152,36,144,15,82,167,4,56,158,
                      122,127,144,141,136,57,28,2,57,63,165,69,16]
tipo=[2,2,2,1,2,1,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,2,2,1,1,2,2,1,1,1,1]
file = open('Localización.txt')
l=[]
 
for line in file:
    for word in line.split(): 
        l.append(word) 
 
file.close()

h=0
for i in range(0, len(l)):
    if l[i]=="#x,y,z":
        h=h+1
        if h==3:
            k=i
posiciones_libres=[]
vector_aux=[]
for i in range(k+1,len(l)):
    vector_aux.append(int(l[i]))
    if len(vector_aux)==3:
        posiciones_libres.append(vector_aux)
        vector_aux=[]

movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+(abs(pos_llegada[2]-pos[2]))+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1])))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))

    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break

    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)
    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i ==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
soluciones_buenas=[]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
cogida_contenedores=[34, 24, 21, 39, 0, 33, 19, 10, 25, 8, 32, 35, 5, 36, 38, 7, 22, 2, 11, 9, 16, 1, 14, 4, 6, 27, 12, 28, 31, 30, 20, 29, 3, 13, 18, 26, 15, 37, 17, 23]
posicion_contenedores=[49, 29, 44, 103, 99, 18, 31, 36, 114, 1, 45, 8, 104, 0, 56, 67, 108, 71, 110, 19, 32, 47, 23, 55, 96, 91, 62, 119, 78, 21, 58, 107, 82, 6, 9, 16, 52, 72, 92, 50]
FO=1580
[[34, 24, 21, 39, 0, 33, 19, 10, 25, 8, 32, 35, 5, 36, 38, 7, 22, 2, 11, 9, 16, 1, 14, 4, 6, 27, 12, 28, 31, 30, 20, 29, 3, 13, 18, 26, 15, 37, 17, 23],[49, 29, 44, 103, 99, 18, 31, 36, 114, 1, 45, 8, 104, 0, 56, 67, 108, 71, 110, 19, 32, 47, 23, 55, 96, 91, 62, 119, 78, 21, 58, 107, 82, 6, 9, 16, 52, 72, 92, 50],1580]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])

#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=120
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1
# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

la_mejor=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor)
print(la_mejor)


# In[6]:


#Instancia 1
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos
def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
posiciones_libres=[[1,38,1],[9,25,1],[10,29,2],[1,18,1],[8,21,2],[7,8,2],[4,33,2],[10,25,1],[6,2,4],[1,4,4],[8,37,1],[2,30,3],[10,38,3],[2,37,4],[9,19,2],[3,14,2]]
llegada_contenedores=[88,112,80,183,127,112,109,87]
tipo=[1,2,1,2,2,1,2,1]
movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+(abs(pos_llegada[2]-pos[2]))+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1])))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))
    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break
    
    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)
    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i ==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
soluciones_buenas=[]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
cogida_contenedores=[2, 7, 0, 6, 1, 5, 4, 3]
posicion_contenedores=[8, 9, 5, 12, 13, 15, 0, 10]
FO=333
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=24
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
        random_bl=randint(0,99)
        if random_bl==0:
            hijo=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,hijo)
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1
# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

la_mejor=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor)
print(la_mejor)


# In[ ]:


#Instancia 2
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos

def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
posiciones_libres=[[7,41,4],[9,12,3],[8,38,1],[7,9,2],[2,23,3],[2,21,4],[3,15,1],[6,24,4],[9,1,4],[10,6,3],[1,38,2],[5,31,2],[2,34,1],[1,3,3],[3,18,3],[10,19,2]]
llegada_contenedores=[158,144,69,158,196,9,34,95]
tipo=[2,2,2,1,1,1,2,2]
movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))+abs(pos_llegada[2]-pos[2]))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))
    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break
        
    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)

    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
soluciones_buenas=[]
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])
cogida_contenedores=[5, 6, 2, 7, 1, 0, 3, 4]
posicion_contenedores=[8, 0, 10, 2, 12, 11, 13, 9]
FO=264
soluciones_buenas.append([cogida_contenedores,posicion_contenedores,FO])

#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=24
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
        random_bl=randint(0,99)
        if random_bl==0:
            hijo=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,hijo)
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1
# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

la_mejor=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor)
print(la_mejor)


# In[ ]:


#instancia 3
def funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores):
    movimientos=0
    espera=0
    posicion_mar=[5,0,1]
    posicion_tierra=[5,43,2]
    pos=posicion_inicial
    k1=[]
    k2=[]
    for i in range(0,len(cogida_contenedores)):
        k1.append(cogida_contenedores[i])
        if tipo[k1[i]]==1:
            pos_llegada=posicion_mar
        else:
            pos_llegada=posicion_tierra
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1]))
        if llegada_contenedores[k1[i]]>espera+movimientos:
            espera=llegada_contenedores[k1[i]]-movimientos
            movimientos=movimientos+espera
        movimientos=movimientos+abs(pos[2]-pos_llegada[2])
        pos=[pos_llegada[0],pos_llegada[1],5]

        k2.append(posicion_contenedores[i])
        if i!=len(llegada_contenedores)-1:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+2*abs(pos[2]-posiciones_libres[k2[i]][2])
        else:
            movimientos=movimientos+max(abs(pos[0]-posiciones_libres[k2[i]][0]),abs(pos[1]-posiciones_libres[k2[i]][1]))+abs(pos[2]-posiciones_libres[k2[i]][2])
        pos=[posiciones_libres[k2[i]][0],posiciones_libres[k2[i]][1],5]
    return movimientos

def BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor):
    for i in range(0,len(cogida_contenedores)-1):
        vector_bl1=[]
        vector_bl2=[]
        for j in range(0,len(cogida_contenedores)):
            if i==j:
                vector_bl1.append(la_mejor[0][j+1])
                vector_bl2.append(la_mejor[1][j+1])
            elif j==i+1:
                vector_bl1.append(la_mejor[0][j-1])
                vector_bl2.append(la_mejor[1][j-1])
            else:
                vector_bl1.append(la_mejor[0][j])
                vector_bl2.append(la_mejor[1][j])
        FObl=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,vector_bl2)
        FObl2=funcionobjetivo(tipo,llegada_contenedores,vector_bl1,posiciones_libres,posicion_inicial,la_mejor[1])
        if FObl<FObl2:
            if FObl<la_mejor[2]:
                la_mejor=[vector_bl1,vector_bl2,FObl]
        else:
            if FObl2<la_mejor[2]:
                la_mejor=[vector_bl1,la_mejor[1],FObl2]

    guardar_sol=[]
    guardar_sol.append(la_mejor)
    j=0
    while j==0:
        j=1
        for i in range(0,len(cogida_contenedores)):
            solucion2=la_mejor[1]
            for j in range(0,len(posiciones_libres)-1):
                vec_aux=[]
                if j not in solucion2:
                    for k in range(0,len(la_mejor[1])):
                        if k==i:
                            vec_aux.append(j)
                        else:
                            vec_aux.append(solucion2[k])
                    FO=funcionobjetivo(tipo,llegada_contenedores,la_mejor[0],posiciones_libres,posicion_inicial,vec_aux)
                    if FO<la_mejor[2]:
                        guardar_sol.append([la_mejor[0],vec_aux,FO])
                        la_mejor=[la_mejor[0],vec_aux,FO]
                        j=0
    return la_mejor

import numpy as np
from random import seed
from random import randint
import time
posicion_inicial=[5,0,5]
posicion_mar=[5,0,1]
posicion_tierra=[5,43,2]
llegada_contenedores=[17,100,84,148,117,61,121,82,57,94,56,84,127,150,115,162,96,166,152,36,144,15,82,167,4,56,158,
                      122,127,144,141,136,57,28,2,57,63,165,69,16]
tipo=[2,2,2,1,2,1,1,2,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1,2,2,2,1,1,2,2,1,1,1,1]
file = open('Localización.txt')
l=[]
 
for line in file:
    for word in line.split(): 
        l.append(word) 
 
file.close()

h=0
for i in range(0, len(l)):
    if l[i]=="#x,y,z":
        h=h+1
        if h==3:
            k=i
posiciones_libres=[]
vector_aux=[]
for i in range(k+1,len(l)):
    vector_aux.append(int(l[i]))
    if len(vector_aux)==3:
        posiciones_libres.append(vector_aux)
        vector_aux=[]

movimientos=[]
movimientos.append(0)
espera=[]
espera.append(0)
pos=posicion_inicial
cogida_contenedores=[]
posicion_contenedores=[]
for i in range(0, len(llegada_contenedores)):
    coste=[]
    for j in range(0, len(llegada_contenedores)):
        if tipo[j]==1:
            pos_llegada=posicion_mar
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
        if tipo[j]==2:
            pos_llegada=posicion_tierra
            if llegada_contenedores[j]>espera[0]+movimientos[0]+max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])):
                coste.append(llegada_contenedores[j]-espera[0]-movimientos[0])
            else:
                coste.append(max(abs(pos_llegada[0]-pos[0]),abs(pos_llegada[1]-pos[1])))
                
    for l in range(0, len(llegada_contenedores)):
        k1=[]
        coste_menor=[]
        if not l in cogida_contenedores:
            coste_menor.append(coste[l])
            k1.append(l)
            break

    for j in range(0, len(llegada_contenedores)):
        if coste[j]<coste_menor[0] and not j in cogida_contenedores:
            coste_menor=[]
            k1=[]
            coste_menor.append(coste[j])
            k1.append(j)

    cogida_contenedores.append(k1[0])
    if tipo[k1[0]]==1:
        pos_llegada=posicion_mar
    else:
        pos_llegada=posicion_tierra
    movimientos1=[]
    movimientos1.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos1[0]+(abs(pos_llegada[2]-pos[2]))+max(abs(pos[0]-pos_llegada[0]),abs(pos[1]-pos_llegada[1])))
    if llegada_contenedores[k1[0]]>espera[0]+movimientos[0]:
        movimientos1=[]
        movimientos1.append(movimientos[0])
        espera=[]
        espera.append(llegada_contenedores[k1[0]]-movimientos1[0])
        movimientos=[]
        movimientos.append(espera[0]+movimientos1[0])
    pos=[pos_llegada[0],pos_llegada[1],pos[2]]
    movimientos2=[]
    movimientos2.append(movimientos[0])
    movimientos=[]
    movimientos.append(movimientos2[0]+(abs(pos_llegada[2]-pos[2])))
    
    coste2=[]
    for j in range(0,len(posiciones_libres)):
        coste2.append(max(abs(pos[0]-posiciones_libres[j][0]),abs(pos[1]-posiciones_libres[j][1]))+abs(pos[2]-posiciones_libres[j][2]))

    for l in range(0, len(llegada_contenedores)):
        k2=[]
        coste_minimo=[]
        if not l in posicion_contenedores:
            k2.append(l)
            coste_minimo.append(coste2[l])
            break

    for j in range(0, len(posiciones_libres)):
        if coste2[j]<coste_minimo[0] and not j in posicion_contenedores:
            coste_minimo=[]
            k2=[]
            coste_minimo.append(coste2[j])
            k2.append(j)
    posicion_contenedores.append(k2[0])
    movimientos3=[]
    movimientos3.append(movimientos[0])
    movimientos=[]
    if i ==len(llegada_contenedores)-1:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+abs(pos[2]-posiciones_libres[k2[0]][2]))
    else:
        movimientos.append(movimientos3[0]+max(abs(pos[0]-posiciones_libres[k2[0]][0]),abs(pos[1]-posiciones_libres[k2[0]][1]))+2*abs(pos[2]-posiciones_libres[k2[0]][2]))
    
    pos=[posiciones_libres[k2[0]][0],posiciones_libres[k2[0]][1],pos[2]]

FO=movimientos[0]
la_mejor=[cogida_contenedores,posicion_contenedores,FO]
soluciones_buenas=[]
soluciones_buenas.append(la_mejor)
cogida_contenedores1=[34, 24, 21, 39, 0, 33, 19, 10, 25, 8, 32, 35, 5, 36, 38, 7, 22, 2, 11, 9, 16, 1, 14, 4, 6, 27, 12, 28, 31, 30, 20, 29, 3, 13, 18, 26, 15, 37, 17, 23]
posicion_contenedores1=[49, 29, 44, 103, 99, 18, 31, 36, 114, 1, 45, 8, 104, 0, 56, 67, 108, 71, 110, 19, 32, 47, 23, 55, 96, 91, 62, 119, 78, 21, 58, 107, 82, 6, 9, 16, 52, 72, 92, 50]
FO1=1580
la_mejor=[cogida_contenedores1,posicion_contenedores1,FO1]
soluciones_buenas.append(la_mejor)
print(soluciones_buenas)

#soluciones aleatorias
soluciones_aleatorias=[]
i=0

while i<98:
    j=0
    cogida_contenedores=[]
    while j<len(llegada_contenedores):
        h=randint(0,len(llegada_contenedores)-1)
        if not h in cogida_contenedores:
            cogida_contenedores.append(h)
            j=j+1
    
    k=0
    posicion_contenedores=[]
    while k<len(llegada_contenedores):
        h=randint(0,len(posiciones_libres)-1)
        if not h in posicion_contenedores:
            posicion_contenedores.append(h)
            k=k+1
    rep=0
    for j in range(0, len(soluciones_aleatorias)):
        if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
            rep=1
    if rep==0:
        FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
        soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
        i=i+1
# Genético
start_time = time.time()
seconds=120
looping=True
numerodevecesenelbucle=0
guardar_soluciones=[soluciones_buenas[1]]
numeroiteracionessinhacernada=0
while looping:
    numerodevecesenelbucle=numerodevecesenelbucle+1
    current_time=time.time()
    if current_time-start_time>seconds:
        looping=False
    n1=randint(0,9)
    if n1<=5:
        solucion1=soluciones_buenas[0]
    else:
        solucion1=soluciones_buenas[1]
    n2=randint(0,len(soluciones_aleatorias)-1)
    solucion2=soluciones_aleatorias[n2]
    punto_corte=randint(int(len(solucion1[0])/4),int(3*len(solucion1[0])/4))
    vector_aux_hijo_1_1=[]
    vector_aux_hijo_1_2=[]
    for i in range(0, len(cogida_contenedores)):
        if i<=punto_corte:
            #El primer hijo coge las primeras partes de la primera solución y el segundo hijo a la inversa
            vector_aux_hijo_1_1.append(solucion1[0][i])
            vector_aux_hijo_1_2.append(solucion1[1][i])
        else:
            vector_aux_hijo_1_1.append(solucion2[0][i])
            vector_aux_hijo_1_2.append(solucion2[1][i])
    falta11=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in vector_aux_hijo_1_1 and not i in falta11:
            falta11.append(i)
    numeros11=[]
    i=0
    while i <len(falta11):
        n1=randint(0,len(cogida_contenedores)-1)
        if not n1 in numeros11:
            numeros11.append(n1)
            i=i+1
    
    vector_hijo11=[]
    h1=0
    i=0
    while len(vector_hijo11) <len(cogida_contenedores):
        if not i in numeros11 and not vector_aux_hijo_1_1[i] in vector_hijo11:
            vector_hijo11.append(vector_aux_hijo_1_1[i])
        elif i in numeros11 and h1<len(falta11):
            vector_hijo11.append(falta11[h1])
            h1=h1+1
        elif i in numeros11 or vector_aux_hijo_1_1[i] in vector_hijo11:
            for j in range(0,len(cogida_contenedores)):
                if not j in falta11 and not j in vector_hijo11:
                    vector_hijo11.append(j)
        i=i+1
        if i==len(cogida_contenedores):
            i=0
    numeros12=[]
    for i in range(0,len(cogida_contenedores)):
        for j in range(0,i+1):
            if i!=j and vector_aux_hijo_1_2[i]==vector_aux_hijo_1_2[j] and not j in numeros12:
                numeros12.append(j)
    vector_hijo12=[]
    for i in range(0,len(cogida_contenedores)):
        if not i in numeros12:
            vector_hijo12.append(vector_aux_hijo_1_2[i])
        elif i in numeros12:
            salir_bucle1=True
            x=randint(0,len(posiciones_libres)-1)
            while salir_bucle1:
                if not x in vector_hijo12 and not x in vector_aux_hijo_1_2:
                    vector_hijo12.append(x)
                    salir_bucle1=False
                x=randint(0,len(posiciones_libres)-1)
    rephijo1=0
    for i in range(0,len(soluciones_aleatorias)):
        if vector_hijo11==soluciones_aleatorias[i][0] and vector_hijo12==soluciones_aleatorias[i][1]:
            rephijo1=1
    FO1=funcionobjetivo(tipo,llegada_contenedores,vector_hijo11,posiciones_libres,posicion_inicial,vector_hijo12)
    hijo=[vector_hijo11,vector_hijo12,FO1]
    if rephijo1==0:
        maximo_buenas=soluciones_buenas[0][2]
        k_buenas=0
        for i in range(0,len(soluciones_buenas)):
            if soluciones_buenas[i][2]>maximo_buenas:
                maximo_buenas=soluciones_buenas[i][2]
                k_buenas=i
        if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
            soluciones_buenas[k_buenas]=hijo
            guardar_soluciones.append(hijo)
            numeroiteracionessinhacernada=0
        maximo_aleatorias=soluciones_aleatorias[0][2]
        k_aleatorias=0
        for i in range(0,len(soluciones_aleatorias)):
            if soluciones_aleatorias[i][2]>maximo_aleatorias:
                maximo_aleatorias=soluciones_aleatorias[i][2]
                k_aleatorias=i
        if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
            soluciones_aleatorias[k_aleatorias]=hijo
            numeroiteracionessinhacernada=0
        n_mutacion=randint(0,1)
        if n_mutacion==1:
            n1_cambio=randint(0,len(cogida_contenedores)-1)
            n2_cambio=randint(0,len(cogida_contenedores)-1)
            while n1_cambio==n2_cambio:
                n2_cambio=randint(0,len(cogida_contenedores)-1)
            vector_cambio=hijo
            vector_aux1=[]
            vector_aux2=[]
            hijo=[]
            for i in range(0,len(cogida_contenedores)):
                if i==n1_cambio:
                    vector_aux1.append(vector_cambio[0][n2_cambio])
                    vector_aux2.append(vector_cambio[1][n2_cambio])
                elif i==n2_cambio:
                    vector_aux1.append(vector_cambio[0][n1_cambio])
                    vector_aux2.append(vector_cambio[1][n1_cambio])
                else:
                    vector_aux1.append(vector_cambio[0][i])
                    vector_aux2.append(vector_cambio[1][i])
            FO=funcionobjetivo(tipo,llegada_contenedores,vector_aux1,posiciones_libres,posicion_inicial,vector_aux2)
            hijo=[vector_aux1,vector_aux2,FO]
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
        random_bl=randint(0,99)
        if random_bl==0:
            hijo=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,hijo)
            if not hijo in soluciones_buenas and not hijo in soluciones_aleatorias:
                maximo_buenas=soluciones_buenas[0][2]
                k_buenas=0
                for i in range(0,len(soluciones_buenas)):
                    if soluciones_buenas[i][2]>maximo_buenas:
                        maximo_buenas=soluciones_buenas[i][2]
                        k_buenas=i
                if hijo[2]<maximo_buenas and not hijo in soluciones_buenas:
                    soluciones_buenas[k_buenas]=hijo
                    guardar_soluciones.append(hijo)
                    numeroiteracionessinhacernada=0
                maximo_aleatorias=soluciones_aleatorias[0][2]
                k_aleatorias=0
                for i in range(0,len(soluciones_aleatorias)):
                    if soluciones_aleatorias[i][2]>maximo_aleatorias:
                        maximo_aleatorias=soluciones_aleatorias[i][2]
                        k_aleatorias=i
                if hijo[2]<maximo_aleatorias and not hijo in soluciones_buenas:
                    soluciones_aleatorias[k_aleatorias]=hijo
                    numeroiteracionessinhacernada=0
    if numeroiteracionessinhacernada==100:
        soluciones_aleatorias=[]
        i=0
        while i<98:
            j=0
            cogida_contenedores=[]
            while j<len(llegada_contenedores):
                h=randint(0,len(llegada_contenedores)-1)
                if not h in cogida_contenedores:
                    cogida_contenedores.append(h)
                    j=j+1

            k=0
            posicion_contenedores=[]
            while k<len(llegada_contenedores):
                h=randint(0,len(posiciones_libres)-1)
                if not h in posicion_contenedores:
                    posicion_contenedores.append(h)
                    k=k+1
            rep=0
            for j in range(0, len(soluciones_aleatorias)):
                if cogida_contenedores==soluciones_aleatorias[j][0] and posicion_contenedores==soluciones_aleatorias[j][1]:
                    rep=1
            if rep==0:
                FO=funcionobjetivo(tipo,llegada_contenedores,cogida_contenedores,posiciones_libres,posicion_inicial,posicion_contenedores)
                soluciones_aleatorias.append([cogida_contenedores,posicion_contenedores,FO])
                i=i+1
    numeroiteracionessinhacernada=numeroiteracionessinhacernada+1
# Búsqueda local
print(numerodevecesenelbucle)
k_mas_pequeña=0
la_mas_pequeña=guardar_soluciones[0][2]
for i in range(0, len(guardar_soluciones)):
    if guardar_soluciones[i][2]<la_mas_pequeña:
        k_mas_pequeña=i
        la_mas_pequeña=guardar_soluciones[i][2]
la_mejor=guardar_soluciones[k_mas_pequeña]

la_mejor=BusquedaLocal(cogida_contenedores,tipo,llegada_contenedores,posiciones_libres,posicion_inicial,la_mejor)
print(la_mejor)


# In[ ]:


Heurística1=[[2, 0, 5, 7, 1, 3, 4, 6], [8, 9, 5, 15, 12, 13, 0, 10], 275]
Heurística2=[[2, 7, 0, 6, 1, 5, 4, 3],[8, 9, 5, 12, 13, 15, 0, 10],333]
iteraciones en el genético=106596
Depués del genético=[[2, 0, 5, 7, 1, 3, 4, 6], [8, 9, 5, 15, 12, 13, 0, 10], 275]
Después del genético con la búsqueda local=[[2, 0, 5, 7, 1, 3, 4, 6], [8, 9, 5, 11, 12, 13, 0, 10], 273]
Añadiendo una búsqueda local dentro del genético (1%) a parte de aplicar la búsqueda local al final=[[2, 0, 5, 7, 1, 3, 4, 6], [8, 9, 5, 11, 12, 13, 0, 10], 273]

 

Heurística1=[[5, 6, 2, 7, 1, 0, 3, 4],[8, 0, 10, 2, 12, 11, 13, 9],264]
Heurística2=[[5, 6, 2, 7, 1, 0, 3, 4],[8, 0, 10, 2, 12, 11, 13, 9],264]
iteraciones en el genético=114924
Depués del genético=[[5, 6, 7, 2, 1, 0, 4, 3], [3, 12, 2, 10, 0, 5, 8, 13], 235]
Después del genético con la búsqueda local=[[5, 6, 7, 2, 1, 0, 4, 3], [1, 12, 2, 10, 0, 5, 8, 13], 233]
Añadiendo una búsqueda local dentro del genético (1%) a parte de aplicar la búsqueda local al final=[[5, 6, 2, 7, 1, 0, 3, 4], [4, 2, 10, 12, 0, 5, 8, 13], 233]

 

Heurística1=[[24, 21, 33, 19, 5, 10, 9, 6, 3, 11, 13, 14, 15, 17, 18, 22, 26, 28, 32, 36, 37, 38, 39, 0, 1, 2, 4, 7, 8, 12, 16, 20, 23, 25, 27, 29, 30, 31, 34, 35], [29, 44, 103, 18, 31, 36, 45, 104, 0, 56, 108, 110, 19, 23, 96, 119, 82, 6, 9, 16, 52, 72, 92, 49, 99, 114, 1, 8, 67, 71, 32, 47, 55, 91, 62, 78, 21, 58, 107, 50], 879]
Heurística2=[[34, 24, 21, 39, 0, 33, 19, 10, 25, 8, 32, 35, 5, 36, 38, 7, 22, 2, 11, 9, 16, 1, 14, 4, 6, 27, 12, 28, 31, 30, 20, 29, 3, 13, 18, 26, 15, 37, 17, 23],[49, 29, 44, 103, 99, 18, 31, 36, 114, 1, 45, 8, 104, 0, 56, 67, 108, 71, 110, 19, 32, 47, 23, 55, 96, 91, 62, 119, 78, 21, 58, 107, 82, 6, 9, 16, 52, 72, 92, 50],1580]
iteraciones en el genético=78412
Depués del genético=[[24, 21, 33, 19, 5, 10, 9, 6, 3, 11, 13, 14, 15, 17, 18, 22, 26, 28, 32, 36, 37, 38, 39, 0, 1, 2, 4, 7, 8, 12, 16, 20, 23, 25, 27, 29, 30, 31, 34, 35], [29, 44, 103, 18, 31, 36, 45, 104, 0, 56, 108, 110, 19, 23, 96, 119, 82, 6, 9, 16, 52, 72, 92, 49, 99, 114, 1, 8, 67, 71, 32, 47, 55, 91, 62, 78, 21, 58, 107, 50], 879]
Después del genético con la búsqueda local=[[24, 21, 33, 19, 5, 10, 9, 6, 3, 11, 13, 14, 15, 17, 18, 22, 26, 28, 32, 36, 37, 39, 38, 0, 1, 2, 4, 7, 8, 12, 16, 20, 23, 25, 27, 29, 30, 31, 34, 35], [29, 44, 103, 18, 31, 36, 45, 104, 0, 56, 108, 110, 19, 23, 96, 119, 82, 6, 9, 16, 52, 92, 14, 49, 99, 114, 1, 8, 67, 71, 32, 47, 55, 91, 62, 78, 21, 58, 107, 50], 873]
Añadiendo una búsqueda local dentro del genético (1%) a parte de aplicar la búsqueda local al final=[[24, 21, 33, 19, 5, 10, 9, 6, 3, 11, 13, 14, 15, 17, 18, 22, 26, 28, 32, 36, 37, 39, 38, 0, 1, 2, 4, 7, 8, 12, 16, 20, 23, 25, 27, 29, 30, 31, 34, 35], [29, 44, 103, 18, 31, 36, 45, 104, 0, 56, 108, 110, 19, 23, 96, 119, 82, 6, 9, 16, 52, 92, 14, 49, 99, 114, 1, 8, 67, 71, 32, 47, 55, 91, 62, 78, 21, 58, 107, 50], 873]


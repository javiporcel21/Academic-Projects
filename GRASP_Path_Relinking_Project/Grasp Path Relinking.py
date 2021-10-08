#!/usr/bin/env python
# coding: utf-8

# In[5]:


def calcular_valores(vector_calculo,m,lista,n):
    la_mejor=vector_calculo
    best_i=la_mejor[0]
    Contribution=[]
    value=0
    for i in range(0,n):
        Contribution.append(lista[i][best_i])
    for j in range(1,m):
        best_i=la_mejor[j]
        largest=Contribution[best_i]
        value=value+largest
        for i in range(0,n):
            Contribution[i]=Contribution[i]+lista[i][best_i]
        Contribution[best_i]=0
    return value

def good(n,Contribution,best_i,sol):
    max = 0
    min = 100000000000
    for i in range(0,n):
        if Contribution[i] > max:
            max = Contribution[i]
        if Contribution[i] > 0 and Contribution[i] < min:
            min = Contribution[i]
    
#     'CREATE RCL
    RCL=[]
    threshold = min + alpha * (max - min)
    n_elements = 0
    for i in range(0,n):
        if Contribution[i] >= threshold:
            n_elements = n_elements + 1
            RCL.append(i)

    
#     'SELECT ELEMENT AT RANDOM
    in_sol=True
    ind = randint(0,len(RCL)-1)
    while in_sol:
        if RCL[ind] in sol:
            ind = randint(0,len(RCL)-1)
        else:
            in_sol=False
    best_i = RCL[ind]
    good = Contribution[best_i]
    return [good,best_i]

def LocalSearch(n,m,sol,value,lista):
    Improve=1
    while Improve==1:
        Improve=0
        for i in range(0,m):
            try_out=sol[i]
            out_value=0
            for j in range(0,m):
                element=sol[j]
                out_value=out_value+lista[try_out][element]
            Move=0
            try_in=0
            while Move==0 and try_in<n:
                if not try_in in sol:
                    in_value=in_val(sol,try_in,try_out,m,lista)
                    if in_value>out_value:
                        sol[i]=try_in
                        value=value-out_value+in_value
                        Move=1
                        Improve=1
                try_in=try_in+1
    return [value,sol]

def in_val(sol,try_in,try_out,m,lista):
    in_val=0
    if not try_in in sol:
        for j in range(0,m):
            element=sol[j]
            if element != try_out:
                in_val=in_val+lista[try_in][element]
    return in_val

import numpy as np
import pandas as pd
from random import seed
from random import randint
import time

file = open('MDP grande.txt')

lista=[]
for line in file:
    l=[]
    for word in line.split(): 
        l.append(int(word)) 
    lista.append(l)
file.close()

alpha=0.8
b = 4
n = 500
m = 25
Best = 0
soluciones=[]
solvalues=[]
impsolvalues=[]
Bul=True
seconds1=30
start_time1=time.time()
iters=0
while Bul:
    current_time1=time.time()
    if current_time1-start_time1>seconds1:
        Bul=False
    sol=[]
    value=0
    best_i=randint(0,n-1)
    sol.append(best_i)
    Contribution=[]
    for i in range(0,n):
        Contribution.append(lista[i][best_i])
    for j in range(1,m):
        [largest,best_i]=good(n,Contribution,best_i,sol)
        sol.append(best_i)
        value=value+largest
        for i in range(0,n):
            Contribution[i]=Contribution[i]+lista[i][best_i]
        Contribution[best_i]=0
        
    solvalues.append(value)
    [value,sol]=LocalSearch(n,m,sol,value,lista)
    impsolvalues.append(value)
    if Best<value:
        Best=value
    soluciones.append(sol)
    iters=iters+1
    current_time1=time.time()
    if current_time1-start_time1>seconds1:
        Bul=False
print("La mejor solución del Grasp:",Best,". Después de ",iters," iteraciones, en ",int(current_time1-start_time1)," segundos.")

start_time2=time.time()
k=[]
mejores_soluciones=[]
for i in range(0,8):
    valor=0
    for j in range(0,iters):
        if impsolvalues[j]>valor and not soluciones[j] in mejores_soluciones:
            valor=impsolvalues[j]
            v=j
    mejores_soluciones.append(soluciones[v])
    k.append(impsolvalues[v])

print("Y la mejor solución es:", mejores_soluciones[0])
#Path Relinking
soluciones_PR=[]
valores_PR=[]
soluciones_PR.append(mejores_soluciones[0])
valores_PR.append(k[0])
for i in range(0,len(mejores_soluciones)-1):
    vector1=mejores_soluciones[i]
    valor=[]
    valor.append(k[i])
    for j in range(i+1,len(mejores_soluciones)):
        vector2=mejores_soluciones[j]
        for p in range(0,m):
            try_out=vector1[p]
            valores=[]
            if vector1!=vector2:
                for q in range(0,m):
                    if not vector2[q] in vector1:
                        try_in=vector2[q]
                        vector_calculo=[]
                        for w8 in range(0,m):
                            if w8!=q:
                                vector_calculo.append(vector1[w8])
                            else:
                                vector_calculo.append(vector2[w8])
                        in_value=calcular_valores(vector_calculo,m,lista,n)
                        valores.append(in_value)
                    if vector2[q] in vector1:
                        valores.append(0)
                maximo=[]
                maximo.append(0)
                posicion=-100
                for longitud in range(0,len(valores)):
                    if valores[longitud]>maximo[0]:
                        maximo=[]
                        maximo.append(valores[longitud])
                        posicion=longitud
                if posicion>=0:
                    vector1_aux=[]
                    for i1 in range(0,len(vector1)):
                        vector1_aux.append(vector1[i1])
                    vector1=[]
                    for i2 in range(0,len(vector1_aux)):
                        if i2!=posicion:
                            vector1.append(vector1_aux[i2])
                        else:
                            vector1.append(vector2[i2])
                    valor=[]
                    valor.append(valores[posicion])
                    if not vector1 in soluciones_PR:
                        soluciones_PR.append(vector1)
                        valores_PR.append(valor[0])
                    randomizar_bl=randint(0,9)
                    if randomizar_bl<1:
                        valuebl=[]
                        [valuebl1,vector1bl]=LocalSearch(n,m,vector1,valor[0],lista)
                        soluciones_PR.append(vector1bl)
                        valuebl.append(valuebl1)
                        valores_PR.append(valuebl[0])

mejor=0
for i in range(0,len(valores_PR)):
    if valores_PR[i]>mejor:
        mejor=valores_PR[i]
        posiciones=i
current_time2=time.time()
print("El mejor valor es:", mejor,". Obtenido en ", int(current_time2-start_time1), " segundos.")
print("Y la solución final es:",soluciones_PR[posiciones])


# In[ ]:





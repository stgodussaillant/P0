# -*- coding: utf-8 -*-

import numpy as np
from numpy import double
from time import perf_counter

def Laplaciana(N, t=double):            #Laplaciana llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)

N=[4,7,10,20,50,70,85,100,150,200,250,300,
   400,500,750,800,950,1000,1250,1400,1500,1650,
   1850,1950,2000,2400,3300,4600,5000,7500,10000]         #Tamaño de las matrices
tamano=[]
tiempo_ensam=[]
tiempo_sol=[]
p=0
while p<10:
    i=0
    while i<len(N):
        t1=perf_counter()
        A=Laplaciana(N[i])
        B=Laplaciana(N[i])
        t2=perf_counter()
        
        dt_ensamblado = t2-t1
        
        t3=perf_counter()
        C = A@B
        t4 =perf_counter()
        
        dt_solucion=t4-t3
        
        print(f"Tiempo de ensamblado matriz A: {dt_ensamblado} s")
        print(f"Tiempo de solucion: {dt_solucion} s")
        print(f"Tamaño de matriz: {N[i]}")
        print()
        
        tamano.append(N[i])
        tiempo_ensam.append(dt_ensamblado)
        tiempo_sol.append(dt_solucion)
        i+=1
    p+=1
    
f = open("Caso_llena_double.txt", "w")
e = 0
f.write("Tiempo ensamblado [s]   Tiempo solucion [s]   Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_ensam[e]}   {tiempo_sol[e]}   {tamano[e]} \n")
    e+=1
f.close()


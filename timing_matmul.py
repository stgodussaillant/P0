# -*- coding: utf-8 -*-
from numpy import zeros
from time import perf_counter

i = 0
tiempo = []
memoria = []
tamano = []
while i < 10:
    N=[3,7,10,20,50,70,85,100,150,200,250,300,
       400,500,750,800,950,1000,1250,1400,1500,1650,
       1850,1950,2000,2400,3300,4600,5000,7500,10000]         #Tamaño de las matrices
    n = 0
    while len(N)>n:
        A = zeros((N[n], N[n]))+1
        B = zeros((N[n], N[n]))+2
        
        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()   
        mem = A.nbytes + B.nbytes + C.nbytes
        dt = t2-t1
        if mem >= 5000000000:               #Si la memoria es mayor a 5GB se termina el ciclo
            break
        
        tiempo.append(dt)
        memoria.append(mem)
        tamano.append(N[n])
        
        print (f"dt = {dt} s")
        print (f"mem = {mem} bytes")
        print (f"N = {N[n]}")
        print ()
        n+=1
    i+=1

f = open("Rendimiento.txt", "w")
e = 0
f.write("Tiempo[s]   Memoria[bytes]    Tamaño \n")
while e < len(tiempo):
    f.write(f"{tiempo[e]}   {memoria[e]}   {tamano[e]} \n")
    e+=1
f.close()



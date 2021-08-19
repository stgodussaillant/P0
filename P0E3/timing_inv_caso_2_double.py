# -*- coding: utf-8 -*-

from time import perf_counter
from scipy.linalg import inv
from numpy import double
from Laplaciana import laplaciana              #Se llama a la funcion desde otro archivo


N=[1,7,10,20,50,70,85,100,150,200,250,300,
   400,500,750,800,950,1000,1250,1400,1500,1650,
   1850,1950,2000,2400,3300,4600,5000,7500,10000]         #Tamaño de las matrices

tamano = []
memoria = []
tiempo_ensam = []
tiempo_inv = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        
        t1 = perf_counter() 
        A = laplaciana(N[p], dtype=double)
        t2 = perf_counter()

        Am1 = inv(A, overwrite_a=False)
        t3 = perf_counter()

        dt_ensamblaje = t2-t1       #Tiempo de armado de laplaciana
        dt_inversion = t3-t2        #tiempo que demora en invertir laplaciana

        bytes_total= A.nbytes+Am1.nbytes
        
        tamano.append(N[p])
        memoria.append(bytes_total)
        tiempo_ensam.append(dt_ensamblaje)
        tiempo_inv.append(dt_inversion)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Uso memoria: {bytes_total} bytes")
        print (f"Tiempo inversion: {dt_inversion} s")
        print ()
        p+=1
    i+=1

f = open("Caso_2_double.txt", "w")
e = 0
f.write("Tiempo inversion[s]   Memoria[bytes]    Tamaño \n")
while e < len(memoria):
    f.write(f"{tiempo_inv[e]}   {memoria[e]}   {tamano[e]} \n")
    e+=1
f.close()




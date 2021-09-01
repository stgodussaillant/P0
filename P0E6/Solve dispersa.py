# -*- coding: utf-8 -*-

import scipy.sparse as sp
import scipy.sparse.linalg as lin
from Laplaciana import laplaciana_dispersa
from time import perf_counter
from numpy import double, ones

N=[10,20,50,75,100,300,500,800,1000,3000,5000,7500,10000,14000,15000,
   20000,50000,75000,100000,130000,150000,250000,500000,600000,750000,
   1000000,2000000,4000000,5500000,6250000,7500000]  #Tamaño de las matrices

tamano=[]
tiempo_ensam=[]
tiempo_sol=[]
p=0
while p<10:
    i=0
    while i<len(N):
        
        t1=perf_counter()
        
        A=laplaciana_dispersa(N[i],double)
        b=ones(N[i],dtype=double)
        
        Acsr=sp.csr_matrix(A)
        
        t2=perf_counter()
        
        x=lin.spsolve(A,b)
        
        t3=perf_counter()
        
        dt_ensam=t2-t1
        dt_sol=t3-t2
        
        tamano.append(N[i])
        tiempo_ensam.append(dt_ensam)
        tiempo_sol.append(dt_sol)
        
        print(f"Tiempo ensamblaje: {dt_ensam} s")
        print(f"Tiempo solucion: {dt_sol} s")
        print(f"Tamaño: {N[i]}")
        print()
        
        i+=1
    p+=1
    
f = open("Solve_dispersa_double.txt", "w")
e = 0
f.write("Tiempo ensamblado [s]   Tiempo solucion [s]   Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_ensam[e]}   {tiempo_sol[e]}   {tamano[e]} \n")
    e+=1
f.close()


# -*- coding: utf-8 -*-

from scipy.linalg import solve
from Laplaciana import laplaciana_llena
from time import perf_counter
from numpy import double, ones

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
        
        A=laplaciana_llena(N[i],double)
        b=ones(N[i],dtype=double)
        
        t2=perf_counter()
        
        x=solve(A,b)
        
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
    
f = open("Solve_llena_double.txt", "w")
e = 0
f.write("Tiempo ensamblado [s]   Tiempo solucion [s]   Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_ensam[e]}   {tiempo_sol[e]}   {tamano[e]} \n")
    e+=1
f.close()


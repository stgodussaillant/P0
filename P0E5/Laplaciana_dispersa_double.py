# -*- coding: utf-8 -*-

from numpy import double
import scipy.sparse as sparse
from time import perf_counter

def Laplaciana(N, t=double):                                    #Laplaciana dispersa
    e = sparse.eye(N, dtype=t)-sparse.eye(N,N,1,dtype=t)
    return e+e.T

N=[10,20,50,75,100,300,500,800,1000,5000,10000,14000,15000,
   20000,50000,75000,100000,130000,150000,250000,500000,600000,750000,
   1000000,2000000,4000000,5500000,6250000,7500000,9000000,10000000]  #Tamaño de las matrices

tamano=[]
tiempo_ensam=[]
tiempo_sol=[]
p=0
while p<10:
    i=0
    while i<len(N):
        t1=perf_counter()
        A = Laplaciana(N[i])
        Acsr = sparse.csr_matrix(A)
        B=Laplaciana(N[i])
        Bcsr = sparse.csr_matrix(B)
        t2=perf_counter()
        
        dt_ensamblado = t2-t1
        
        t3=perf_counter()
        C = Acsr@Bcsr
        t4 =perf_counter()
        
        dt_solucion=t4-t3
        
        print(f"Tiempo de ensamblado matriz A: {dt_ensamblado} [s]")
        print(f"Tiempo de solucion: {dt_solucion} [s]")
        print(f"Tamaño de matriz: {N[i]}")
        print()
        
        tamano.append(N[i])
        tiempo_ensam.append(dt_ensamblado)
        tiempo_sol.append(dt_solucion)
        i+=1
    p+=1
    
f = open("Caso_dispersa_double.txt", "w")
e = 0
f.write("Tiempo ensamblado [s]   Tiempo solucion [s]   Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_ensam[e]}   {tiempo_sol[e]}   {tamano[e]} \n")
    e+=1
f.close()




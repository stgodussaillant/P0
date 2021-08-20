# -*- coding: utf-8 -*-

from time import perf_counter
from scipy.linalg import eigh
from numpy import double
from Laplaciana import laplaciana              #Se llama a la funcion desde otro archivo

def Caso1(A):
    w,v = eigh(A)
    return w,v

def Caso2(A, turbo, overwrite_a):
    w,v = eigh(A, turbo=turbo, overwrite_a=overwrite_a)
    return w,v

N=[3,7,10,20,50,70,85,100,150,200,250,300,
   400,500,750,800,950,1000,1250,1300,1400,1500,
   1650,1850,1950,2000,2100,2400,3300,4600,5000]         #Tamaño de las matrices

"""CASO 1"""

print ("CASO 1")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso1(A)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_1_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 2"""

print ("CASO 2.1")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="ev", overwrite_a=False)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_2.1_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

print ("CASO 2.2")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="ev", overwrite_a=True)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_2.2_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 3"""

print ("CASO 3.1")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evd", overwrite_a=False)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_3.1_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

print ("CASO 3.2")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evd", overwrite_a=True)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_3.2_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 4"""

print ("CASO 4.1")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evr", overwrite_a=False)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_4.1_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

print ("CASO 4.2")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evr", overwrite_a=True)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_4.2_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()


"""CASO 5"""

print ("CASO 5.1")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evx", overwrite_a=False)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_5.1_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()

print ("CASO 5.2")
tamano = []
tiempo_vvp = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        x = Caso2(A, turbo="evx", overwrite_a=True)
        t2 = perf_counter()
        
        dt_vvp = t2-t1        #tiempo que demora en encontrar valores y vectores propios

        tamano.append(N[p])
        tiempo_vvp.append(dt_vvp)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo eigh: {dt_vvp} s")
        print ()
        p+=1
    i+=1

f = open("Caso_5.2_eigh_double.txt", "w")
e = 0
f.write("Tiempo eigh[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_vvp[e]}   {tamano[e]} \n")
    e+=1
f.close()



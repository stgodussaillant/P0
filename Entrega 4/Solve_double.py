# -*- coding: utf-8 -*-

from time import perf_counter
from scipy.linalg import inv, solve
from numpy import double
from Laplaciana import laplaciana              #Se llama a la funcion desde otro archivo
import numpy as np

def solve1(Am1, b):
    x = Am1*b
    return x

def solve2(A, b):
    x = solve(A, b)
    return x

def solve3(A, b, assume_a):
    x = solve(A, b, assume_a=assume_a)
    return x

def solve4(A, b, overwrite_a):
    x = solve(A, b, overwrite_a=True)
    return x

def solve5(A, b, overwrite_b):
    x = solve(A, b, overwrite_b=True)
    return x

def solve6(A, b, overwrite_a, overwrite_b):
    x = solve(A, b, overwrite_a=True, overwrite_b=True)
    return x

N=[3,7,10,20,50,70,85,100,150,200,250,300,
   400,500,750,800,950,1000,1250,1400,1500,1650,
   1850,1950,2000,2400,3300,4600,5000,7500,10000]         #Tamaño de las matrices

"""CASO 1"""

print ("CASO 1")
tamano = []
tiempo_solve = []
tiempo_inv = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        t1 = perf_counter() 
        Am1 = inv(A)
        t2 = perf_counter()
        
        vect1=np.ones(N[p], double)
        
        t3=perf_counter()
        x = solve1(Am1, vect1)
        t4=perf_counter()
        
        dt_inversion = t2-t1        #tiempo que demora en invertir laplaciana
        dt_solver = t4-t3           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
        tiempo_inv.append(dt_inversion)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print (f"Tiempo inversion: {dt_inversion} s")
        print ()
        p+=1
    i+=1

f = open("Caso_1_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()


"""CASO 2"""

print ("CASO 2")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        
        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve2(A, vect1)
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_2_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()


"""CASO 3"""

print ("CASO 3")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)

        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve3(A, vect1, assume_a="pos")
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_3_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 4"""

print ("CASO 4")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve3(A, vect1, assume_a="sym")
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_4_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 5"""

print ("CASO 5")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve4(A, vect1, overwrite_a=True)
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_5_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 6"""

print ("CASO 6")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)        
        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve5(A, vect1, overwrite_b=True)
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_6_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()

"""CASO 7"""

print ("CASO 7")
tamano = []
tiempo_solve = []
i = 0
while i < 10:
    p = 0
    while p<len(N):
        A = laplaciana(N[p], double)
        vect1=np.ones(N[p], double)
        
        t1=perf_counter()
        x = solve6(A, vect1, overwrite_a=True, overwrite_b=True)
        t2=perf_counter()
        
        dt_solver = t2-t1           #tiempo que demora el solve

        tamano.append(N[p])
        tiempo_solve.append(dt_solver)
    
        print (f"Tamaño matriz: {N[p]}")
        print (f"Tiempo solve: {dt_solver} s")
        print ()
        p+=1
    i+=1

f = open("Caso_7_solve_double.txt", "w")
e = 0
f.write("Tiempo solve[s]    Tamaño \n")
while e < len(tamano):
    f.write(f"{tiempo_solve[e]}   {tamano[e]} \n")
    e+=1
f.close()


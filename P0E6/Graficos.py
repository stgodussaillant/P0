# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

tipo=input("Ingrese el tipo de problema a solucionar (solve o inv): ")
archivo = (input("Ingrese el tipo de matriz (llena o dispersa): "))
if tipo=="solve":
    if archivo == "llena":
        f = open("Solve_llena_double.txt", "r")
    
        datos = f.read()
        datos = datos.split("\n")
        datos.pop(0)
        datos.pop(-1)
        q=0
        tiempo_ensam = []
        tiempo_sol = []
        tamano = []
        while q<len(datos):
            fila = datos[q]
            fila = fila.split("   ")
            tiempo_ensam.append(float(fila[0]))
            tiempo_sol.append(float(fila[1]))
            tamano.append(float(fila[2]))
            q+=1
        
        N = len(datos)/10
        N = int(N)
        
    if archivo == "dispersa":
        f = open("Solve_dispersa_double.txt", "r")
    
        datos = f.read()
        datos = datos.split("\n")
        datos.pop(0)
        datos.pop(-1)
        q=0
        tiempo_ensam = []
        tiempo_sol = []
        tamano = []
        while q<len(datos):
            fila = datos[q]
            fila = fila.split("   ")
            tiempo_ensam.append(float(fila[0]))
            tiempo_sol.append(float(fila[1]))
            tamano.append(float(fila[2]))
            q+=1
        
        N = len(datos)/10
        N = int(N)
        
if tipo=="inv":
    if archivo == "llena":
        f = open("Inv_llena_double.txt", "r")
    
        datos = f.read()
        datos = datos.split("\n")
        datos.pop(0)
        datos.pop(-1)
        q=0
        tiempo_ensam = []
        tiempo_sol = []
        tamano = []
        while q<len(datos):
            fila = datos[q]
            fila = fila.split("   ")
            tiempo_ensam.append(float(fila[0]))
            tiempo_sol.append(float(fila[1]))
            tamano.append(float(fila[2]))
            q+=1
        
        N = len(datos)/10
        N = int(N)
        
    if archivo == "dispersa":
        f = open("Inv_dispersa_double.txt", "r")
    
        datos = f.read()
        datos = datos.split("\n")
        datos.pop(0)
        datos.pop(-1)
        q=0
        tiempo_ensam = []
        tiempo_sol = []
        tamano = []
        while q<len(datos):
            fila = datos[q]
            fila = fila.split("   ")
            tiempo_ensam.append(float(fila[0]))
            tiempo_sol.append(float(fila[1]))
            tamano.append(float(fila[2]))
            q+=1
        
        N = len(datos)/10
        N = int(N)

x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
x11 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000","50000","100000","200000","500000","1000000","2000000","5000000","10000000"]
y1 = [ "0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
y12 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min"]
y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
tiempo12 = [0.1/1000,1/1000,10/1000,0.1,1,10,60]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamano1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
tamano11 = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000,10000000]

"""Grafico arriba"""
plt.subplot(2,1,1)

r=0
t=0
while r < 10:
    while t < len(datos):
        plt.loglog(tamano[t:t+31],tiempo_ensam[t:t+31], "o-",alpha=0.2,ms=3,color="k")
        t+=N
    r+=1

plt.hlines(y=max(tiempo_ensam), xmin=min(tamano), xmax=max(tamano), linestyle="--", color="blue", label="Constante")

"""O(N)"""

m=max(tiempo_ensam)
n=tiempo1[0]
tiempo=[n,m]
tamano22=[tamano[0],tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="orange", label="O(N)")

"""O(N2)"""

m=max(tiempo_ensam)
n=tiempo1[0]
tiempo=[n**2,m]
tamano22=[tamano[0]**2,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="green", label="O(N^2)")

"""O(N3)"""

m=max(tiempo_ensam)
n=tiempo1[0]
tiempo=[n**3,m]
tamano22=[tamano[0]**3,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="red", label="O(N^3)")

"""O(N4)"""

m=max(tiempo_ensam)
n=tiempo1[0]
tiempo=[n**4,m]
tamano22=[tamano[0]**4,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="purple", label="O(N^4)")

plt.xticks(tamano1, ["","","","","","","","","",""])

if tipo=="solve":
    if archivo == "dispersa":
        plt.title(f"Rendimiento Laplaciana {tipo} {archivo}")
        plt.yticks(tiempo1, y1)
        plt.ylim(bottom=tiempo1[0], top=tiempo1[-1])
    if archivo == "llena":
        plt.xlim(right=20000)
        plt.yticks(tiempo1, y1)
        plt.ylim(bottom=min(tiempo_ensam), top=tiempo1[-1])
        plt.title(f"Rendimiento Laplaciana {tipo} {archivo}")

if tipo=="inv":
    plt.xlim(right=20000)
    plt.yticks(tiempo1, y1)
    plt.ylim(bottom=min(tiempo_ensam), top=tiempo1[-1])
    plt.title(f"Rendimiento Laplaciana {tipo} {archivo}")

plt.ylabel("Tiempo de ensamblaje")


"""Grafico abajo"""
plt.subplot(2,1,2)

r=0
t=0
while r < 10:
    while t < len(datos):
        plt.loglog(tamano[t:t+31],tiempo_sol[t:t+31], "o-",alpha=0.2,ms=3,color="k")
        t+=N
    r+=1

plt.hlines(y=max(tiempo_sol), xmin=min(tamano), xmax=max(tamano), linestyle="--", color="blue", label="Constante")

"""O(N)"""

m=max(tiempo_sol)
n=tiempo1[0]
tiempo=[n,m]
tamano22=[tamano[0],tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="orange", label="O(N)")

"""O(N2)"""

m=max(tiempo_sol)
n=tiempo1[0]
tiempo=[n**2,m]
tamano22=[tamano[0]**2,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="green", label="O(N^2)")

"""O(N3)"""

m=max(tiempo_sol)
n=tiempo1[0]
tiempo=[n**3,m]
tamano22=[tamano[0]**3,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="red", label="O(N^3)")

"""O(N4)"""

m=max(tiempo_sol)
n=tiempo1[0]
tiempo=[n**4,m]
tamano22=[tamano[0]**4,tamano[-1]]
plt.loglog(tamano22,tiempo, linestyle="--", color="purple", label="O(N^4)")

if tipo=="solve":    
    if archivo == "dispersa":
        plt.xticks(tamano11, x11, rotation=45)
        plt.yticks(tiempo1, y1)
        plt.ylim(bottom=tiempo1[0], top=tiempo1[-1])
    if archivo == "llena":
        plt.xticks(tamano1, x1, rotation=45)
        plt.yticks(tiempo1, y1)
        plt.xlim(right=20000)
        plt.ylim(bottom=min(tiempo_sol), top=tiempo1[-1])
        
if tipo=="inv":
    plt.xticks(tamano1, x1, rotation=45)
    plt.yticks(tiempo1, y1)
    plt.xlim(right=20000)
    plt.ylim(bottom=min(tiempo_sol), top=tiempo1[-1])

plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo de solucion")
plt.legend()

plt.savefig(f"Laplaciana {tipo} {archivo}")
plt.show()

f.close()





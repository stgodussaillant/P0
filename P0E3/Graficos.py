# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

archivo = (input("Ingrese el nombre del archivo .txt (sin el .txt): "))
archivo1 = archivo + ".txt"
f = open(archivo1, "r")

datos = f.read()
datos = datos.split("\n")
datos.pop(0)
datos.pop(-1)
q=0
tiempo = []
tamano = []
memoria = []
while q<len(datos):
    fila = datos[q]
    fila = fila.split("   ")
    tiempo.append(float(fila[0]))
    memoria.append(float(fila[1]))
    tamano.append(float(fila[2]))
    q+=1

N = len(datos)/10
N = int(N)

x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamano1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

plt.subplot(2,1,1)
plt.title(f"Rendimiento inversa {archivo}")
r=0
t=0
while r < 10:
    while t < len(datos):
        plt.loglog(tamano[t:t+30],tiempo[t:t+30], "o-")
        t+=N
    r+=1
    
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, ["","","","","","","","","",""])
plt.xlim(right=20000)
plt.grid()
plt.ylabel("Tiempo transcurrido")

plt.subplot(2,1,2)
plt.loglog(tamano, memoria,"o-")
plt.hlines(y=8*10**9, xmin=0, xmax=20000, linestyle="--")
plt.xticks(tamano1, x1, rotation=45)
plt.yticks(memoria1,y2)
plt.xlim(right=20000)
plt.grid()
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")

caso = archivo
plt.savefig(caso)
plt.show()



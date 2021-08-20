# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

dtype = (input("Ingrese el dtype (single o double): "))
if dtype == "single":
    f = open("Caso_1_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh1 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh1.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_2.1_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh21 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh21.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_2.2_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh22 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh22.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_3.1_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh31 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh31.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_3.2_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh32 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh32.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


    f = open("Caso_4.1_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh41 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh41.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()
    
    f = open("Caso_4.2_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh42 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh42.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_5.1_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh51 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh51.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()
    
    f = open("Caso_5.2_eigh_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh52 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh52.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


elif dtype == "double":
    f = open("Caso_1_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh1 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh1.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_2.1_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh21 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh21.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()
    
    f = open("Caso_2.2_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh22 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh22.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_3.1_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh31 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh31.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()
    
    f = open("Caso_3.2_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh32 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh32.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


    f = open("Caso_4.1_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh41 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh41.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_4.2_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh42 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh42.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


    f = open("Caso_5.1_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh51 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh51.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()
    
    f = open("Caso_5.2_eigh_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_eigh = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_eigh.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_eigh52 = []
    w =0
    b=0
    while w < len(tiempo_eigh):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_eigh[t]
            t+=N
        prom_eigh52.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamano1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

plt.title("Rendimiento eigh")
plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh21, "o-", label="Eigh_caso2.1.txt")
plt.loglog(tamano[0:31],prom_eigh22, "o-", label="Eigh_caso2.2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 vs caso 2")
    plt.savefig("Desempeño eigh single caso 1 vs caso 2")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 vs caso 2")
    plt.savefig("Desempeño eigh double caso 1 vs caso 2")
plt.show()

plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh31, "o-", label="Eigh_caso3.1.txt")
plt.loglog(tamano[0:31],prom_eigh32, "o-", label="Eigh_caso3.2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 vs caso 3")
    plt.savefig("Desempeño eigh single caso 1 vs caso 3")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 vs caso 3")
    plt.savefig("Desempeño eigh double caso 1 vs caso 3")
plt.show()

plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh41, "o-", label="Eigh_caso4.1.txt")
plt.loglog(tamano[0:31],prom_eigh42, "o-", label="Eigh_caso4.2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 vs caso 4")
    plt.savefig("Desempeño eigh single caso 1 vs caso 4")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 vs caso 4")
    plt.savefig("Desempeño eigh double caso 1 vs caso 4")
plt.show()
    
plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh51, "o-", label="Eigh_caso5.1.txt")
plt.loglog(tamano[0:31],prom_eigh52, "o-", label="Eigh_caso5.2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 vs caso 5")
    plt.savefig("Desempeño eigh single caso 1 vs caso 5")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 vs caso 5")
    plt.savefig("Desempeño eigh double caso 1 vs caso 5")
plt.show()

plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh21, "o-", label="Eigh_caso2.1.txt")
plt.loglog(tamano[0:31],prom_eigh31, "o-", label="Eigh_caso3.1.txt")
plt.loglog(tamano[0:31],prom_eigh41, "o-", label="Eigh_caso4.1.txt")
plt.loglog(tamano[0:31],prom_eigh51, "o-", label="Eigh_caso5.1.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 a 5,1")
    plt.savefig("Desempeño eigh single caso 1 a 5,1")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 a 5,1")
    plt.savefig("Desempeño eigh double caso 1 a 5,1")
plt.show()

plt.loglog(tamano[0:31],prom_eigh1, "o-", label="Eigh_default.txt")
plt.loglog(tamano[0:31],prom_eigh22, "o-", label="Eigh_caso2.2.txt")
plt.loglog(tamano[0:31],prom_eigh32, "o-", label="Eigh_caso3.2.txt")
plt.loglog(tamano[0:31],prom_eigh42, "o-", label="Eigh_caso4.2.txt")
plt.loglog(tamano[0:31],prom_eigh52, "o-", label="Eigh_caso5.2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño eigh single caso 1 a 5,2")
    plt.savefig("Desempeño eigh single caso 1 a 5,2")
elif dtype=="double":
    plt.title("Desempeño eigh double caso 1 a 5,2")
    plt.savefig("Desempeño eigh double caso 1 a 5,2")
plt.show()

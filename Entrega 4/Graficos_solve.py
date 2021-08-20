# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

dtype = (input("Ingrese el dtype (single o double): "))
if dtype == "single":
    f = open("Caso_1_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve1 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve1.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_2_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve2 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve2.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_3_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve3 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve3.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_4_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve4 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve4.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_5_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve5 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve5.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_6_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve6 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve6.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_7_solve_single.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve7 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve7.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

elif dtype == "double":
    f = open("Caso_1_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve1 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve1.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_2_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve2 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve2.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_3_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve3 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve3.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_4_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve4 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve4.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_5_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve5 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve5.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_6_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve6 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve6.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()

    f = open("Caso_7_solve_double.txt", "r")

    datos = f.read()
    datos = datos.split("\n")
    datos.pop(0)
    datos.pop(-1)
    q=0
    tamano = []
    tiempo_solve = []
    while q<len(datos):
        fila = datos[q]
        fila = fila.split("   ")
        tiempo_solve.append(float(fila[0]))
        tamano.append(float(fila[1]))
        q+=1

    corrida = 10
    N = len(datos)/corrida            #Se divide por el numero de corridas
    N = int(N)
    
    prom_solve7 = []
    w =0
    b=0
    while w < len(tiempo_solve):
        a=0
        t=b
        while t<len(datos):
            a+=tiempo_solve[t]
            t+=N
        prom_solve7.append(a/corrida)    #Se divide por el numero de corridas
        b+=1
        w+=corrida                #El numero que aumenta w depende de las corridas
    
    f.close()


x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms", "1 ms", "10 ms","0.1 s", "1 s", "10 s", "1 min", "10 min"]
y2 = ["1 KB", "10KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamano1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

plt.title("Rendimiento solve")
plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve2, "o-", label="A_invB_npSolve2.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 2")
    plt.savefig("Desempeño solve single caso 1 vs caso 2")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 2")
    plt.savefig("Desempeño solve double caso 1 vs caso 2")
plt.show()

plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve3, "o-", label="A_invB_npSolve3.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 3")
    plt.savefig("Desempeño solve single caso 1 vs caso 3")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 3")
    plt.savefig("Desempeño solve double caso 1 vs caso 3")
plt.show()

plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve4, "o-", label="A_invB_npSolve4.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 4")
    plt.savefig("Desempeño solve single caso 1 vs caso 4")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 4")
    plt.savefig("Desempeño solve double caso 1 vs caso 4")
plt.show()
    
plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve5, "o-", label="A_invB_npSolve5.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 5")
    plt.savefig("Desempeño solve single caso 1 vs caso 5")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 5")
    plt.savefig("Desempeño solve double caso 1 vs caso 5")
plt.show()

plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve6, "o-", label="A_invB_npSolve6.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
plt.legend()
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 6")
    plt.savefig("Desempeño solve single caso 1 vs caso 6")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 6")
    plt.savefig("Desempeño solve double caso 1 vs caso 6")
plt.show()

plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve7, "o-", label="A_invB_npSolve7.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.legend()
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
if dtype=="single":
    plt.title("Desempeño solve single caso 1 vs caso 7")
    plt.savefig("Desempeño solve single caso 1 vs caso 7")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 vs caso 7")
    plt.savefig("Desempeño solve double caso 1 vs caso 7")
plt.show()

plt.loglog(tamano[0:31],prom_solve1, "o-", label="A_invB.txt")
plt.loglog(tamano[0:31],prom_solve2, "o-", label="A_invB_npSolve2.txt")
plt.loglog(tamano[0:31],prom_solve3, "o-", label="A_invB_npSolve3.txt")
plt.loglog(tamano[0:31],prom_solve4, "o-", label="A_invB_npSolve4.txt")
plt.loglog(tamano[0:31],prom_solve5, "o-", label="A_invB_npSolve5.txt")
plt.loglog(tamano[0:31],prom_solve6, "o-", label="A_invB_npSolve6.txt")
plt.loglog(tamano[0:31],prom_solve7, "o-", label="A_invB_npSolve7.txt")
plt.yticks(tiempo1, y1)
plt.xticks(tamano1, x1, rotation=45)
plt.xlim(right=20000)
plt.legend()
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz")
if dtype=="single":
    plt.title("Desempeño solve single caso 1 a 7")
    plt.savefig("Desempeño solve single caso 1 a 7")
elif dtype=="double":
    plt.title("Desempeño solve double caso 1 a 7")
    plt.savefig("Desempeño solve double caso 1 a 7")
plt.show()


# MCOC2021-P0

# Mi computador principal

* Marca/modelo: HP Pavilion 
* Tipo: Notebook
* Año adquisición: 2017
* Procesador:
  * Marca/Modelo: Intel Core i3-6100U
  * Velocidad Base: 2.30 GHz
  * Velocidad Máxima: 2304 MHz
  * Numero de núcleos: 2
  * Numero de hilos: 4
  * Arquitectura: AMD64
  * Set de instrucciones: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2,EM64T, VT-x, AES, AVX, AVX2, FMA3, TSX
* Tamaño de las cachés del procesador
  * L1d: 32 KB
  * L1i: 32 KB
  * L2: 256 KB
  * L3: 3.0 MB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR4
  * Velocidad: 2133 Mhz
  * Numero de (SO)DIMM: 
* Tarjeta Gráfica
  * Marca / Modelo: Intel HD Graphics 520
  * Memoria dedicada: 1 GB
  * Resolución: 1366 x 768
* Disco 1: 
  * Marca: TOSHIBA
  * Tipo: HDD
  * Tamaño: 932 GB
  * Particiones: 4
  * Sistema de archivos: NTFS
  
* Dirección MAC de la tarjeta wifi: 48:E2:44:DC:C0:7B
* Dirección IP (Interna, del router): 192.168.68.115
* Dirección IP (Externa, del ISP): 190.215.253.6
* Proveedor internet: GTD Internet S.A.

# Desempeño MATMUL

![Redimiento A@B](https://user-images.githubusercontent.com/88340864/128451252-f09511fd-96f8-4b78-86ee-e2bca738b80b.png)


* ¿Cómo difiere del gráfico del profesor/ayudante?
  * En el grafico del profesor la primera matriz no se demora tanto tiempo en ser calculada. Ademas, en mi caso, algunas matrices no se demoran tanto, pues siempre se mantienen tiempos mas o menos constantes, no como en el caso del profesor que hay algunas corridas en las que difiere mucho el tiempo.

* ¿A qué se pueden deber las diferencias en cada corrida?
  * Se debe a que durante cada corrida se estan utilizando otros elementos del computador que tambien utilizan parte de la memoria, por lo que esto ultimo se ve reflejado en el tiempo que le demora al programa en calcular cada matriz

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * El del tiempo transucrrido no es lineal ya que el tiempo que demora en calcular cada matriz no es acumulado. En cambio el de la memoria (si bien no es acumulativo) si considera la memoria utilizada por las matrices anteriores, pues es un tamaño mayor.

* ¿Qué versión de python está usando?
  * 3.6.5

* ¿Qué versión de numpy está usando?
  * 1.19.3

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
  * Si, se estan usando 4 procesadores
  ![Procesadores](https://user-images.githubusercontent.com/88340864/128451214-49431a5b-1ccb-4ae7-ac25-6d78eb66f81c.jpg)





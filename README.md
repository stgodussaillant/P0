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



# Desempeño INV

* El tamaño de memoria para cada uno de los tipos de datos son los que se muestran a continuacion:
  * Half: 10 bytes
  * Single: 8 bytes
  * Double: 16 bytes
  * Longdouble: 16 bytes

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.
  * El metodo de numpy debe usar el metodo de optimizar el algoritmo de Coppersmith y Winograd, porque la complejidad de matrices que puede trabajar no es tan alta como en los otros casos (complejidad: 2373x2373).
  * El metodo de scipy overwrite_a=False debe utilizar el mismo metodo de algoritmo de Coppersmith y Winograd, pues la complejidad de matrices es levemente mayor que en numpy (complejidad: 2376x2376).
  * El metodo de scipy overwrite_a=True debe usar el algoritmo de Strassen, pues la complejidad de matrices que puede trabajar es mayor que la de los casos anteriores (complejidad: 2807x2807).

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 
  * La estructura cache puede provocar que en cada caso el computador se demore mas en resolver las matrices, por lo que los procesadores funcionen al maximo mientras la memoria se encuentra completa. Esto ocurre en el caso de numpy, pues la memoria por lo general alcanza valores muy cercanos a su capacidad, mientra que los procesadores funcionan al maximo.
  * El paralelismo puede ayudar a que los problemas de matrices no consuman tantos recursos como la estructura cache, por lo que los procesadores no funcionan al maximo de su capacidad y la memoria no llega a valores cercanos a su capacidad. Esto ocurre en el caso de scipy.

* Para el primer caso (Numpy) los tipos de datos Half y Longdouble no eran procesados por el computador.
* Es por esto que las comparaciones de los usos de memorias y procesadores se haran en relacion a los tipos de datos Single y Double.

  * Caso 1 single
  ![Caso 1 single procesadores](https://user-images.githubusercontent.com/88340864/129997015-dbba8476-2d10-41ca-bcac-337fdf2a0056.jpeg)
  ![Caso 1 single memoria](https://user-images.githubusercontent.com/88340864/129996986-a692412e-e448-48ab-8715-4591502d7016.jpeg)
  
  * Caso 2 single
  ![Caso 2 single procesadores](https://user-images.githubusercontent.com/88340864/129997089-d00d59eb-1d3b-42b0-83d5-8c41b010d45a.jpeg)
  ![Caso 2 single memoria](https://user-images.githubusercontent.com/88340864/129997099-19b9046f-b44c-4467-ae3b-518a433332fc.jpeg)

  * Caso 3 single
  ![Caso 3 single procesadores](https://user-images.githubusercontent.com/88340864/129997116-93a36c74-ecad-4baf-b706-b5ca0fb159ae.jpeg)
  ![Caso 3 single memoria](https://user-images.githubusercontent.com/88340864/129997132-a4acbd20-f397-414d-928a-c0c7a1286ef1.jpeg)

  * Caso 1 double
  ![Caso 1 double procesadores](https://user-images.githubusercontent.com/88340864/129997146-85ccb4a7-1ec9-4367-8175-1701d776ba58.jpeg)
  ![Caso 1 double memoria](https://user-images.githubusercontent.com/88340864/129997161-53ee7075-ed9e-47fe-ada0-5906a7a55ce9.jpeg)

  * Caso 2 double
  ![Caso 2 double procesadores](https://user-images.githubusercontent.com/88340864/129997176-9f4d73ff-43bd-4919-8f2f-8141a61319bd.jpeg)
  ![Caso 2 double memoria](https://user-images.githubusercontent.com/88340864/129997194-05c0844f-bfff-4ca5-bdbb-8516ae63bfa5.jpeg)

  * Caso 3 double
  ![Caso 3 double procesadores](https://user-images.githubusercontent.com/88340864/129997222-5f342136-4f65-4a8b-ad55-c8dcb562cb2f.jpeg)
  ![Caso 3 double memoria](https://user-images.githubusercontent.com/88340864/129997234-6b392670-2de2-4b90-bcaf-eac84fd47123.jpeg)

* Como se puede observar en las imagenes, invertir una matriz con numpy consume muchos mas recursos que con scipy. Ademas, el uso de la memoria en numpy es mas "inestable" mientras que en scipy se mantiene en valores similiares.




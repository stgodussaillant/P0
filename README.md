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


# Desempeño SOLVE y EIGH

* SOLVE
  * En los distintos graficos se puede observar que la funcion solve requiere de mayor tiempo para resolver las matrices, mientras que la simple multiplicacion de la inversa por el vector de 1's no demora tanto como la funcion solve. Esto ocurre tanto en el dtype=single como en el dtype=double.
  * Durante la ejecucion del programa con dtype=single, el tiempo que le toma a cada matriz realizar el solve es bastante menor que el que utiliza el dtype=double, pues para este ultimo el tiempo que le toma al dtype=double es el doble que para dtype=single.
  * Ademas, durante la ejecucion de ambos dtypes se utilizan los 4 procesadores del computador, siendo en el caso del dtype=single que se utiliza en menor medida que en el caso del dtype=double.
  * Tambien, hay que señalar que el uso de la memoria en el caso del dtype=double es mayor que en el caso del dtype=single, en el cual la memoria se mantiene en valores mas bajos.
  * En base a lo anterior, claramente el algoritmo que utiliza un dtype=single es mejor, ya que demora menos tiempo en realizar el calculo de las matrices, ademas de utilizar menor memoria y los procesadores no se exigen mucho.
  * Finalmente, la superioridad del dtype=single se puede deber a que este funciona con 32 bits y por lo tanto utiliza menor memoria que el dtype=double, el cual funciona con 64 bits, lo que se puede traducir en un mayor uso de la memoria y de los procesadores, lo cual tambien conlleva a un mayor tiempo de ejecucion del codigo.

* EIGH
  * Debido a que las matrices de tamaño 7500 y 10000 provocaban que la corrida demorara mas de 2 minutos, se eliminaron estos terminos, llegando solo a tamaños de matrices de N=5000.
  * Ademas, cada caso se subdividio en dos casos, ovewrite_a=False y overwrite_=True. Cuando es caso False, se denota con un .1, mientras que cuando es True, con un .2. Por ejemplo, para el caso 2 con overwrite_a=False, el archivo corresponde al que sea 2.1, mientras que el 2.2 corresponde al caso 2 con overwrite_a=True.
  * Tambien, como el argumento driver no era reconocido por el computador, se cambio por turbo, el cual si funciona con la version de scipy que esta instalada en el computador.
  * Al igual que el caso de solve, cuando se ejecutaba el codigo con dtype=single, la memoria se mantenia en valores estables y no era utilizada en su totalidad. Cuando el dtype era igual a double, la memoria del computador tambien se mantenia en valores estables, pero esta utilizaba una mayor memoria, pues al trabajar con 64 bits este requiere de mayor memoria para ejecutar el codigo.
  * Para el caso de los procesadores, la situacion era similar al caso del solve, con el dtype=single se utilizan los 4 procesadores, sin que ninguno llegue al limite. Para el caso del dtype=double, tambien se usaban los 4 procesadores, pero a diferencia del dtype=single, este si llegaba a utilizar toda la capacidad de los procesadores cuando se trabajaban tamaños de matrices mas grandes, pero el tiempo de ejecucion no se veia impactado por esto ultimo.
  * Finalmente, a diferncia del solve, el dtype no influye en significativamente en el tiempo de ejecucion del codigo, donde si se nota la diferencia es en la memoria y en los procesadores, que si bien no llegan a utilizar todos los recursos, si se nota que el dtype=double requiere de mayores recursos para ejecutar el codigo.
  * Para los graficos con la funcion eigh, estos comparan el caso cuando eigh usa valores por defecto (caso 1) y el caso corresponiente con driver (o turbo en este caso). Por ejemplo, un grafico compara el caso 1 con el caso 2.1 y 2.2, para poder ver y analizar el como se influye el overwrite_a en las distintas funciones.
  * En los graficos se puede notar como no existe tanta diferencia entre los casos con overwrite_a=False y overwrite_a=True. Ademas, las mayores variaciones se presentan entre las matrices de tamaño 10 y 200, pero de igual forma aquellas variaciones de tiempo son menores a 0.1s, por lo que no es significativo.


# Matrices dispersas y complejidad computacional

* Complejidad algoritmica de MATMUL
  * El codigo para ensamblar la matriz laplaciana para el formato llena y tipo double es el que se muestra a continuacion:
   ```
   def Laplaciana(N, t=double):            #Laplaciana llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)
   ```
   * Para el caso con formato dispersa y tipo double, el codigo para ensamblar la matriz laplaciana fue:
   ```
   def Laplaciana(N, t=double):                                    #Laplaciana dispersa
    e = sparse.eye(N, dtype=t)-sparse.eye(N,N,1,dtype=t)
    return e+e.T
   ```

  * En los graficos del formato disperso se puede observar que esta demora mucho menos que el formato lleno en ensamblar y en encontrar la solucion de MATMUL. Esto se debe a que la matriz dispersa no considera los valores de 0 dentro de su ensamblaje, y tampoco lo hace para solucionar MATMUL.
  * Esto provoca que este formato no utilize tantos recursos (y por lo tanto demore menos en procesar) como el formato lleno. Es por esto que con matrices dispersas se pueden procesar matrices de tamaños muy superiores, en comparacion a las matrices llenas, de hecho se pueden procesar matrices de hasta 10.000.000x10.000.000, mientras que las matrices llenas solo pueden procesar matrices de hasta 10.000x10.000
 
  ![Laplaciana dispersa](https://user-images.githubusercontent.com/88340864/131069324-3765dc16-4543-4c43-b399-8db02548bf07.png)
  
  ![Laplaciana llena](https://user-images.githubusercontent.com/88340864/131069339-0e491eab-9c1c-4657-a84b-6926c128e802.png)




# -*- coding: utf-8 -*-

from time import perf_counter
#from numpy import zeros
#from numpy.linalg import inv
from scipy.linalg import inv
from numpy import float16, float32, float64
from Laplaciana import laplaciana              #Se llama a la funcion desde otro archivo

"""
Se puede poner la funcion en este mismo archivo para no estar cargando todo el rato
el otro archivo
"""


N = 100

t1 = perf_counter()
A = laplaciana(N, dtype=float64)
t2 = perf_counter()

Am1 = inv(A)
t3 = perf_counter()

dt_ensamblaje = t2-t1       #Tiempo de armado de laplaciana
dt_inversion = t3-t2        #tiempo que demora en invertir laplaciana

bytes_total= A.nbytes+Am1.nbytes

print (f"Uso memoria: {bytes_total} bytes")
print (f"Tiempo ensamblaje: {dt_ensamblaje} s")
print (f"Tiempo inversion: {dt_inversion} s")






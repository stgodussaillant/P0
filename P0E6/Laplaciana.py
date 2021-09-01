# -*- coding: utf-8 -*-

from scipy.sparse import lil_matrix
import numpy as np
from numpy import double
from scipy import sparse

def laplaciana(N, dtype):
    A=lil_matrix((N,N),dtype=dtype)
    
    for i in range(N):
        A[i,i]=2
        for j in range(max(0,i-2),i):
            if abs(i-j)==1:
                A[i,j]=-1
                A[j,i]=-1
                
    return (A)

def laplaciana_llena(N, t=double):            #Laplaciana llena
    e=np.eye(N)-np.eye(N,N,1)
    return t(e+e.T)

def laplaciana_dispersa(N, t=double):                                    #Laplaciana dispersa
    e = sparse.eye(N, dtype=t)-sparse.eye(N,N,1,dtype=t)
    return e+e.T


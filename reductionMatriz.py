from turtle import shape
import numpy as np 
from mpi4py import MPI 
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank
global MultiprocesoTotal1
size_ = (10000,10000)
matriz1 = np.random.randint(10, size=size_).astype("float") / 100

corte1=np.hsplit(matriz1,4)
nueva1_1=corte1[0]
size1=np.shape(nueva1_1)

nueva2_1=corte1[1]
size2=np.shape(nueva2_1)

nueva3_1=corte1[2]
size3=np.shape(nueva3_1)

nueva4_1=corte1[3]
size4=np.shape(nueva4_1)   

result1S = np.zeros(dtype=float, shape=size1)
result2S = np.zeros(dtype=float, shape=size2)
result3S = np.zeros(dtype=float, shape=size3)
result4S = np.zeros(dtype=float, shape=size4)

result1R = np.zeros(dtype=float, shape=size1)
result2R = np.zeros(dtype=float, shape=size2)
result3R = np.zeros(dtype=float, shape=size3)
result4R = np.zeros(dtype=float, shape=size4)

if (rank==1):
    nueva1_1R=corte1[0]
    nueva2_1R=corte1[1]
    nueva3_1R=corte1[2]
    nueva4_1R=corte1[3]
    MultiprocesoTotal1=np.concatenate((nueva1_1,nueva2_1,nueva3_1,nueva4_1),axis=1)
    print('Matriz 1')
    for i in range(9995,10000,1):
        print("%f" % (MultiprocesoTotal1[i][i]))
else: 
    nueva1_1R=-nueva1_1
    nueva2_1R=-nueva2_1
    nueva3_1R=-nueva3_1
    nueva4_1R=-nueva4_1 
    
comm.Reduce(np.ascontiguousarray(nueva1_1),np.ascontiguousarray(result1S),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva2_1),np.ascontiguousarray(result2S),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva3_1),np.ascontiguousarray(result3S),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva4_1),np.ascontiguousarray(result4S),root=0,op=MPI.SUM)

comm.Reduce(np.ascontiguousarray(nueva1_1R),np.ascontiguousarray(result1R),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva2_1R),np.ascontiguousarray(result2R),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva3_1R),np.ascontiguousarray(result3R),root=0,op=MPI.SUM)
comm.Reduce(np.ascontiguousarray(nueva4_1R),np.ascontiguousarray(result4R),root=0,op=MPI.SUM)

sumaMultiprocesoTotal=np.concatenate((result1S,result2S,result3S,result4S),axis=1)
restaMultiprocesoTotal=np.concatenate((result1R,result2R,result3R,result4R),axis=1)

if (rank==0):
    MultiprocesoTotal2=np.concatenate((nueva1_1,nueva2_1,nueva3_1,nueva4_1),axis=1)
    print('Matriz 2')
    for i in range(9995,10000,1):
            print("%f" % (MultiprocesoTotal2[i][i]))
    print("resultado Suma")
    for i in range(9995,10000,1):
            print("%f" % (sumaMultiprocesoTotal[i][i]))
    print("resultado Resta")
    for i in range(9995,10000,1):
            print("%f" % (restaMultiprocesoTotal[i][i]))

# print(np.shape(sumaMultiprocesoTotal))


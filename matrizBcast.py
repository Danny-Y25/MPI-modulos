from logging import root
from mpi4py import MPI
import numpy as np 


comm=MPI.COMM_WORLD
rank = comm.rank

    
t1 = MPI.Wtime();


 
print("my rank is : " , rank)



if rank==0:
 
    size_ = (200,200)
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100

    corte1=np.hsplit(matriz1,4)
    corte2=np.hsplit(matriz2,4)

    nueva1_1=corte1[0]
    nueva1_2=corte2[0]
    

    nueva2_1=corte1[1]
    nueva2_2=corte2[1]
    
    nueva3_1=corte1[2]
    nueva3_2=corte2[2]
    

    nueva4_1=corte1[3]
    nueva4_2=corte2[3]
    

    destination_process = 0
    destination_process2 = 0
    destination_process3 = 0
    destination_process4 = 0

    
    comm.bcast(nueva1_1,root=destination_process)
    comm.bcast(nueva1_2,root=destination_process)
    
    comm.bcast(nueva2_1,root=destination_process2)
    comm.bcast(nueva2_2,root=destination_process2)
    
    comm.bcast(nueva3_1,root=destination_process3)
    comm.bcast(nueva3_2,root=destination_process3)
    
    comm.bcast(nueva4_1,root=destination_process4)
    comm.bcast(nueva4_2,root=destination_process4)
else:
    nueva1_1=None
    nueva1_2=None


    nueva2_1=None
    nueva2_2=None


    nueva3_1=None
    nueva3_2=None
  

    nueva4_1=None
    nueva4_2=None
    

    destination_process = None
    destination_process2 = None
    destination_process3 = None
    destination_process4 = None

    
   
if rank==1:
    
    # print(size_)
    matriz1=comm.bcast(nueva1_1,root=0)
    # print(np.shape(matriz1)[0])
    matriz2=comm.bcast(nueva1_2,root=0)
    # print(np.shape(matriz2))
    size_ = np.shape(matriz1)
    suma = np.zeros(dtype=float, shape=size_)
    resta = np.zeros(dtype=float, shape=size_)
   
    for i in range(np.shape(matriz1)[0]):
        for j in range(np.shape(matriz1)[1]):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]
            resta[i][j] = matriz1[i][j] - matriz2[i][j]
    comm.send(suma,dest=5)
    comm.send(resta,dest=5)
    comm.send(matriz1,dest=5)
    comm.send(matriz2,dest=5)

   

if rank==2:
    
    # print(size_)
    matriz1=comm.bcast(nueva2_1,root=0)
    # print(np.shape(matriz1)[0])
    matriz2=comm.bcast(nueva2_2,root=0)
    size_ = np.shape(matriz1)
    
    suma = np.zeros(dtype=float, shape=size_)
    resta = np.zeros(dtype=float, shape=size_)
   
    for i in range(np.shape(matriz1)[0]):
        for j in range(np.shape(matriz1)[1]):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]
            resta[i][j] = matriz1[i][j] - matriz2[i][j]
    comm.send(suma,dest=5)
    comm.send(resta,dest=5)
    comm.send(matriz1,dest=5)
    comm.send(matriz2,dest=5)

    
            
    
if rank==3:
    
    matriz1=comm.bcast(nueva3_1,root=0)
    # print(np.shape(matriz1)[0])
    matriz2=comm.bcast(nueva3_2,root=0)

    size_ = np.shape(matriz1)
    
    suma = np.zeros(dtype=float, shape=size_)
    resta = np.zeros(dtype=float, shape=size_)
   
    for i in range(np.shape(matriz1)[0]):
        for j in range(np.shape(matriz1)[1]):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]
            resta[i][j] = matriz1[i][j] - matriz2[i][j]
    comm.send(suma,dest=5)
    comm.send(resta,dest=5)
    comm.send(matriz1,dest=5)
    comm.send(matriz2,dest=5)

    
   

if rank==4:
    
    matriz1=comm.bcast(nueva4_1,root=0)
    # print(np.shape(matriz1)[0])
    matriz2=comm.bcast(nueva4_2,root=0)
    size_ = np.shape(matriz1)
    
    suma = np.zeros(dtype=float, shape=size_)
    resta = np.zeros(dtype=float, shape=size_)
   
    for i in range(np.shape(matriz1)[0]):
        for j in range(np.shape(matriz1)[1]):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]
            resta[i][j] = matriz1[i][j] - matriz2[i][j]
    comm.send(suma,dest=5)
    comm.send(resta,dest=5)
    comm.send(matriz1,dest=5)
    comm.send(matriz2,dest=5)

   

if rank==5:
    
    global t2
    
    
    # sumaMultiprocesoTotal=np.concatenate((comm.bcast(suma,root=1),comm.bcast(suma,root=2),comm.bcast(suma,root=3),comm.bcast(suma,root=4)),axis=1)
    # restaMultiprocesoTotal=np.concatenate((comm.bcast(resta,root=1),comm.bcast(resta,root=2),comm.bcast(resta,root=3),comm.bcast(resta,root=4)),axis=1)
    # MultiprocesoTotal1=np.concatenate((comm.bcast(matriz1,root=1),comm.bcast(matriz1,root=2),comm.bcast(matriz1,root=3),comm.bcast(matriz1,root=4)),axis=1)
    # MultiprocesoTotal2=np.concatenate((comm.bcast(matriz2,root=1),comm.bcast(matriz2,root=2),comm.bcast(suma,root=3),comm.bcast(matriz2,root=4)),axis=1)
    # print(np.shape(MultiprocesoTotal1))
    sumaMultiprocesoTotal=np.concatenate((comm.recv(source=1),comm.recv(source=2),comm.recv(source=3),comm.recv(source=4)),axis=1)
    restaMultiprocesoTotal=np.concatenate((comm.recv(source=1),comm.recv(source=2),comm.recv(source=3),comm.recv(source=4)),axis=1)
    MultiprocesoTotal1=np.concatenate((comm.recv(source=1),comm.recv(source=2),comm.recv(source=3),comm.recv(source=4)),axis=1)
    MultiprocesoTotal2=np.concatenate((comm.recv(source=1),comm.recv(source=2),comm.recv(source=3),comm.recv(source=4)),axis=1)
    print(np.shape(MultiprocesoTotal1))
    t2 = MPI.Wtime(); 
    print( "Elapsed time is %f\n", t2 - t1 ) 
    # for i in range(90,100,1):
    #     print("%f + %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], sumaMultiprocesoTotal[i][i]))

    # print("Resta de matrices")
    # for i in range(90,100,1):
    #     print("%f - %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], restaMultiprocesoTotal[i][i]))
    # for i in range(5):
    #     print("%f + %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], sumaMultiprocesoTotal[i][i]))

    # print("Resta de matrices")
    # for i in range(5):
    #     print("%f - %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], restaMultiprocesoTotal[i][i]))


 
    
    
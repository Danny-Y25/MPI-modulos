from mpi4py import MPI
import numpy as np 


comm=MPI.COMM_WORLD
rank = comm.rank

    
t1 = MPI.Wtime();


 
print("my rank is : " , rank)



if rank==0:
    size_ = (2000,2000)
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100

    corte1=np.hsplit(matriz1,4)
    corte2=np.hsplit(matriz2,4)

    nueva1_1=corte1[0]
    nueva1_2=corte2[0]
    size1=np.shape(nueva1_1)

    nueva2_1=corte1[1]
    nueva2_2=corte2[1]
    size2=np.shape(nueva2_1)

    nueva3_1=corte1[2]
    nueva3_2=corte2[2]
    size3=np.shape(nueva3_1)

    nueva4_1=corte1[3]
    nueva4_2=corte2[3]
    size4=np.shape(nueva4_1)
    
    destination_process = 1
    destination_process2 = 2
    destination_process3 = 3
    destination_process4 = 4

    comm.send(size1,dest=destination_process)
    comm.send(nueva1_1,dest=destination_process)
    comm.send(nueva1_2,dest=destination_process)
    comm.send(size2,dest=destination_process2)
    comm.send(nueva2_1,dest=destination_process2)
    comm.send(nueva2_2,dest=destination_process2)
    comm.send(size3,dest=destination_process3)
    comm.send(nueva3_1,dest=destination_process3)
    comm.send(nueva3_2,dest=destination_process3)
    comm.send(size4,dest=destination_process4)
    comm.send(nueva4_1,dest=destination_process4)
    comm.send(nueva4_2,dest=destination_process4)
    
   
if rank==1:
    size_ = comm.recv(source=0)
    matriz1=comm.recv(source=0)
    matriz2=comm.recv(source=0)
    
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
    size_ = comm.recv(source=0)
    matriz1=comm.recv(source=0)
    matriz2=comm.recv(source=0)
    
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
    size_ = comm.recv(source=0)
    matriz1=comm.recv(source=0)
    matriz2=comm.recv(source=0)
    
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
    size_ = comm.recv(source=0)
    matriz1=comm.recv(source=0)
    matriz2=comm.recv(source=0)
    
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
    global sumaMultiproceso
    global restaMultiproceso
    global sumaMultiprocesoTotal
    global restaMultiprocesoTotal
    global MultiprocesoTotal1
    global MultiprocesoTotal2
    
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
    for i in range(5):
        print("%f + %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], sumaMultiprocesoTotal[i][i]))

    print("Resta de matrices")
    for i in range(5):
        print("%f - %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], restaMultiprocesoTotal[i][i]))


 
    
    
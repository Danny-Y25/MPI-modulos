from mpi4py import MPI
import numpy as np 


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()



# print("my rank is : " , rank)

size_ = (10000,10000)
matriz1 = np.random.randint(10, size=size_).astype("float") / 100
matriz2 = np.random.randint(10, size=size_).astype("float") / 100

corte1=np.hsplit(matriz1,4)
corte2=np.hsplit(matriz2,4)

        

nueva1_1=corte1[rank-1]
nueva1_2=corte2[rank-1]
size1=np.shape(nueva1_1)
result1S = np.zeros(dtype=float, shape=size1)
result1R = np.zeros(dtype=float, shape=size1)

for i in range(np.shape(nueva1_1)[0]):
        for j in range(np.shape(nueva1_1)[1]):
            result1S[i][j] = nueva1_1[i][j] + nueva1_2[i][j]
            result1R[i][j] = nueva1_1[i][j] - nueva1_2[i][j]

data1 = comm.gather(nueva1_1, root=4)
data2 = comm.gather(nueva1_2, root=4)
data3 = comm.gather(result1S, root=4)
data4 = comm.gather(result1R, root=4)



if rank == 4:
    # print ("rank = %s " %rank +\
    #       "...receiving data to other process")
    
    MultiprocesoTotal1=np.concatenate((data1[0],data1[1],data1[2],data1[3]),axis=1)
    MultiprocesoTotal2=np.concatenate((data2[0],data2[1],data2[2],data2[3]),axis=1)
    sumaMultiprocesoTotal=np.concatenate((data3[0],data3[1],data3[2],data3[3]),axis=1)
    restaMultiprocesoTotal=np.concatenate((data4[0],data4[1],data4[2],data4[3]),axis=1)
    # print(np.shape(MultiprocesoTotal1))

    # for i in range(1995,2000,1):
    #     print("%f + %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], sumaMultiprocesoTotal[i][i]))

    # print("Resta de matrices")
    # for i in range(1995,2000,1):
    #     print("%f - %f = %f" % (MultiprocesoTotal1[i][i], MultiprocesoTotal2[i][i], restaMultiprocesoTotal[i][i]))


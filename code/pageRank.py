import numpy as np
steps= 20
alpha=0.5
N=3
A=np.array([[0,1,0],
           [1,0,1],
		   [0,1,0]])

# create P
Y=np.count_nonzero(A ==1, axis=0)
P=(A.T / Y).T # Step 1 divide each row with # of 1s
P= (1-alpha)*P+ (alpha/N) # non teleporation and teleporation
print(P)
# todo convert row with all zeros to all ones.


print("Result of algorithms as given in IIR book \nPower iteration method")
#print(P)
x= np.array([0,1,0])#(1/N)*np.array([1,1,1])#
#print(x)
for i in range(steps):
    print(i,x)
    x=np.dot(x, P)
    




print("Result of algorithm as given in SE book")
I=(1/N)*np.array([1,1,1])
for j in range(steps):
    print(j,I)
    R=(alpha/N)*np.array([1,1,1]) # adding teleporation probability
    #print(z)
    for i in range(N):
        #get ith node's outlink nodes
        Q=np.argwhere(A[i]==1)    #todo use adj list and change this line      
        Q=np.reshape(Q, (1,Q.shape[0]))[0]

        if Q.shape[0]>0:
            # divide ith nodes probabbility into its outnodes
            R[Q]= R[Q]+ (1-alpha)*I[i]/Q.shape[0]
        else:
            for j in range(N):
                R[j]= R[j] + (1-alpha)*I[i]/N
    I=R # update
   
'''
A=np.array([[0,1/2,1/2],[1/3,1/3,1/3],[1/2,1/2,0]])
P= 0.9*A + (0.1/3)*(np.ones(A.shape))
print(P)

x= np.array([0,0.75,0.25])#np.array([0,1,0])
#print(x)
for i in range(steps):
    print(i,x)
    x=np.dot(x, P)



        
'''

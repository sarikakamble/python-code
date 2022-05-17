import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as m

X=[0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3]
Y=[0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]

#data set
A=np.array(list(zip(X,Y)))
print(" DATASET ",A)

# 2 clusters
k1=[]
k2=[]

# 2 centroids are 
b=c1=[0.1,0.3]
v=c2=[0.6,0.2]

for i in range(8):
    m1=m.sqrt(((X[i]-c1[0])**2)+((Y[i]-c1[1])**2))#euclidean distance of k1
    m2=m.sqrt(((X[i]-c2[0])**2)+((Y[i]-c2[1])**2))#euclidean distance for k2
    print("eculidean distance for " ,i,"is ",m1,"and ",m2,"\n")
    if(m1<m2):
        k1.append(i+1)
        c1=[(X[i]+c1[0])/2,(Y[i]+c1[1])/2] #change in centroid 
        print(" new centroid of M1 " ,c1,"\n")
    else:
        k2.append(i+1)
        c2=[(X[i]+c2[0])/2,(Y[i]+c2[1])/2]#change in centroid
        print(" new centroid is M2" ,c2,"\n")
# population of the cluster
print(" CLUSTER  K1 COntains ",k1)
print(" CLUSTER  K2 COntains ",k2)



print("centroids are",b,v)
print("UPDATED centroids are",c1,c2)

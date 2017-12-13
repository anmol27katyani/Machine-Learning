import numpy as np
import matplotlib.pyplot as pltcd

#Below is the Distance function required
def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

X_train= np.array([[1,1],[2,2.5],[3,1.2],[5.5,6.3],[6,9],[7,6]])
Y_train=['red','red','red','blue','blue','blue']

plt.figure
# Here s is the size of the dot being plotted
plt.scatter(X_train[:,0],X_train[:,1], s=170,color=Y_train[:])
#X_train holds all the coordinates being given
plt.show()

#To compute distance from every point in X_train
num=len(X_train)
distance=np.zeroes(num) # Numpy array of zeroes
for i in range(num):
    distance[i]=dist(X_train[i],X_test)
print(distance)

import numpy as np
import matplotlib.pyplot as plt

X_train= np.array([[1,1],[2,2.5],[3,1.2],[5.5,6.3],[6,9],[7,6]])
Y_train=['red','red','red','blue','blue','blue']

plt.figure
# Here s is the size of the dot being plotted
plt.scatter(X_train[:,0],X_train[:,1], s=170,color=Y_train[:])
#X_train holds all the coordinates being given
plt.show()

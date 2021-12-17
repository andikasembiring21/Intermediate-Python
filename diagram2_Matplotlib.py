import matplotlib.pyplot as plt
import random
import numpy as np

arr=np.random.normal(size=40).reshape(20,2)
plt.plot(arr,color='teal',marker='o',linestyle='dashed')
plt.show()
 

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

df=pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('abcd'))
print(df)

print(df.describe())

np.random.seed(10)

n=30
x=np.random.rand(n)
y=np.random.rand(n)
colors=np.random.rand(n)
area=(30*np.random.rand(n))**3
plt.scatter(x,y,s=area,c=colors,alpha=0.9)
plt.show()

from matplotlib import style
style.use('ggplot')

x=[2,4,5]
y=[23,53,23]
x2=[12,34,25]
y2=[2,25,3]

plt.bar(x,y,color='r',align='center')
plt.bar(x2,y2,color='b',align='center')

plt.title("info")
plt.ylabel("y axix")
plt.xlabel("x axix")
plt.show()

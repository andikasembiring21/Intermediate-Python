import matplotlib.pyplot as plt
import random
import numpy as np

x=[1.3,2.4,3.6,4.6,5.3,6.7,7.3,8.6,9.8,10.4]
y=[random.randrange(1,100) for i in range(10)]
y2=[random.randrange(1,100) for i in range(10)]
plt.plot(x,y,'ro-',x,y,'bo') #memberikan efek titik di ujug grafik, 'b' pengaturan warna 
#plt.plot(x,y,'b*-')
#plt.plot(x,y,'bo')
plt.plot(x,y2,'go--',x,y2,'ro')
#plt.plot(x,y2,'ro')
plt.title("judul simple")
plt.xlabel("sumbu X")
plt.ylabel("sumbu Y")

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import random

x=np.linspace(0,10)

fig,((ax1,ax2,aux1),(ax3,ax4,aux2))=plt.subplots(2,3,sharex=True,sharey=True)

aux1.axis("off")
aux2.axis("off")

ax5=fig.add_subplot(133)

ax1.plot(x,np.sin(x))
ax2.plot(x,np.sin(x))
ax3.plot(x,np.sin(x))
ax4.plot(x,np.sin(x))
ax5.plot(5*x,x)

plt.show()


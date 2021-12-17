import matplotlib.pyplot as plt

#creating figure
figure=plt.figure()

#creating subplot
ax=figure.add_subplot(111) #define 1 row, 1 column and start at index 1

ax.set_title('Judul diagram')

ax.set_ylabel('Sumbu -Y')
ax.set_xlabel('Sumbu -X')

figure,ax = plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True)
ax[0,0].set(title="Upper Left")
ax[0,1].set(title="Upper Right")
ax[1,0].set(title="Lower Left")
ax[1,1].set(title="Lower Right")


plt.show()

             

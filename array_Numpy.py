import numpy as np

angka=np.array([3,5,2,5,2,6,23,64,23,2])
print(angka)

print(angka.ndim)
print(angka.shape)

for i in angka.flat:
    print(i,end= " ")

#array dengan spesifik nilai
print(np.zeros(5))

print(np.ones((5,4),dtype=int))

print(np.full((3,5),15))

#here show arrange 1-10 in list
print(np.arange(10))
tets=[]
test=np.arange(10)
print(test)

#show rang start 5 until 12
print(np.arange(5,12))

#start 20, end 2 with steps -3
print(np.arange(20,2,-3))

print(np.arange(1,100001).reshape(4,25000))

print(np.arange(1, 100001).reshape(100, 1000))

angkat=np.arange(1,30)

print(angkat ** 2)


for i in range (1,100):
    tp=chr(i)
    print(tp)


angka = np.linspace(1.1,5.5,5)
print(angka)

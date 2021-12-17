import numpy as np
import cv2

cap=cv2.VideoCapture(0)
while (True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

"""a=1
b=5
for x in range(a,b):
    for y in range(1,x):
        print("z",end="")
    print("")
s=("pakaian","kemeja","l",79,"pria")
print(s[1][5])

a=50
b=100
if(a>=b):
    m=a
else:
    b=a
    m=b
print(m)
s=3
b=4
if(b!=(s**2)):
   print("b")
else:
    print("salah")
a=10
b=5
m=a
a=b
b=m
print(a)
for z in range(-10,-2,2):
    print(z,end="")

data=("a","d","r","w","o")
print(data[1])
print(data.index('r'))

a=[1,2,3,4]
def kal(x):
    return x*3
hasil=map(kal,a)
print(list(hasil))


a=int(input())
b=int(input())
for x in range(a,b):
    print("*",end="")

a=100
b=50
if(a==b):
    m=a*3
else:
    if(a%b==0):
        m=a*5
    else:
        m=b*7
print(m)

print("\n")

for x in range(1,1):
    print(x)

data=[('b',77),('r',58),('m',99)]
n=[]
for x in data:
    n.append(x[1])
print(sorted(n))
"""

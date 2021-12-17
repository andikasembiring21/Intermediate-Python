import random
lower = "abcdefghijklmnopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
simbol = "[]{}!@#$%^&*()_=-;?><,.|/"
all = lower+upp+number+simbol
length =9
tampung=""
psswd="".join(random.sample(all,length))
print("your generator password : ",psswd)

tampung=input("masukkan ulang : ")
if tampung != psswd:
    print("try again")
else:
    print("welcome user")

import numpy as np

start=int(input("masukkan angka mulai: "))
end=int(input("masukkan angka batas: "))

print("1. angka akan di pangkat kan 1")
print("2. angka akan di pangkat kan 2")
print("3. angka akan di pangkat kan 3")
print("4. input manual: ")

pilihan=int(input("masukkan pilihan: "))
tampung=np.arange(start,end)

if pilihan == 1:
    print(tampung **1)
elif pilihan == 2:
    print(tampung ** 2)
elif pilihan == 3:
    print(tampung ** 3)
else:
    tpl=int(input("masukkan pangkat: "))
    print(tampung**tpl)


import pandas as pd
import matplotlib.pyplot as plt

tampung=pd.read_csv('Intermediete_Python/file/Users.csv')

print(tampung,"\n")

print(tampung.head(5))

tpng=pd.DataFrame(tampung)
print(tpng.keys())

print(tpng.T)
print(tpng.T.describe())

tampil=pd.DataFrame(tampung,columns=["Name","Email","Password"])
print(tampil)



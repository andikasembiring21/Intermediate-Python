import pandas as pd

average=pd.Series([43,23,53,23,64,23,64,23])

Max=average.max()
Min=average.min()
count=average.count()
std=average.std()
de=average.describe()

print(average,"\n")
print("nilai max ",Max)
print("nilai min ",Min)
print("jumlah nilai",count)
print("std ",std,"\n")

print("describes ",de,"\n")

print(pd.Series(94.6,range(4)),"\n")

data=pd.Series([45,34,23,44,23,64,23,64], index=['santo','daf','ra','dg','te','uy','wr','tw'])
print(data)
    

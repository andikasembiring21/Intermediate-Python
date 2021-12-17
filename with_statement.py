#untuk menulis di dalam text
try:
    with open('test.txt',mode='w') as ac:
        ac.write('100 jones 23.23\n')
        ac.write('200 daffd 54.23\n')
        ac.write('300 afsdf 54.45\n')
        ac.write('400 adfkd 53.54\n')
        ac.write('500 dfsad 64.34\n')
        
except FileNotFoundError:
    print("the file name not exist")

#untuk menampilkan isi di dalam text
try:
    with open('test.txt',mode='r') as ac:
        print(f'{"Account":<10} {"Name":<10} {"Balance":>4}')
        for record in ac:
            acc,name,balance=record.split()
            print(f'{acc:<10}{name:<10}{balance:>7}')
            
except FileNotFoundError:
    print("the file name not exist")       

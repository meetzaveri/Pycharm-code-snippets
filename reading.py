import os

cuwodi = os.getcwd()
print (cuwodi)

data = open('sham.txt')

print(data.readline() , end='')

for lineindata in data:
    print(lineindata, end='')

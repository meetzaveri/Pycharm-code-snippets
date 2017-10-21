import random
import sys
import os
from sklearn import tree

for x in range(0,10):
    print(x , ' ' , end="")


grocery_list =['Juice','Potatoes','Tomatoes','Carrots','Pickles']

print(" \n")

for y in grocery_list:
    print(y)

num_list=[[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

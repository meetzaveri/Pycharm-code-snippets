## Note that this is for subset containing only two numbers that eqaul to sum
numlist = [3,35,4,12,5,8]
sum = 9
someother = []
isthere=[]

def doverification():
    for i in numlist:
        if(i<9):
            someother.append(i)
        else:
            print('number <9')
            
## calling verification
doverification()

l=1
## For appending values that match equal to sum
def doappending():
    for k in someother:
        for l in someother:
            if(l + k == sum):
                print('Its a match')
                if l not in isthere:
                    isthere.append(l)
                    isthere.append(k)
                else:
                    continue
            else:
                print(' Not a match')


doappending()
print(isthere)

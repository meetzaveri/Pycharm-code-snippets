arr = []
newarr = []

def chunks(arr,length):

    for i in range(0, len(arr), length):

        if(i != 0):
            newarr.append(arr[i:i + length])
        else:
            newarr.append(arr[i:length])


    print(newarr)
    return newarr

chunks([2,4,5,7,3,1,6,7,564,423,2,57,88,6],6)

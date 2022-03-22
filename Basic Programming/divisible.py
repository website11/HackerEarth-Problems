def arraySize():
    newArray = int(input())
    return newArray

def arrayNum(size):
    i = 0
    numbers = input()
    newArray = numbers.split()
    return newArray

if __name__ == '__main__':
    i = 0
    j = 0

    newNum = ""
    array_size = arraySize()
    arrayList = arrayNum(array_size)

    for i in range(array_size):
        if(i < array_size/2):
            first_letter = arrayList[i][0]
            newNum = newNum + first_letter
        else:
            last_letter = arrayList[i][-1]
            newNum = newNum + last_letter
    
    newNum = int(newNum)
    if (newNum % 11 == 0):
        print("OUI")
    else:
        print("NON")
    


    
    

    

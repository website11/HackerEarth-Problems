def testCase():
    test_cases = int(input())
    return test_cases

def balloonCost():
    cost = input()
    costList = cost.split()
    numCostList = [int(x) for x in costList]
    return numCostList

def participants():
    totalPeople = int(input())
    return totalPeople

def correct():
    answer = input()
    answerList = answer.split()
    numAnswerList = [int(x) for x in answerList]
    return numAnswerList

def totalCost(answer,newList):
    if(answer[0] == 1):
        newList[0] += 1
    
    if(answer[1] == 1):
        newList[1] += 1
    
    

if __name__ == '__main__':
    cases = testCase()
    i = 0
    j = 0
    count = [0,0]

    while i < cases:
        costList = balloonCost()
        totalPeople = participants()
        
        while j < totalPeople:
            answer = correct()
            totalCost(answer,count)
            j += 1

        price = (count[0] * costList[0]) + (count[1] * costList[1])
        priceB = (count[0] * costList[1]) + (count[1] * costList[0])
        if(price > priceB):
            print(priceB)
        else:
            print(price)
        price = 0
        count = [0,0]
        j = 0
        i += 1

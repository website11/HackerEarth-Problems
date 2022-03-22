def testCases():
    test_case = int(input())
    return test_case

def gridSize():
    newGrid = list(map(int,input().split()))
    return newGrid

if __name__ == '__main__':
    test_cases = testCases()
    i = 0
    j = 0
    k = 0
    max = 0
    
    while (i < test_cases):
        grid_size = gridSize()
        while j < grid_size[0]:
            shape = list(input())
            total = shape.count('#')
            if(total > max):
                max = total
            j += 1
        j = 0
        print(max)
        max = 0
        i += 1

        
        
            



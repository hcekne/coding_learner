def binGap(N):
    # Implement your solution here
    string = f'{N:b}'
    #print(string)
    list1 = list(string)
    listLength = len(list1)
    #print(listLength)
    if (listLength == 1) and (int(list1[0]) ==0):
        return 0
    if (listLength == 1) and (int(list1[0]) == 1):
        return 0
    
    binaryGap = 0
    binGapCounter = 0    
    
    for i in range(listLength):
        #print(i)
        #print(int(list1[i]))
        if (int(list1[i]) == 0): 
            binGapCounter = binGapCounter +1
        if (int(list1[i]) == 1) and (binGapCounter >= 1):
            if binGapCounter > binaryGap:
                binaryGap = binGapCounter
            binGapCounter = 0
    
    return binaryGap

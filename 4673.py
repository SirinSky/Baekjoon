def selfNumber(num):
    num = str(num)
    result = int(num)
    for intNum in num:
        result += int(intNum)
    
    return result
    
        
        

numList = [True for a in range(0, 10001)]

for i in range(0, 10001):
    result = selfNumber(i)
    
    if(result <= 10000):
        numList[selfNumber(i)] = False
    
    
for i in range(0, 10001):
    if(numList[i]):
        print(i)

import sys
num = int(input())

result = num

for i in range(0, num):
    word = sys.stdin.readline().rstrip()
    groupChar = []
    
    prevWord = word[0]
    
    for w in word:
        if(prevWord != w):
            
            if(w in groupChar):
                result -= 1
                break
            
            else:
                groupChar.append(prevWord)
                prevWord = w
        
print(result)



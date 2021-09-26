import sys

def hanSoo(num):
    num = str(num)
    
    if(len(num) == 1 or len(num) == 2):
        return True
    
    difference = int(num[1]) - int(num[0])
    
    for i in range(0, len(num)):
        if(i == 0 or i == 1):
            continue
            
        else:
            if(int(num[i]) - int(num[i-1]) != difference):
                return False
            
            else:
                continue
    return True



endNum = int(sys.stdin.readline())

result = 0
for i in range(1, endNum + 1):
    if(hanSoo(i)):
        result += 1

print(result)

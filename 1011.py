def fly(n):
    sqrtN = int((n-1) ** (1/2))

    result = sqrtN * 2
    
    if(n > (sqrtN ** 2 + (sqrtN+1) ** 2) / 2):
        result += 1
        
    print(result)

n = int(input())

for i in range(n):
    a , b = map(int, input().split())
    fly(b - a)

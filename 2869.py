#달팽이는 나의 원쑤
#에스카고르로 만들어버리자

import math
a, b, v = map(int, input().split())

if(a >= v):
    print("1")
    
else:
    print(int(math.ceil((v - a) / (a - b) + 1)))

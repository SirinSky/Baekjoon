def thisIsMathBro():
    height = int(input()) + 1
    width = int(input()) + 1
    
    
    #아파트 리스트 생성
    aptList = [[0 for k in range(width)] for a in range(height)]
    
    aptList[0] = [i for i in range(1, width + 1)]
    
    for i in range(height):
        aptList[i][0] = 1
        
    for h in range(height):
        for w in range(width):
            if(h != 0):
                if(w != 0):
                    aptList[h][w] = aptList[h][w-1] + aptList[h-1][w]
            
    print(aptList[height - 1][width - 2])
    
    
n = int(input())

for i in range(n):
    thisIsMathBro()

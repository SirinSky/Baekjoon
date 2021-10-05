def delete_star(n, nList, num):
    
    tempXY = []
    
    for i in range(int(n / num)):
        
        temp = [j for j in range(int(num / 3 + (i*num)), int(num / 3 * 2 + (i*num)))]
        
        tempXY += temp
    
    for x in tempXY:
            for y in tempXY:
                nList[x][y] = ' '
                        

    if(num == 3):
        return 0
        
    else:
        delete_star(n, nList, num / 3)
    


n = int(input())

nList = [['*' for i in range(n)] for i in range(n)]

delete_star(n, nList, n)

for i in range(n):
    for j in range(n):
        
        print(nList[i][j] ,end='')
    
    print('')

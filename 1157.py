import sys

word = sys.stdin.readline().rstrip()

alpabet = [0 for i in range(0,26)]

for w in word:
    
    #소문자라면 대문자로 변환
    if(ord(w) >= 97):
        alpabet[ord(w) - 32 - 65] += 1
        
    else:
        alpabet[ord(w) -65] += 1

maxChar = max(alpabet)

max_list = []

for i in range(0, 26):
    if(alpabet[i] == maxChar):
        max_list.append(i + 65)

if(len(max_list) > 1):
    print("?")
    
else:
    print(chr(max_list[0]))
    

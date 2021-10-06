string = input()

prevChar = 'A'
count = 0

for char in string:
    if(char > prevChar):
        if(abs(ord(prevChar) + 26 - ord(char)) <= ord(char) - ord(prevChar)):
            count += abs(ord(prevChar) + 26 - ord(char))
            
        else:
            count += ord(char) - ord(prevChar)
            
    elif(char < prevChar):
        
        if(abs(ord(char) + 26 - ord(prevChar)) <= ord(prevChar) - ord(char)):
            count += abs(ord(char) + 26 - ord(prevChar))
        else:
            count += ord(prevChar) - ord(char)
        
    else:
        pass
    
    prevChar = char

print(count)

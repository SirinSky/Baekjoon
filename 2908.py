import sys
a, b = map(str, sys.stdin.readline().split())

a_reversed = ''
b_reversed = ''

for char in a:
    a_reversed = char + a_reversed
for char in b:
    b_reversed = char + b_reversed    
    
if int(a_reversed) >= int(b_reversed):
    print(a_reversed)

else:
    print(b_reversed)

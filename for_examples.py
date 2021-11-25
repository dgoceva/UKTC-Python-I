import sys

for x in range(1, 101):
    print(x)
print('\n'+50*'-')  # '\n' = new line character

for x in range(1, 1001):
    if x % 10 == 7:
        print(x, end=" ")
print('\n'+50*'-')

for ch in range(ord('a'), ord('z')+1):
    print(chr(ch), end=" ")
print('\n'+50*'-')

n = int(input('n='))
sum_n = 0
for x in range(n):  # range(0,n,2)
    num = int(input())
    sum_n += num
print('sum = ', sum_n)
print(50*'-')

x = 1
while x < 11:
    print(x, end=" ")
    x += 1
print('\n'+50*'-')

for x in range(1, 11):
    print(x, end=" ")
print('\n'+50*'-')

n = int(input('n='))
max_int = None
for x in range(n):
    num = int(input())
    if max_int is None:
        max_int = x
    elif max_int < num:
        max_int = num
print('max = ', max_int)
print(50*'-')

max_int = -sys.maxsize-1

for x in range(n):
    num = int(input())
    if max_int < num:
        max_int = num
print('max = ', max_int)
print(50*'-')

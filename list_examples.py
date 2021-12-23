import random

ll = []
for i in range(10):
    ll.append(i)
print(ll)

# ll = []
# for i in range(3):
#     ll.append(int(input('number: ')))
# print(ll)

ll = []
for i in range(10):
    ll.append(random.randint(-10, 100))
print(ll)

print(ll[2])
print(ll[2:8])
print(ll[5:])
print(ll[:6])
ll[3] = 101  # mutable
print(ll)
ll[1:3] = [3, 4, 5]
print(ll)
ll[3:5] = [7]
print(ll)
# del ll[:6]
# print(ll)
# del ll[:]
# print(ll)
# del ll
# print(ll)

# sum
sum1 = 0
for num in ll:
    sum1 += num  # sum = sum + num
print(sum1)

print(sum(ll, 0))

# sum by condition
sum1 = 0
for num in ll:
    if num % 2 == 0:
        sum1 += num
print(sum1)

# count by condition
cnt = 0
for num in ll:
    if num < 0:
        cnt += 1
print(cnt)

# min
minel = ll[0]
for num in ll:
    if num < minel:
        minel = num
print(minel)

print(min(ll))
print(max(ll))

# max by condition
init = False
for num in ll:
    if num % 2 != 0:
        if not init:
            init = True
            maxel = num
        elif num > maxel:
            maxel = num
if not init:
    print('No odd number...')
else:
    print(maxel)

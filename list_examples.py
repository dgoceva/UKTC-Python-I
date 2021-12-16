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

sum = 0
for num in ll:
    sum += num  # sum = sum + num
print(sum)

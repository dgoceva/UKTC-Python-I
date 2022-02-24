from wsgiref import validate


numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[3])
print(numbers[-4])
print(numbers[2:])
print(numbers[:])
print(numbers[1:3])
print(numbers[:4])
# numbers[1] = 44
# del numbers[1]
# numbers.append(33)
numbers = (11, 12, 13, 14, 15, 16, 17, 18, 19)
print(numbers)
del numbers
# print(numbers)

t1 = (21, 'a', 'b', 'c', 'd', 'e', 'Hello tuple!', 2.34)
print(t1)

for data in t1:
    print(data)

for i in range(0, len(t1), 2):
    print(t1[i])

t2 = tuple()
print(any(t2))
print(all(t2))

for i, v in enumerate(t1):
    print(i, '->', v)

t2 = (1, 2, 3, -1, -11, -3, 44)
print(len(t2))
print(max(t2))
print(min(t2))

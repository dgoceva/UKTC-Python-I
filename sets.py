s1 = set()
s2 = frozenset([1, 2, 3, 4])
print(s1, s2)
s1 = {1, 12, 3, 14, 15, 6, 17, 18, 19, 20}
print(s1)

print(len(s1), len(s2))

s2 = frozenset((1, 2, 3, 4, 5, 6))
print(s2)
s3 = {1, 3, 17}
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2.copy())
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1.isdisjoint(s3))
print(s3.issubset(s1))
print(s3 <= s1)
print(s1.issuperset(s1))
print(s1 >= s3)
print(s1.union(s2))
print(s1 | s2)
print(s1.intersection(s3))

s3.add(33)
print(s3)
s3.discard(1)
print(s3)
s3.discard(2)
print(s3)
s3.difference_update(s1)
print(s3)
s1.intersection_update(s2)
print(s1)
# s2.intersection_update(s3)
s3.symmetric_difference_update(s2)
print(s3)
s3.update(s2)
print(s3)
print(s3.pop())
print(s3)
s3.remove(4)
# s3.remove(-1)
print(s3)

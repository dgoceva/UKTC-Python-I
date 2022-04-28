def cube(x):
    return x*x*x


def input_list():
    ll = []
    for x in range(3):
        ll.append(int(input()))
    return ll


def my_min(ll):
    minel = ll[0]
    for x in ll:
        if minel > x:
            minel = x
    return minel


def is_palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False


def square(a):
    return a*a


x = int(input('x='))
print(cube(x))
print(input_list())

ll = [int(x) for x in input().split(',')]
print(ll)

print([x for x in range(10)])


print(my_min(ll))
print(min(ll))

print(is_palindrome('121'))
print(is_palindrome('124'))

print(square(5))

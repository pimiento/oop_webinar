class A:
    x = 10
    _y = 20
    __z = 30

a = A()
print(a.x)   # -> 10
print(a._y)  # -> 20
try:
    a.__z # -> ERROR!
except AttributeError as e:
    print(e)
print(a._A__z)
a._A__z = 0
print(a._A__z)

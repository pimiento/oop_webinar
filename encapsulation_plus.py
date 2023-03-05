class A:
    x = 10
    _y = 20
    __z = 30
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, val):
        if value < 0:
            raise ValueError(f"{val}<0")
        self.__z = valuelP
        return value

a = A()
print(a.x)   # -> 10
print(a._y)  # -> 20
print(a.z)   # -> ???
a.z = 0
print(a.z)   # -> ???

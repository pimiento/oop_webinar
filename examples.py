from dataclasses import dataclass
from typing import ClassVar

def birthday(cat):
    cat["age"] += 1

cat_type = {
    "init": add_cat,
    "name": None,
    "color": None,
    "age": None,
    "birthday": birthday
}


cats = []
cats.append(cat_type.copy())
cats[0]["name"] = "Барсик"
cats[0]["color"] = "рыжий"
cats[0]["age"] = 3


def add_cat(cats, params):
    cats.append(cat_type.copy())
    cats[-1].update(params)

birthday(cats[0])

@dataclass
class Animal(object):
    sound: ClassVar[str] = None
    color: str
    age: float

    def voice(self):  # self == a_cat
        print(self.sound)

@dataclass
class Cat(Animal):
    tail_state: ClassVar[str] = "puffed up"
    __sleep_counter: ClassVar[float] = 0
    name: str

    def birthday(self, months=None):
        if months is None:
            self.age += 1
        else:
            self.age += months/12

    def sleep(self, hours):
        self.__sleep_counter += hours
        self.__sleep_counter %= 24

    @property
    def sleep_counter(self):
        return self.__sleep_counter

    def __repr__(self):
        return f"{self.name} {self.color} {self.age}"

@dataclass
class Bird(Animal):
    can_fly: bool

a_cat = Cat("рыжик", "рыжий", 4)
a_cat2 = Cat("Вася", "чёрный", 3)
Cat.tail_state = "down"


class A:
    def function(self):
        print("— Я твой отец, Люк!")

class B(A):
    def function(self):
        print("— Я Люк!")
        super().function()

"""
KISS — Keep It Simple Stupid (оставь это простым, дубина)
DRY — Don't Repeat Yourself (не повторяй самого себя)
Работает не трожь!
"""

class AbstractAnimal:
    def sound(self):
        raise NotImplementedError

def what_is_it(self: AbstractAnimal):
    return f"{self.__class__.__name__} {self.color} {self.age}"


class X:
    var = 1

    @classmethod
    def foo(cls):
        print(cls)

class YMixin:

    @staticmethod
    def bar():
        return "Bar"

class Z(X, YMixin):
    def foobar(self):
        return self.var

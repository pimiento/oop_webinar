- [Класс](#org3c3cd5f)
- [Объект](#orge7ec5ee)
- [Объект](#org9982520)
- [Метод](#org8332b04)
- [Атрибут](#org0b7cb8f)
- [Атрибут класса](#org39627f4)
- [self](#org0a838ce)
- [self](#org0adcecc)
- [Инициализация](#org2b019fc)
- [Инициализация](#orgc1d2bf1)
- [@dataclass](#orga4108fe)
- [@dataclass](#orga962354)
- [@dataclass](#org88a5eac)
- [Наследование](#org35b84e5)
- [Наследование по-простому](#orgee63ee7)
- [super](#orgdf4df9a)
- [super](#org853a421)
- [Полиморфизм](#org1515ef2)
- [Инкапсуляция](#org3a07516)
- [Инкапсуляция](#org3b27c22)
- [Инкапсуляция](#orgd161705)
- [setter / getter](#org134a308)
- [setter/getter](#org62f5994)
- [Статические методы](#org65cd4e9)
- [Статические методы](#orgf549ad9)
- [В Python всё есть объект](#orga0aacea)
- [Дополнительная литература](#orgb983eb4)
- [Вопросы-ответы](#orgda065f5)



<a id="org3c3cd5f"></a>

# Класс

```python
class Animal(object):
    ...

class Cat(Animal):
    ...
```

![img](class_example.png)  


<a id="orge7ec5ee"></a>

# Объект

```python
a_cat = Cat(type="египетский")
```

![img](cat_object.png)  


<a id="org9982520"></a>

# Объект

```python
a_cat = Cat(type="кроличий")
```

![img](cat.jpg)  


<a id="org8332b04"></a>

# Метод

```python
class Cat(Animal):
    ...
    def sleep(self, period):
        self.activity = None
        time.sleep(period)
```

![img](cat_sleeping.jpeg)  


<a id="org0b7cb8f"></a>

# Атрибут

```python
class Cat(Animal):
    tail_state = 'puffed up'
    ...
```

![img](cat_tail.jpg)  


<a id="org39627f4"></a>

# Атрибут класса

Так мы говорим, что у всех кошек на Земле хвост задран  

```python
class Cat(Animal):
    tail_state = 'puffed up'
    ...
```

А так только у какой-то конкретной кошки (у конкретного экземпляра объекта класса *Cat*)  

```python
class Cat(Animal):
    def __init__(self):
        self.tail_state = 'puffed up'
    ...
```


<a id="org0a838ce"></a>

# self

-   **self:** это указать на конкретный экземпляр объекта класса.

![img](cats.png)  


<a id="org0adcecc"></a>

# self

```python
class Cat(Animal):
    def meow(self):
        print('Meow')

cat_1 = Cat()
cat_2 = Cat()
cat_3 = Cat()
cat_1.meow()
# Кто сказал "мяу"?
```


<a id="org2b019fc"></a>

# Инициализация

```python
class Cat(Animal):
  def __init__(self,
               age,
               breed,
               color_schema,
               tail_state,
               is_domestic=False,
               family=None):
      self.age = age
      self.breed = breed
      self.color_schema = color_schema
      self.tail_state = tail_state,
      self.is_domestic = is_domestic
      self.family = family
```


<a id="orgc1d2bf1"></a>

# Инициализация

```python
def take_cat(self, family):
  if is_domestic:
      raise Exception(
        'Это домашняя кошка!'
        ' Её нельзя забрать!'
      )
  self.is_domestic = True
  self.family = family
```


<a id="orga4108fe"></a>

# @dataclass

<span class="underline"><span class="underline">[документация](https://docs.python.org/3.8/library/dataclasses.html)</span></span>  

```python
from dataclasses import dataclass

@dataclass
class Cat(Animal):
    age: int
    breed: str
    color_schema: int
    tail_state: int
    is_domestic: bool = False
    family: object = None
```


<a id="orga962354"></a>

# @dataclass

<span class="underline"><span class="underline">[документация](https://docs.python.org/3.8/library/dataclasses.html)</span></span>  

```python
class Cat(Animal):
  def __init__(
    self, age: int, breed: str,
    color_schema: int, tail_state: int,
    is_domestic: bool=False,
    family: object=None
  ):
    self.age = age
    self.breed = breed
    self.color_schema = color_schema
    self.tail_state = tail_state,
    self.is_domestic = is_domestic
    self.family = family
```


<a id="org88a5eac"></a>

# @dataclass

```python
@dataclasses.dataclass(
    *, init=True, repr=True, eq=True,
    order=False, unsafe_hash=False,
    frozen=False
)
```


<a id="org35b84e5"></a>

# Наследование

```python
class Animal:
    def say(self):
        raise NotImplementedError()

class Cat(Animal):
    def say(self):
        print('meow!')

class Dog(Animal):
    def barking(self):
        # что произойдёт?
        return self.say()
```


<a id="orgee63ee7"></a>

# Наследование по-простому

Наследование это всего лишь порядок, по которому будет идти поиск атрибутов и методов.  

```python
# class A(object):
class A:
    attr = 10
    def method(self):
        print("method")

class B(A):
    attr = 20
    def function(self):
        print("function")
```


<a id="orgdf4df9a"></a>

# super

$super()$ возвращает объект родителя, чтобы мы могли запросить нужный нам метод/атрибут у родителя  

```python
class B(A):
    def function(self):
        super().method()
        (
            self.__class__
            .__bases__[0]
            .method(self)
        )
        print("function")
```


<a id="org853a421"></a>

# super

```python
b = B()
b.function()
```

    method
    method
    function


<a id="org1515ef2"></a>

# Полиморфизм

```python
def listen_to_animal(animal: Animal):
    animal.say()

a_cat = Cat()
a_dog = Dog()
listen_to_animal(a_cat)
listen_to_animal(a_dog)
```


<a id="org3a07516"></a>

# Инкапсуляция

-   переменные и методы с одним подчёркиванием **\_name** программисты договорились считать внутренними переменными
-   переменные и методы с двойным подчёркиванием **\_ \_name** Python прячет особым образом (но к ним всё ещё можно получить доступ)


<a id="org3b27c22"></a>

# Инкапсуляция

```python
class A:
    x = 10
    _y = 20
    __z = 30

a = A()
print(a.x)    # -> 10
print(a._y)   # -> 20
print(a.__z)  # -> ???
```


<a id="orgd161705"></a>

# Инкапсуляция

```python


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
```


<a id="org134a308"></a>

# setter / getter

```python
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
```


<a id="org62f5994"></a>

# setter/getter

```python


a = A()
print(a.x)   # -> 10
print(a._y)  # -> 20
print(a.z)   # -> ???
a.z = 0
print(a.z)   # -> ???
```


<a id="org65cd4e9"></a>

# Статические методы

Не требуют указания текущего объекта вызова  

```python
class Cat:

    @staticmethod
    def say():
        print("meow")

class AnotherCat:
    pass

def say():
    print("meow")
```


<a id="orgf549ad9"></a>

# Статические методы

```python
AnotherCat.say = staticmethod(say)
cat_1 = Cat()
cat_2 = AnotherCat()
cat_1.say()
cat_2.say()
```


<a id="orga0aacea"></a>

# В Python всё есть объект

```python
a = 10
print(a.bit_length())

def func(x, y):
    return x + y

f = func
print(f.__name__)
```

    4
    func


<a id="orgb983eb4"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[Object Oriented Programming in Python](https://python-scripts.com/object-oriented-programming-in-python)</span></span>
-   <span class="underline"><span class="underline">[Основы ООП. Классы, объекты, методы](https://pythonchik.ru/osnovy/osnovy-oop-v-python-klassy-obekty-metody)</span></span>
-   <span class="underline"><span class="underline">[wikibook](https://ru.wikibooks.org/wiki/Python/%25D0%259E%25D0%25B1%25D1%258A%25D0%25B5%25D0%25BA%25D1%2582%25D0%25BD%25D0%25BE-%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D0%25BE%25D0%25B5_%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5_%25D0%25BD%25D0%25B0_Python)</span></span>
-   Марк Лутц. «Изучаем Python»

![img](lutz.png)  


<a id="orgda065f5"></a>

# Вопросы-ответы

![img](questions.jpg)

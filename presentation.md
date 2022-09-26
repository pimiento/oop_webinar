- [Класс](#org386627e)
- [Объект](#orgd40f3f1)
- [Объект](#org68f3c2c)
- [Метод](#orgeebc6f1)
- [Атрибут](#org885e395)
- [Атрибут класса](#org45f713a)
- [self](#orgf9b4db4)
- [self](#org03b3e02)
- [Инициализация](#org26bf28e)
- [Инициализация](#org76ca137)
- [@dataclass](#org2c32bc8)
- [@dataclass](#org2d28a78)
- [@dataclass](#orgc658fd2)
- [Наследование](#org8a66d4a)
- [Наследование по-простому](#org7580190)
- [super](#orgc1ca2a5)
- [super](#org5219b71)
- [Полиморфизм](#orgab61349)
- [Инкапсуляция](#orgb937eca)
- [Инкапсуляция](#org74bbfdb)
- [Статические методы](#org519c7b9)
- [Статические методы](#orgefa1f0f)
- [В Python всё есть объект](#org3a76047)
- [Дополнительная литература](#orga279ddf)
- [Вопросы-ответы](#org0856552)



<a id="org386627e"></a>

# Класс

```python
class Animal(object):
    ...

class Cat(Animal):
    ...
```

![img](class_example.png)  


<a id="orgd40f3f1"></a>

# Объект

```python
a_cat = Cat(type="египетский")
```

![img](cat_object.png)  


<a id="org68f3c2c"></a>

# Объект

```python
a_cat = Cat(type="кроличий")
```

![img](cat.jpg)  


<a id="orgeebc6f1"></a>

# Метод

```python
class Cat(Animal):
    ...
    def sleep(self, period):
        self.activity = None
        time.sleep(period)
```

![img](cat_sleeping.jpeg)  


<a id="org885e395"></a>

# Атрибут

```python
class Cat(Animal):
    tail_state = 'puffed up'
    ...
```

![img](cat_tail.jpg)  


<a id="org45f713a"></a>

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


<a id="orgf9b4db4"></a>

# self

-   **self:** это указать на конкретный экземпляр объекта класса.

![img](cats.png)  


<a id="org03b3e02"></a>

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


<a id="org26bf28e"></a>

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


<a id="org76ca137"></a>

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


<a id="org2c32bc8"></a>

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


<a id="org2d28a78"></a>

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


<a id="orgc658fd2"></a>

# @dataclass

```python
@dataclasses.dataclass(
    *, init=True, repr=True, eq=True,
    order=False, unsafe_hash=False,
    frozen=False
)
```


<a id="org8a66d4a"></a>

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


<a id="org7580190"></a>

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


<a id="orgc1ca2a5"></a>

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


<a id="org5219b71"></a>

# super

```python
b = B()
b.function()
```

    method
    method
    function


<a id="orgab61349"></a>

# Полиморфизм

```python
def listen_to_animal(animal: Animal):
    animal.say()

a_cat = Cat()
a_dog = Dog()
listen_to_animal(a_cat)
listen_to_animal(a_dog)
```


<a id="orgb937eca"></a>

# Инкапсуляция

-   переменные и методы с одним подчёркиванием **\_name** программисты договорились считать внутренними переменными
-   переменные и методы с двойным подчёркиванием **\_ \_name** Python прячет особым образом (но к ним всё ещё можно получить доступ)


<a id="org74bbfdb"></a>

# Инкапсуляция

```python
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
```


<a id="org519c7b9"></a>

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


<a id="orgefa1f0f"></a>

# Статические методы

```python
AnotherCat.say = staticmethod(say)
cat_1 = Cat()
cat_2 = AnotherCat()
cat_1.say()
cat_2.say()
```


<a id="org3a76047"></a>

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


<a id="orga279ddf"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[Object Oriented Programming in Python](https://python-scripts.com/object-oriented-programming-in-python)</span></span>
-   <span class="underline"><span class="underline">[Основы ООП. Классы, объекты, методы](https://pythonchik.ru/osnovy/osnovy-oop-v-python-klassy-obekty-metody)</span></span>
-   <span class="underline"><span class="underline">[wikibook](https://ru.wikibooks.org/wiki/Python/%25D0%259E%25D0%25B1%25D1%258A%25D0%25B5%25D0%25BA%25D1%2582%25D0%25BD%25D0%25BE-%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D0%25BE%25D0%25B5_%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5_%25D0%25BD%25D0%25B0_Python)</span></span>
-   Марк Лутц. «Изучаем Python»

![img](lutz.png)  


<a id="org0856552"></a>

# Вопросы-ответы

![img](questions.jpg)

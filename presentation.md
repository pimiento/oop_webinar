- [Класс](#orgb205e8f)
- [Объект](#org0d376ac)
- [Объект](#org2840fa4)
- [Метод](#org68ccdba)
- [Атрибут](#orgc623143)
- [Атрибут класса](#org7603a8b)
- [self](#org6f12038)
- [self](#orge487961)
- [Инициализация](#orgc50b48a)
- [Инициализация](#org3c1aad9)
- [Наследование](#org094b360)
- [Полиморфизм](#orgdbcc011)
- [Инкапсуляция](#org5f733f7)
- [Инкапсуляция](#org91ffecf)
- [Статические методы](#orgfcda6f3)
- [Статические методы](#org354d311)
- [В Python всё есть объект](#org633e043)
- [Методы класса](#orgbe8f091)
- [Дополнительная литература](#org81c6b89)
- [Вопросы-ответы](#org643b548)



<a id="orgb205e8f"></a>

# Класс

```python
class Animal(object):
    ...

class Cat(Animal):
    ...
```

![img](class_example.png)


<a id="org0d376ac"></a>

# Объект

```python
a_cat = Cat(type="египетский")
```

![img](cat_object.png)


<a id="org2840fa4"></a>

# Объект

```python
a_cat = Cat(type="кроличий")
```

![img](cat.jpg)


<a id="org68ccdba"></a>

# Метод

```python
class Cat(Animal):
    ...
    def sleep(self, period):
        self.activity = None
        time.sleep(period)
```

![img](cat_sleeping.jpeg)


<a id="orgc623143"></a>

# Атрибут

```python
class Cat(Animal):
    tail_state = 'puffed up'
    ...
```

![img](cat_tail.jpg)


<a id="org7603a8b"></a>

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


<a id="org6f12038"></a>

# self

-   **self:** это указать на конкретный экземпляр объекта класса.

![img](cats.png)


<a id="orge487961"></a>

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


<a id="orgc50b48a"></a>

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


<a id="org3c1aad9"></a>

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


<a id="org094b360"></a>

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


<a id="orgdbcc011"></a>

# Полиморфизм

```python
def listen_to_animal(animal: Animal):
    animal.say()

a_cat = Cat()
a_dog = Dog()
listen_to_animal(a_cat)
listen_to_animal(a_dog)
```


<a id="org5f733f7"></a>

# Инкапсуляция

-   переменные и методы с одним подчёркиванием **\_name** программисты договорились считать внутренними переменными
-   переменные и методы с двойным подчёркиванием **\_ \_name** Python прячет особым образом (но к ним всё ещё можно получить доступ)


<a id="org91ffecf"></a>

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


<a id="orgfcda6f3"></a>

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


<a id="org354d311"></a>

# Статические методы

```python
AnotherCat.say = staticmethod(say)
cat_1 = Cat()
cat_2 = AnotherCat()
cat_1.say()
cat_2.say()
```


<a id="org633e043"></a>

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


<a id="orgbe8f091"></a>

# Методы класса

```python
class Animal:
    @classmethod
    def what_says(cls):
        print(
          f"{cls.__name__} "
          "says {cls.say()}"
        )

class Cat(Animal):
    @staticmethod
    def say():
        return "meow"

Cat.what_says()
```

    Cat says {cls.say()}


<a id="org81c6b89"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[Object Oriented Programming in Python](https://python-scripts.com/object-oriented-programming-in-python)</span></span>
-   <span class="underline"><span class="underline">[Основы ООП. Классы, объекты, методы](https://pythonchik.ru/osnovy/osnovy-oop-v-python-klassy-obekty-metody)</span></span>
-   <span class="underline"><span class="underline">[wikibook](https://ru.wikibooks.org/wiki/Python/%25D0%259E%25D0%25B1%25D1%258A%25D0%25B5%25D0%25BA%25D1%2582%25D0%25BD%25D0%25BE-%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D0%25BE%25D0%25B5_%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5_%25D0%25BD%25D0%25B0_Python)</span></span>
-   Марк Лутц. «Изучаем Python»

![img](lutz.png)


<a id="org643b548"></a>

# Вопросы-ответы

![img](questions.jpg)

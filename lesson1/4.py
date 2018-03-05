#!/usr/bin/python3

# Написать программу, симулирующую семью. В семье должно быть от 2 до 5 детей.
# Мама и папа. В выводе члены семьи должны называть свое имя, пол и возраст

from abc import ABCMeta, abstractmethod, abstractproperty


class FamilyAble(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # Имя
    def get_name(self):
        return self.name

    # Возраст
    def get_age(self):
        return self.age

    # Пол
    def get_sex(self):
        return self.sex

    @abstractmethod
    def __str__(self):
        pass


class Father(FamilyAble):
    def __init__(self, name, age):
        super().__init__(name, age, 'мужчина')

    def __str__(self):
        return "Я папа, мне {} лет и моё имя {}".format(self.get_age(), self.get_name())


class Mother(FamilyAble):
    def __init__(self, name, age):
        super().__init__(name, age, 'женщина')

    def __str__(self):
        return "Я мама, мне {} лет и моё имя {}".format(self.get_age(), self.get_name())


class Child(FamilyAble):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def __str__(self):
        return "Я ребенок, мне {} лет и моё имя {}, а ещё я {}".format(self.get_age(), self.get_name(), self.get_sex())


father = Father('Николай', 45)
print(father)
mother = Mother('Валерия', 45)
print(mother)
child1 = Child('Илья', 15, 'мальчик')
child2 = Child('Ксения', 13, 'девочка')
print(child1)
print(child2)

from typing import Protocol


class Animal(Protocol):
    def make_sound(self) -> None:
        ...

# 无需显式地继承。这种方式称为鸭子类型（Duck Typing）。


class Dog:
    def make_sound(self) -> None:
        print("Woof! Woof!")


class Cat:
    def make_sound(self) -> None:
        print("Meow")


class Duck:
    def make_sound(self) -> None:
        print("Quack")


class Cow:
    def make_sound(self) -> None:
        print("Moo")


def animal_sound(animal: Animal) -> None:
    animal.make_sound()


dog = Dog()
cat = Cat()

animal_sound(dog)  # 输出: Woof! Woof!
animal_sound(cat)  # 输出: Meow

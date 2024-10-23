from abc import ABC, abstractmethod

#Exercice 1
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def area(self):
        return self.longueur * self.largeur

class Circle(Shape):
    def __init__(self, rayon):
        self.rayon = rayon
    def area(self):
        return 3.14 * self.rayon**2

#Exercice 2
class BankAccount :
    def __init__(self, solde_initial):
        self.balance = solde_initial
    def __add__(self, montant_ajouté):
        self.balance += montant_ajouté
        return self
    def __sub__(self, montant_retrait):
        self.balance-= montant_retrait
        return self

#Exercice 5
class AgeError(Exception):
    pass
class Person :
    def __init__(self, nom, age):
        if age < 0 or age > 150:
            raise AgeError("Age non valide")
        self.name = nom
        self.age = age


#Exercice 10
class Animal (ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
class AnimalFactory:
    @staticmethod
    def create(animal_type, name):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()

#Exercice 11
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
    def __ne__(self, other):
        return self.price != other.price

#Exercice 12
class Account:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Le dépôt initial ne peut pas être négatif.")
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être négatif.")
        self._balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le dépôt ne peut pas être négatif.")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Le retrait ne peut pas être négatif.")
        if self._balance < amount:
            raise ValueError("Solde insuffisant.")
        self._balance -= amount

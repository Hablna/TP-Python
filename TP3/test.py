import pytest
from reponse import *

# Exercice 1: Classe Abstraite Simple
def test_exercise_1():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    assert pytest.approx(circle.area(), 0.01) == 78.54
    assert rectangle.area() == 24
    with pytest.raises(TypeError):
        Shape()


# Exercice 2: Surcharge d'Opérateurs
def test_exercise_2():
    account = BankAccount(100)
    account = account + 50
    assert account.balance == 150
    account = account - 30
    assert account.balance == 120


# Exercice 3: Décorateurs
def test_exercise_3():
    assert check_positive(4) == 8
    with pytest.raises(ValueError):
        check_positive(-5)


# Exercice 4: Propriétés (Property)
def test_exercise_4():
    car = Car()
    car.speed = 150
    assert car.speed == 150
    with pytest.raises(ValueError):
        car.speed = 250
    with pytest.raises(ValueError):
        car.speed = 0


# Exercice 5: Gestion des Exceptions
def test_exercise_5():
    person = Person("John", 30)
    assert person.name == "John"
    assert person.age == 30
    with pytest.raises(AgeError):
        Person("Jane", 160)


# Exercice 6: Singleton et Context Manager
def test_exercise_6():
    db = DatabaseConnection()
    with DbContext(db) as context:
        context.add_entry({"id": 1, "data": "Test"})
        context.add_entry({"id": 2, "data": "Another"})
    assert db.entries == [{"id": 1, "data": "Test"}, {"id": 2, "data": "Another"}]
    db.remove_by_id(1)
    assert db.entries == [{"id": 2, "data": "Another"}]
    db.drop_all()
    assert db.entries == []


# Exercice 7: Factory Pattern
def test_exercise_7():
    circle = ShapeFactory.create(shape="circle", radius=5)
    assert pytest.approx(circle.area(), 0.01) == 78.54
    rectangle = ShapeFactory.create(shape="rectangle", width=4, height=6)
    assert rectangle.area() == 24


# Exercice 8: Décorateurs avec Paramètres
def test_exercise_8():
    with pytest.raises(TimeoutError):
        timeout_limit(10)

    with pytest.raises(TimeoutError):
        timeout_limit(10, raise_exception=True)


# Exercice 9: Opérateurs Avancés (Matrice)
def test_exercise_9():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6], [7, 8]])
    result_add = mat1 + mat2
    result_mult = mat1 * mat2
    assert result_add.values == [[6, 8], [10, 12]]
    assert result_mult.values == [[19, 22], [43, 50]]


# Exercice 10: Classes Abstraites et Factory (Animal)
def test_exercise_10():
    dog = AnimalFactory.create(animal_type="dog", name="Buddy")
    cat = AnimalFactory.create(animal_type="cat", name="Whiskers")
    assert dog.name == "Buddy"
    assert dog.speak() == "Woof"
    assert cat.name == "Whiskers"
    assert cat.speak() == "Meow"


# Exercice 11: Surcharge d'Opérateurs (Comparaison)
def test_exercise_11():
    p1 = Product("Laptop", 1000)
    p2 = Product("Phone", 800)
    assert p1 > p2
    assert p2 < p1
    assert p1 != p2

def test_exercise_11_bonus():
    p1 = Product("Laptop", 1000)
    p2 = Product("Phone", 800)
    p3 = Product("Tablet", 600)
    products = [p1, p2, p3]
    top_products = top_product(products, 2)
    assert top_products == [p1, p2]


# Exercice 12: Propriétés et Gestion d’Exceptions (Compte)
def test_exercise_12():
    account = Account(500)
    account.deposit(100)
    assert account.balance == 600
    with pytest.raises(ValueError):
        account.deposit(-50)
    account.withdraw(200)
    assert account.balance == 400
    with pytest.raises(ValueError):
        account.withdraw(1000)


# Exercice 14: Surcharge d'Opérateurs (Vecteur)
def test_exercise_14():
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    assert v3.x == 6 and v3.y == 8
    v4 = v1 - v2
    assert v4.x == -2 and v4.y == -2
    v5 = v1 * 3
    assert v5.x == 6 and v5.y == 9


# Exercice 15: Mock et Monkey-Patch
def test_exercise_15():
    def original_function():
        return "Original"

    with patch(original_function, return_value="Mocked"):
        assert original_function() == "Mocked"

    assert original_function() == "Original"


# Exercice 16: Classes Génériques et Méthodes Statistiques
def test_exercise_16():
    stats = Statistics([10, 20, 30, 40])
    assert stats.mean() == mean([10, 20, 30, 40])
    assert stats.median() == median([10, 20, 30, 40])
    assert pytest.approx(stats.variance(), 0.01) == variance([10, 20, 30, 40])


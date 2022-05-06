# добавить 2-3 магических методов
# вариант 5 - Cars.

class Car:
    pass
    def __init__(self, id, brand, model, year, color, price, registrationNumber):
        """Описание автомобиля"""
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.registrationNumber = registrationNumber

        # __repr__ - текстовое отображение объекта внутри системы
    def __repr__(self):
        return f"The object Car - {self.id} {self.brand} {self.model} {self.year} {self.color} {self.price} {self.registrationNumber} "

        # __str__ - как увидит объект пользователь, если к нему применить функцию str или print
    def __str__(self):
        return f"The best Car - {self.id} {self.brand} {self.model} {self.year} {self.color} {self.price} {self.registrationNumber} "

        # __eq__ - магический метод для оператора сравнения
    def __eq__(self, other):
        if not isinstance(other, (int, Car)):
            raise TypeError("Операнд справада должен иметь тип int или Car")

        test = other if isinstance(other, int) else other.year
        return self.year == test

car_1 = Car ('1', 'BMW', 'X5', '2020', 'Blue', '20000', '1234-АВ7')
car_2 = Car ('2','Audi', 'A4', '2019', 'Red', '25000','1235-АC5')
print(car_1)
print(car_1 == car_2)







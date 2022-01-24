# Вариант 5
# Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер

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
        self.mileage = 0

    def getFullName(self):
        """Автомобиль"""
        name = f"Автомобиль {self.id} {self.brand} {self.model} {self.year} {self.color} {self.price} {self.registrationNumber} "
        return name.title()

    def getDiscount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.id} {self.brand} {self.model} {self.year} {self.color} {self.price} {self.registrationNumber} скидка 5%")

    def getReadMileage(self):
        """Пробег автомобиля"""
        print(f"Пробег автомобиля {self.mileage} км.")

car_1 = Car('1', 'BMW', 'X5', '2020', 'Blue', '20000','1234-АВ7')
car_1.getDiscount()

car_2 = Car('2','Audi', 'A4', '2019', 'Red', '25000','1235-АC5')
print(car_2.getFullName())
car_2.getReadMileage()

class ElectricCar(Car):
    """Описывает электромобиль"""
    def __init__(self, id, brand, model, year, color, price, registrationNumber):
        """Инициализирует атрибуты класса родителя"""
        super().__init__( id, brand, model, year, color, price, registrationNumber)
        # атрибут класса-потомка
        self.battery_size = 100

    def getBatteryPower(self):
        """Выводит мощность аккумулятора авто"""
        print(f"Мощность аккумулятора {self.battery_size} кВт⋅ч")

    def getFullName(self):
        """Автомобиль"""
        name = f"Автомобиль {self.id} {self.brand} {self.model} {self.year} {self.color} {self.price} {self.registrationNumber} {self.battery_size}-кВт⋅ч "
        return name.title()

tesla_1 = ElectricCar('3', 'tesla', 'model x', '2021', 'Black', '45000','1235-АC5')
print(tesla_1.getFullName())
tesla_1.getBatteryPower()
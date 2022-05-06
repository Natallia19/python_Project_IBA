
class Car:
    cars = []
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

# метод класса для вывода цены авто
    @classmethod
    def print_list_color(cls, color: str):
        print(f"Список автомобилей по выбранному цвету: \n")
        for car in cls.cars:
            if car.color == color:
                print(f"{car.id} {car.brand} {car.model} {car.year} {car.color} {car.price} {car.registrationNumber}")

Car(1, 'BMW', 'auris', 2017, 'red', 12000, '1789-АX5')
Car(2, 'Audi', 'cx-5', 2020, 'black', 22000, '1234-АВ7')
Car(3, 'Toyota', 'Corolla', 2018, 'red', 21000, '1234-АВ7')
Car(4, 'Mazda', 'cx-5', 2018, 'white', 21000, '1234-АВ7')
Car(5, "KIA", "Camry ", 2016, "green", 14000, "1234-АВ7")
Car(6, "BMW", "cx-5", 2015, "blue", 16000, "1234-АВ7")
Car(7, "BMW", "Highlander", 2020, "blue", 28000, "1234-АВ7")
Car(8, "BMW", "cx-5", 2020, "grey", 22000, "1234-АВ7")
Car(9, "toyota", "RAV4", 2019, "black", 22000, "1234-АВ7")
Car(10, "mazda", "cx-5", 2017, "blue", 18000, "1234-АВ7")
Car(11, "toyota", "Land Cruiser Prado", 2019, "black", 30000,"1234-АВ7")
Car(12, "mazda", "cx-5", 2019, "white", 20000, "1234-АВ7")

Car.print_list_color('red')

car_1 = Car('1', 'BMW', 'X5', '2020', 'Blue', '20000','1234-АВ7')
car_1.getFullName()
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


def print_list_color():
    return "red"
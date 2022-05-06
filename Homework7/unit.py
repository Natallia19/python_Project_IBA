import unittest
import Car
import Homework7.Car


class TestCar(unittest.TestCase):
    """Тест для класса Car"""

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up for a test")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after a test")

    def test_get_full_name(self):
        """Проверяет правильность получения полного имени"""
        car_1 = Car('1', 'BMW', 'X5', '2020', 'Blue', '20000','1234-АВ7')
        self.assertEqual(Homework7.Car.car_1.get_full_name(), 'Автомобиль 1 BMW X5 2020 Blue 20000 1234-АВ7')

    def test_print_сolor(self):
        self.assertEqual(Homework7.Car.print_list_color('green'))

if __name__ == '__main__':
    unittest.main()
import unittest
from descriptors import Food, CalorieDescriptor, Car, SpeedLimitDescriptor, Price, RubToUsdConverter

class TestCalorieDescriptor(unittest.TestCase):
    def setUp(self):
        self.apple = Food("Apple", 52)
        self.banana = Food("Banana", 89)

    def test_set_calories(self):
        self.assertEqual(self.apple.calories, 52)

        self.apple.calories = 60
        self.assertEqual(self.apple.calories, 60)

    def test_set_negative_calories(self):
        with self.assertRaises(ValueError):
            self.apple.calories = -10

    def test_total_calories(self):
        total_calories = self.apple.calories + self.banana.calories
        self.assertEqual(total_calories, 141)


class TestSpeedLimitDescriptor(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_set_speed_within_limit(self):
        self.car.speed = 80
        self.assertEqual(self.car.speed, 80)

    def test_set_speed_above_limit(self):
        self.car.speed = 150
        self.assertEqual(self.car.speed, 120)

    def test_set_negative_speed(self):
        with self.assertRaises(ValueError):
            self.car.speed = -10

    def test_accelerate_within_limit(self):
        self.car.accelerate(50)
        self.assertEqual(self.car.speed, 50)

    def test_accelerate_above_limit(self):
        self.car.accelerate(150)
        self.assertEqual(self.car.speed, 120)

    def test_brake_within_limit(self):
        self.car.speed = 80
        self.car.brake(30)
        self.assertEqual(self.car.speed, 50)

    def test_brake_below_zero(self):
        self.car.speed = 30
        self.car.brake(40)
        self.assertEqual(self.car.speed, 0)


class TestRubToUsdConverter(unittest.TestCase):
    def setUp(self):
        self.price = Price(1400)

    def test_initial_conversion(self):
        self.assertEqual(self.price.usd, 20.0)

    def test_setting_usd(self):
        self.price.usd = 30
        self.assertEqual(self.price.rub_amount, 2100)


if __name__ == '__main__':
    unittest.main()


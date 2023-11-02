class RubToUsdConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def __get__(self, instance, owner):
        return instance.rub_amount / self.exchange_rate

    def __set__(self, instance, value):
        instance.rub_amount = value * self.exchange_rate


class Price:
    def __init__(self, rub_amount):
        self.rub_amount = rub_amount

    usd = RubToUsdConverter(70)


class SpeedLimitDescriptor:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __get__(self, instance, owner):
        return instance._speed

    def __set__(self, instance, value):
        if value < 0:
            instance._speed = 0
        elif value > self.max_speed:
            instance._speed = self.max_speed
        else:
            instance._speed = value


class Car:
    speed = SpeedLimitDescriptor(max_speed=120)

    def __init__(self):
        self._speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount


class CalorieDescriptor:
    def __get__(self, instance, owner):
        return instance._calories

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Calories cannot be negative")
        instance._calories = value


class Food:
    calories = CalorieDescriptor()

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name} - {self.calories} calories"

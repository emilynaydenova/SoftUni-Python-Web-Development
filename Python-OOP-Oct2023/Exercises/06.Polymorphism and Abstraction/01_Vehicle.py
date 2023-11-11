from abc import ABC, abstractmethod


# задължава подкласовете да имат всички необходими методи иначе:
# TypeError: Can't instantiate abstract class Car with
# abstract methods refuel
class Vehicle(ABC):
    # да има поне 1 абстр.метод
    @abstractmethod
    def drive(self, distance):
        pass
        # if there is no @abstractmethod
        # raise NotImplementedError

    @abstractmethod
    def refuel(self, fuel):
        pass


# abstract class can't be instantiated


class Car(Vehicle):  # наследява абстрактен клас
    # must have all abstract methods in parent abstract class
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 0.9) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 1.6) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


# car = Car(50, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# # 32.3
# # 14.599999999999994
# # 24.599999999999994
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
#
# # Polymorphism -> наследниците на абстр.клас могат
# # да се използват едновременно, без да зависят един от друг
# vehicles = [Car(20, 5), Truck(100, 15)]
# for vehicle in vehicles:
#     vehicle.drive(5)
#     print(vehicle.fuel_quantity)




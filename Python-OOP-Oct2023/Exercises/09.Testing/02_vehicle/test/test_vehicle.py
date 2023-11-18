import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.vehicle = Vehicle(100, 3)

    def test_default_fuel_consumption_is_correct(self):
        result = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.assertEqual(result, 1.25)

    def test_correct_initializing(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.horse_power, 3)
        self.assertEqual(self.vehicle.capacity, 100)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_vehicle_not_enough_fuel(self):
        self.vehicle.fuel = 80
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(81)
        # !!!!!! test message
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_vehicle_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 87.5)

    def test_vehicle_refuel_properly(self):
        self.vehicle.drive(70)
        self.vehicle.refuel(50)
        self.assertEqual(self.vehicle.fuel, 62.5)

    def test_vehicle_more_refuel_exception(self):
        self.vehicle.drive(10)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)
            # !!!!!! test message
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_vehicle_string_presentation(self):
        expected = "The vehicle has 3 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(str(self.vehicle), expected)


# Running Tests
if __name__ == '__main__':
    unittest.main()

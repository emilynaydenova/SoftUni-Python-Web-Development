import unittest

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(unittest.TestCase):

    def setUp(self):
        self.car = SecondHandCar('Volvo', 'sedan', 1000, 2000.0)

    def test_car_initializing(self):
        self.car.model = 'Volvo'
        self.car.car_type = 'sedan'
        self.car.car_mileage = 1000
        self.car.price = 2000.0
        self.car.repairs = []

    def test_car_price_if_not_grater_than_1_throw_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        expected = 'Price should be greater than 1.0!'
        self.assertEqual(str(ve.exception), expected)

    def test_car_property_price_when_grater_than_1(self):
        self.car.price = 1.1
        self.assertEqual(self.car.price, 1.1)

    def test_car_mileage_if_not_grater_than_100_throw_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        expected = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(str(ve.exception), expected)

    def test_car_mileage_when_grater_than_100(self):
        self.car.mileage = 101
        self.assertEqual(self.car.mileage, 101)

    def test_set_promotional_price_greater_than_real_throw_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2001)
        expected = 'You are supposed to decrease the price!'
        self.assertEqual(str(ve.exception), expected)
        self.assertEqual(self.car.price, 2000)

    def test_set_promotional_price_successfully(self):
        result = self.car.set_promotional_price(1999)
        expected = 'The promotional price has been successfully set.'
        self.assertEqual(result, expected)
        self.assertEqual(self.car.price, 1999)

    def test_need_repair_if_repair_price_is_high(self):
        result = self.car.need_repair(1050, 'motor needs repair')
        expected = 'Repair is impossible!'
        self.assertEqual(result, expected)

    def test_need_repair_if_repair_is_possible(self):
        result = self.car.need_repair(950, 'motor needs repair')
        expected = 'Price has been increased due to repair charges.'
        self.assertEqual(result, expected)
        self.assertEqual(self.car.price, 2950)
        self.assertEqual(self.car.repairs, ['motor needs repair'])

    def test_compare_two_cars_different_types(self):
        car2 = SecondHandCar('Volvo', 'bus', 1000, 2000.0)
        result = self.car > car2
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare_two_cars_equal_types(self):
        car2 = SecondHandCar('Audi', 'sedan', 3000, 4000.0)
        result = self.car > car2
        self.assertFalse(result)

    def test_string_presentation(self):
        result = str(self.car)
        expected = "Model Volvo | Type sedan | Milage 1000km\n" + \
                   "Current price: 2000.00 | Number of Repairs: 0"
        self.assertEqual(result, expected)


if '__name__' == '__main__':
    unittest.main()

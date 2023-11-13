import unittest
from project.trip import Trip


class TestTrip(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(30000, 3, True)

    def test_travelers_enough(self):
        self.assertEqual(self.trip.travelers, 3)

    def test_travelers_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.trip.travelers = 0
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_one_traveler_not_is_family(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, False)

    def test_more_than_one_traveler_could_be_a_family(self):
        self.trip.travelers = 2
        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, True)

    def test_if_destination_is_in_offered_ones(self):
        answer = self.trip.book_a_trip('Ireland')
        self.assertEqual(answer, 'This destination is not in our offers, please choose a new one!')
        answer = self.trip.book_a_trip('Bulgaria')
        self.assertNotEqual(answer, 'This destination is not in our offers, please choose a new one!')

    def test_budget_enough_for_the_destination_if_family(self):
        answer = self.trip.book_a_trip('New Zealand')
        self.assertEqual(self.trip.budget, 9750)
        self.assertEqual(answer, 'Successfully booked destination New Zealand! Your budget left is 9750.00')
        self.assertEqual(self.trip.booked_destinations_paid_amounts['New Zealand'], 20250)

    def test_budget_enough_for_the_destination_if_not_family(self):
        self.trip.is_family = False
        answer = self.trip.book_a_trip('New Zealand')
        self.assertEqual(self.trip.budget, 7500)
        self.assertEqual(answer, 'Successfully booked destination New Zealand! Your budget left is 7500.00')
        self.assertEqual(self.trip.booked_destinations_paid_amounts['New Zealand'], 22500)

    def test_budget_is_not_enough(self):
        self.trip.is_family = False
        self.trip.travelers = 5
        answer = self.trip.book_a_trip('New Zealand')
        self.assertEqual(answer, 'Your budget is not enough!')

    def test_no_booking_status(self):
        self.trip.travelers = 5
        answer = self.trip.booking_status()
        self.assertEqual(answer, 'No bookings yet. Budget: 30000.00')

    def test_booking_status_3_bookings(self):
        self.trip.budget = 50000
        booking1 = self.trip.book_a_trip('Australia')
        booking2 = self.trip.book_a_trip('Bulgaria')
        booking3 = self.trip.book_a_trip('New Zealand')
        self.assertEqual(self.trip.booking_status(),
        """Booked Destination: Australia
Paid Amount: 15390.00
Booked Destination: Bulgaria
Paid Amount: 1350.00
Booked Destination: New Zealand
Paid Amount: 20250.00
Number of Travelers: 3
Budget Left: 13010.00""")

if __name__ == '__main__':
    unittest.main()

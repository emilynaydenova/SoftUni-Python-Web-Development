import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):

    def setUp(self):
        self.station = RailwayStation('Dublin')


    def test_init_values(self):
        self.assertEqual(self.station.name,"Dublin")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_name_less_than_3_chars_exception(self):
        with self.assertRaises(Exception) as ex:
            self.station.name = 'aaa'
        self.assertEqual(str(ex.exception),"Name should be more than 3 symbols!")
        with self.assertRaises(Exception) as ex:
            self.station.name = 'a'
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board('Cork')
        self.assertEqual(self.station.arrival_trains,deque(['Cork']))
        self.station.new_arrival_on_board('Limerick')
        self.assertEqual(self.station.arrival_trains, deque(['Cork','Limerick']))


    def test_if_test_info_is_not_for_first_arriving(self):
        self.station.new_arrival_on_board('Cork')
        self.station.new_arrival_on_board('Limerick')
        result = self.station.train_has_arrived('Limerick')
        expected = f"There are other trains to arrive before Limerick."
        self.assertEqual(result,expected)

    def test_if_test_info_is_for_first_arriving(self):
        self.station.new_arrival_on_board('Cork')
        self.station.new_arrival_on_board('Limerick')
        result = self.station.train_has_arrived('Cork')
        expected = f"Cork is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected)
        self.assertEqual(self.station.departure_trains,deque(['Cork']))

    def test_if_train_has_left_successfully(self):
        self.station.departure_trains = deque(['Cork','Limerick'])
        result = self.station.train_has_left('Cork')
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains,deque(['Limerick']))


    def test_if_train_has_not_left(self):
        self.station.departure_trains = deque(['Cork', 'Limerick'])
        result = self.station.train_has_left('Limerick')
        self.assertFalse(result)
        self.station.departure_trains = deque()
        result = self.station.train_has_left('Limerick')
        self.assertFalse(result)

# Running Tests
if __name__ == '__main__':
    unittest.main()

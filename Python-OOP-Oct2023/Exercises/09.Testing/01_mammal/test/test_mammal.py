from unittest import TestCase, main

from project.mammal import Mammal


#  A test suite is a collection of test cases, test suites, or both.
class TestMammal(TestCase):
    def setUp(self):
        self.lion = Mammal('Douglas', 'Lions', 'roar')

    def test_correct_initializing(self):
        self.assertEqual('Douglas', self.lion.name)
        self.assertEqual('Lions', self.lion.type)
        self.assertEqual('roar', self.lion.sound)

    def test_if_make_sound_is_correct(self):
        result = self.lion.make_sound()
        self.assertEqual(result, "Douglas makes roar")

    def test_if_get_right_kingdom_is_correct(self):
        result = self.lion.get_kingdom()
        self.assertEqual(result, 'animals')

    def test_if_get_info_returns_correct_message(self):
        result = self.lion.info()
        self.assertEqual(result, "Douglas is of type Lions")


# Running Tests
if __name__ == '__main__':
    main()

import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = TennisPlayer("some1", 20, 30)
        self.player2 = TennisPlayer("some2", 24, 10)

    def test_player_initializing(self):
        self.assertEqual(self.player1.name, 'some1')
        self.assertEqual(self.player1.age, 20)
        self.assertEqual(self.player1.points, 30)
        self.assertEqual(self.player1.wins, [])

    def test_if_player_name_has_less_or_equal_than_2_chars(self):
        with self.assertRaises(Exception) as ex:
            self.player1.name = 'Ab'
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_if_age_under_18(self):
        with self.assertRaises(Exception) as ex:
            self.player1.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_adding_win_to_tournament_list(self):
        self.player1.add_new_win('Paris')
        self.assertEqual(self.player1.wins, ['Paris'])

    def test_adding_existed_win_to_tournament_list_raise_error(self):
        self.player1.add_new_win('Paris')
        self.assertEqual(self.player1.add_new_win('Paris'),
                         f"Paris has been already added to the list of wins!")

    def test_if_player1_is_a_winner(self):
        self.player2.points = 40
        result = self.player1 < self.player2
        expected = 'some2 is a top seeded player and he/she is better than some1'
        self.assertEqual(result, expected)

    def test_if_player2_is_a_winner(self):

        result = self.player1 < self.player2
        expected = 'some1 is a better player than some2'
        self.assertEqual(result, expected)

    def test__str__no_wins(self):
        self.player1.points = 0
        expected = 'Tennis Player: some1\nAge: 20\nPoints: 0.0\nTournaments won: '
        self.assertEqual(str(self.player1), expected)

    def test__str__one_win(self):
        self.player1.wins.append('Paris')
        expected = "Tennis Player: some1\nAge: 20\nPoints: 30.0\nTournaments won: Paris"
        self.assertEqual(str(self.player1), expected)

    def test__str__two_wins(self):
        self.player1.wins.append('Paris')
        self.player1.wins.append('AO 2023')
        expected = "Tennis Player: some1\nAge: 20\nPoints: 30.0\nTournaments won: Paris, AO 2023"
        self.assertEqual(str(self.player1), expected)

if __name__ == '__main__':
    unittest.main()
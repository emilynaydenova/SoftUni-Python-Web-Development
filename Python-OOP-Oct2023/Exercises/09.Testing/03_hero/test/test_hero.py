import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("some hero", 1, 5, 5)
        self.enemy = Hero("some enemy", 1, 3, 0)

    def test_correct_initializing(self):
        self.assertEqual(self.hero.username, "some hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 5)
        self.assertEqual(self.hero.damage, 5)

    def test_battle_equal_heroes_usernames_exception(self):
        # act
        self.enemy.username = "some hero"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_when_hero_negative_health_exception(self):
        self.hero.health = 0
        # act
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        expected ="Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(str(ve.exception), expected)

    def test_battle_enemy_hero_with_negative_health_exception(self):
        # act
        enemy_hero = Hero("some name2", 5, -8, 3)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        expected = f"You cannot fight some name2. He needs to rest"
        self.assertEqual(str(ex.exception), expected)

    def test_battle_hero_and_enemy_with_negative_health(self):
        self.enemy.health = 5
        self.enemy.damage = 5
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "Draw")

    def test_when_hero_is_a_winner(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.damage, 10)
        self.assertLessEqual(self.enemy.health, 0)

    def test_when_enemy_is_a_winner(self):
        self.enemy.level = 2
        self.enemy.health = 10

        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.enemy.level, 3)
        self.assertEqual(self.enemy.health, 10)
        self.assertEqual(self.enemy.damage, 5)

    def test_hero_str_presentation(self):
        result = """Hero some hero: 1 lvl
Health: 5
Damage: 5
"""
        self.assertEqual(str(self.hero), result)


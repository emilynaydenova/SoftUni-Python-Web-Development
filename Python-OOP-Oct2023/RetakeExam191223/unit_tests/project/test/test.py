from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot('Alpine', 'Head', 100, 200)
        # self.robot.installed_software = [{'name': 'windows', 'capacity_consumption': 30, 'memory_consumption': 20},
        #                                  {'name': 'pycharm', 'capacity_consumption': 15, 'memory_consumption': 35}
        #                                  ]

    def test_climbing_robot_structure(self):
        self.assertEqual(ClimbingRobot.__base__.__name__, "object")
        self.assertTrue(hasattr(ClimbingRobot, "get_used_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_used_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "install_software"))

        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))

    def test_initial_values_set(self):
        self.assertEqual(self.robot.category, 'Alpine')
        self.assertEqual(self.robot.part_type, 'Head')
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 200)
        self.assertListEqual(self.robot.installed_software, [])

    def test_reject_not_allowed_category(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Invalid"
        self.assertEqual(str(ex.exception), f"Category should be one of {self.ALLOWED_CATEGORIES}")

    def test_category_setter_valid(self):
        for category in self.ALLOWED_CATEGORIES:
            with self.subTest(category=category):
                self.robot.category = category
                self.assertEqual(self.robot.category, category)

    def test_get_used_capacity(self):
        software1 = {'name': 'DataGrip', 'capacity_consumption': 20, 'memory_consumption': 20}
        software2 = {'name': 'PyCharm', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.installed_software = [software1, software2]
        expected = 50
        self.assertEqual(self.robot.get_used_capacity(), expected)

    def test_get_available_capacity(self):
        self.robot.installed_software = [{'capacity_consumption': 30}]
        expected = 70
        self.assertEqual(self.robot.get_available_capacity(), expected)

    def test_get_used_memory(self):
        software1 = {'name': 'DataGrip', 'capacity_consumption': 20, 'memory_consumption': 20}
        software2 = {'name': 'PyCharm', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.installed_software = [software1, software2]
        expected = 70
        self.assertEqual(self.robot.get_used_memory(), expected)

    def test_get_available_memory(self):
        self.robot.installed_software = [{'memory_consumption': 30}]
        expected = 170
        self.assertEqual(self.robot.get_available_memory(), expected)

    def test_install_software_successfully(self):
        software = {'name': 'Datagrip', 'capacity_consumption': 33, 'memory_consumption': 120}
        result = self.robot.install_software(software)
        self.assertEqual(result, f"Software 'Datagrip' successfully installed on Alpine part.")
        self.assertListEqual(self.robot.installed_software,[software])

    def test_install_software_successfully_with_limit_values(self):
        software = {'name': 'Datagrip', 'capacity_consumption': 100, 'memory_consumption': 200}
        result = self.robot.install_software(software)
        self.assertEqual(result, f"Software 'Datagrip' successfully installed on Alpine part.")
        self.assertListEqual(self.robot.installed_software,[software])

    def test_install_software_not_enough_capacity(self):
        software = {'name': 'Datagrip', 'capacity_consumption': 233, 'memory_consumption': 120}
        result = self.robot.install_software(software)
        self.assertEqual(result, f"Software 'Datagrip' cannot be installed on Alpine part.")
        self.assertEqual(self.robot.installed_software,[])


    def test_install_software_not_enough_memory(self):
        software = {'name': 'Datagrip', 'capacity_consumption': 33, 'memory_consumption': 220}
        result = self.robot.install_software(software)

        self.assertEqual(result, f"Software 'Datagrip' cannot be installed on Alpine part.")
        self.assertEqual(self.robot.installed_software,[])


if __name__ == '__main__':
    main()

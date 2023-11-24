from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        self.weight = 9
        super().__init__(name, kind, price, self.weight)

    def eating(self):
        self.weight += 3

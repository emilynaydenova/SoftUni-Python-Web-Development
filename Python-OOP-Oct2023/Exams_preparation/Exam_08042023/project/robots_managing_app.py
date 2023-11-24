from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService,
    }

    VALID_ROBOT_TYPES = {
        'FemaleRobot': FemaleRobot,
        'MaleRobot': MaleRobot
    }

    def __init__(self):
        self.robots = []  # all
        self.services = []  # all

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        robot_type = type(robot).__name__
        service_type = type(service).__name__
        if (robot_type, service_type) not in \
                [('FemaleRobot', 'SecondaryService'), ('MaleRobot', 'MainService')]:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in service.robots if r.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum([r.price for r in service.robots])
        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self):
        output = []
        for s in self.services:
            output.append(s.details())
        return '\n'.join(output)

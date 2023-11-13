import math
from abc import ABC, abstractmethod
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget: float = budget

        self.wins: int = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if value == '' or value.isspace():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        avg_team_equipment_protection = 0
        total_team_equipment_price = 0
        if self.equipment:
            total_team_equipment_price = sum([e.price for e in self.equipment])
            avg_team_equipment_protection = sum([e.protection for e in self.equipment]) / len(self.equipment)

        output = [f"Name: {self.name}",
                  f"Country: {self.country}",
                  f"Advantage: {self.advantage} points",
                  f"Budget: {self.budget:.2f}EUR",
                  f"Wins: {self.wins}",
                  f"Total Equipment Price: {total_team_equipment_price:.2f}",
                  f"Average Protection: {math.floor(avg_team_equipment_protection)}",
                  ]
        return '\n'.join(output)

import sys
from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in ["KneePad", "ElbowPad"]:
            raise Exception("Invalid equipment type!")
        new_equipment = KneePad() if equipment_type == "KneePad" else ElbowPad()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in ["OutdoorTeam", "IndoorTeam"]:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        new_team = OutdoorTeam(team_name, country, advantage) if team_type == 'OutdoorTeam' \
            else IndoorTeam(team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        equipment = [e for e in self.equipment if type(e).__name__ == equipment_type][-1]

        team = [t for t in self.teams if t.name == team_name][0]
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = [t for t in self.teams if t.name == team_name]
        if not team:
            raise Exception("No such team!")
        team = team[0]
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        equipments = [e for e in self.equipment if type(e).__name__ == equipment_type]

        increased = [e.increase_price() for e in equipments]
        return f"Successfully changed {len(increased)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = [t for t in self.teams if t.name == team_name1][0]
        team2 = [t for t in self.teams if t.name == team_name2][0]

        if type(team1) != type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_result = team1.advantage + sum([e.protection for e in team1.equipment])
        team2_result = team2.advantage + sum([e.protection for e in team2.equipment])

        if team1_result == team2_result:
            return "No winner in this game."

        if team1_result > team2_result:
            team1.win()
            return f"The winner is {team1.name}."
        else:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        sorted_teams_by_wins = sorted(self.teams, key=lambda x: -x.wins)
        # 145 teams_stat = '\n'.join([t.get_statistics() for t in sorted_teams_by_wins])

        statistics = [f"Tournament: {self.name}",
                      f"Number of Teams: {len(self.teams)}",
                      "Teams:"]
        [statistics.append(t.get_statistics()) for t in sorted_teams_by_wins]
        return '\n'.join(statistics)

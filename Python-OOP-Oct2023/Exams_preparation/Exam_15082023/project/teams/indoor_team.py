from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        self.budget = 500
        super().__init__(name, country, advantage, self.budget)

    def win(self):
        self.advantage += 145
        self.wins += 1

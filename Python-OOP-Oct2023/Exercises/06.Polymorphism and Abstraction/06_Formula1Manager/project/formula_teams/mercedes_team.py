from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {
            'Petronas': {
                1: 1000000,
                3: 500000,
            },
            'TeamViewer': {
                5: 100000,
                7: 50000
            },
        }
        expenses = 200000

        revenue = 0
        for sponsor in sponsors:
            for place in sponsors[sponsor]:
                if race_pos <= place:
                    revenue += sponsors[sponsor][place]
                    break
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

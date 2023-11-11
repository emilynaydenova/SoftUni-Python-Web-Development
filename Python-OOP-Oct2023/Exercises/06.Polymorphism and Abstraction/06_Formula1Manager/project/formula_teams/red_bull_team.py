from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {
            'Oracle': {
                1: 1500000,
                2: 800000,
            },
            'Honda': {
                8: 20000,
                10: 10000
            },
        }
        expenses = 250000
        revenue = 0
        for sponsor in sponsors:
            for place in sponsors[sponsor]:
                if race_pos <= place:
                    revenue += sponsors[sponsor][place]
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

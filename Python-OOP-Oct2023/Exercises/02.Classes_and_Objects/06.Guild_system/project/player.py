class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp  # health points
        self.mp = mp  # magic/mana points
        self.skills = {}   # skill:mana_cost
        self.guild = 'Unaffiliated'  # неприсъединен

    def add_skill(self, skill_name, mana_cost):
        # if key in dictionary
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        result = [f'Name: {self.name}']
        result.append(f'Guild: {self.guild}')
        result.append(f'HP: {self.hp}')
        result.append(f'MP: {self.mp}')
        for k, v in self.skills.items():
            result.append(f'==={k} - {v}')
        return '\n'.join(result)


"""
Magic or mana is an attribute assigned to characters within
a role-playing or video game that indicates their power to use
special magical abilities or "spells".
Magic is usually measured in magic points or mana points, shortened as MP.
"""
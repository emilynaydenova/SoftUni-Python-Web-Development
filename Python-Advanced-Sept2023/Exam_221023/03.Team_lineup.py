"""
Write a function called team_lineup that receives information
about certain football players and their countries and
returns a sorted result
"""


def team_lineup(*args):
    team_players = dict(args)

    countries = set(team_players.values())

    team_by_countries = {c: [] for c in countries}

    for c in countries:
        for k, v in team_players.items():
            if v == c:
                team_by_countries[c].append(k)

    result = dict(sorted(team_by_countries.items(), key=lambda x: (-len(x[1]), x[0])))

    output = []
    for k, v in result.items():
        output.append(f'{k}:')
        for player in v:
            output.append(f"  -{player}")

    return '\n'.join(output)


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))

print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))

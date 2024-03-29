
from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        player_found = [pp for pp in self.players if pp.name == player.name]
        if player_found:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        for player in self.players:
            if player_name == player.name:
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        result = [f'Guild: {self.name}']
        for pp in self.players:
            result.append(pp.player_info())
        return '\n'.join(result)


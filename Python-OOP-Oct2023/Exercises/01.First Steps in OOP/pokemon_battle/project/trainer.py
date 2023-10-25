from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        for pp in self.pokemons:
            if pokemon == pp:
                return 'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for obj in self.pokemons:
            if pokemon_name == obj.name:
                self.pokemons.remove(obj)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = list()
        result.append(f'Pokemon Trainer {self.name}')
        result.append(f'Pokemon count {len(self.pokemons)}')
        for p in self.pokemons:
            result.append(f'- {p.pokemon_details()}')
        return '\n'.join(result)

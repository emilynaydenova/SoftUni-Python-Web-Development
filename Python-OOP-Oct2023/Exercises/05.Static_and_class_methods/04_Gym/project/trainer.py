from itertools import count
class Trainer:
    id = count(start=1)

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return next(Trainer.id)

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'

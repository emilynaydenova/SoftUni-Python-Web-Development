from itertools import count


class Equipment:
    id = count(start=1)

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return next(Equipment.id)

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

#
# e1 = Equipment("e1")
# e2 = Equipment("e2")
# e3 = Equipment("e3")
#
# print(e1)
# print(e2)
# print(e3)

from functools import reduce
from typing import List

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

from project.animal import Animal

from project.worker import Worker


class Zoo:
    def __init__(self,
                 name: str,
                 budget: int,
                 animal_capacity: int,
                 workers_capacity: int
                 ):
        # public instance attribute
        self.name = name
        # private attributes
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        # public instance attributes
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if (price <= self.__budget) and (len(self.animals) < self.__animal_capacity):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
            # or type(animal).__name__

        if (price > self.__budget) and (len(self.animals) < self.__animal_capacity):
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
            # or {type(worker).__name__}
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f'{worker[0].name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        # !!!!!
        workers_payment = sum([w.salary for w in self.workers])

        if workers_payment <= self.__budget:
            self.__budget -= workers_payment
            return f'You payed your workers. They are happy. ' \
                   f'Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        # get_needs = self.money_for_care
        amount_to_pay = sum([t.get_needs() for t in self.animals])
        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        animals_types = ['Lion', 'Tiger', 'Cheetah']
        animals_list = {idx: [] for idx in range(0, 3)}

        for animal in self.animals:
            idx = animals_types.index(type(animal).__name__)
            animals_list[idx].append(animal)

        lions, tigers, cheetahs = animals_list[0], animals_list[1], animals_list[2]
        #
        # lions = [animal for animal in self.animals if type(animal).__name__ == animals_types[0]]
        # tigers = [animal for animal in self.animals if type(animal).__name__ == animals_types[1]]
        # cheetahs = [animal for animal in self.animals if type(animal).__name__ == animals_types[2]]

        result = [f'You have {len(self.animals)} animals']
        result.append(f'----- {len(lions)} Lions:')
        result.append('\n'.join([animal.__repr__() for animal in lions]))
        result.append(f'----- {len(tigers)} Tigers:')
        result.append('\n'.join([animal.__repr__() for animal in tigers]))
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.append('\n'.join([animal.__repr__() for animal in cheetahs]))
        return '\n'.join(result)

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers\n"
        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join([k.__repr__() for k in keepers]) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join([c.__repr__() for c in caretakers]) + '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join([v.__repr__() for v in vets])
        return result

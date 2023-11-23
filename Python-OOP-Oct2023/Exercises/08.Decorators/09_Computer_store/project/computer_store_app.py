from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPE = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPE:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.VALID_COMPUTER_TYPE[type_computer](manufacturer, model)
        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        # sorted_warehouse = sorted(self.warehouse, key= lambda x: x.ram)
        computer = [computer for computer in self.warehouse
                    if (computer.price <= client_budget and
                        computer.processor == wanted_processor
                        and computer.ram >= wanted_ram)]
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")

        self.warehouse.remove(computer[0])
        self.profits += client_budget - computer[0].price
        return f"{computer[0]} sold for {client_budget}$."

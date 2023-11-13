from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        self.protection = 90
        self.price = 25.0
        super().__init__(self.protection, self.price)

    def increase_price(self):
        self.price *= 1.1


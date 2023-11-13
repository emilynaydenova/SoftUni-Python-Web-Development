from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        self.protection = 120
        self.price = 15.0
        super().__init__(self.protection, self.price)

    def increase_price(self):
        self.price *= 1.2


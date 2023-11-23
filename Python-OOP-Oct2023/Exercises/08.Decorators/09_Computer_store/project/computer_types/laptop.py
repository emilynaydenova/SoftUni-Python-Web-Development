from project.computer_types.computer import Computer


class Laptop(Computer):
    VALID_DESKTOP_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200,
    }

    # 93%
    @staticmethod
    def validate_ram(ram):
        if ram in [2, 4, 8, 16, 32, 64]:
            return True

        return False

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_DESKTOP_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if not self.validate_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.calculate_price(ram, self.VALID_DESKTOP_PROCESSORS[self.processor])
        return f"Created {self.__repr__()} for {self.price}$."


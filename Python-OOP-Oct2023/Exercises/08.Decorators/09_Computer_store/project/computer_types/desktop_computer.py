from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    VALID_DESKTOP_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800,
    }

    @staticmethod
    def validate_ram(ram):
        if ram in [2, 4, 8, 16, 32, 64, 128]:
            return True
        return False

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_DESKTOP_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if not self.validate_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.calculate_price(ram,self.VALID_DESKTOP_PROCESSORS[self.processor])
        return f"Created {self.__repr__()} for {self.price}$."


# d = DesktopComputer('Apple',"XP")
# d.configure_computer('Intel Core i5-12600K',4)
# print(d.price)
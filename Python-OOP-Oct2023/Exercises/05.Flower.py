class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

        # print(type(self)) # <class '__main__.Flower'>

    def water(self, quantity):
        # Each time check if the quantity  ...
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        flag = '' if self.is_happy else 'not '
        return f'{self.name} is {flag}happy'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

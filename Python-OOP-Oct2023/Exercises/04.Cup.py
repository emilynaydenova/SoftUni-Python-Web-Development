class Cup:
    # print(globals())
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

        # print(locals())
        # self is a Cup object in a local scope
        # {'self': <__main__.Cup object at 0x0000018CEB10C0D0>,
        # 'size': 200, 'quantity': 50}

    def fill(self, quantity):
        if self.get_free_size() < quantity:
            return
        self.quantity += quantity

    def get_free_size(self):
        return self.size - self.quantity

    def status(self):
        return self.get_free_size()



cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

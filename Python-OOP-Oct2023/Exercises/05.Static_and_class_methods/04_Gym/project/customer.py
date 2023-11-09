from itertools import count


class Customer:
    id = count(start=1)

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        # every customer has his own id
        self.id =  Customer.get_next_id()

    @staticmethod
    def get_next_id():
        return next(Customer.id)

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; ' \
               f'Email: {self.email}'

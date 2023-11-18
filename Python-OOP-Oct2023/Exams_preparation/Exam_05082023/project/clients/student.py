from project.clients.base_client import BaseClient


class Student(BaseClient):
    INTEREST_PROC = 1.0
    LOAN_TYPE_ = 'StudentLoan'

    def __init__(self, name: str, client_id: str, income: float):
        self.interest = 2.0
        super().__init__(name, client_id, income, self.interest)

    def increase_clients_interest(self):
        self.interest += self.INTEREST_PROC

#
# s = Student("  ",1234567890, 1000)
# print(s.interest)
# s.increase_clients_interest()
# print(s.interest)
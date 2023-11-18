from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST_PROC = 2.0
    LOAN_TYPE_ = "MortgageLoan"

    def __init__(self, name: str, client_id: str, income: float):
        self.interest = 4.0
        super().__init__(name, client_id, income, self.interest)

    def increase_clients_interest(self):
        self.interest += self.INTEREST_PROC

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}
    VALID_CLIENT_TO_LOAN = {"Student": "StudentLoan", "Adult": "MortgageLoan"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id][0]
        if client.LOAN_TYPE_ != loan_type:
            raise Exception("Inappropriate loan type!")

        loan = [loan for loan in self.loans if type(loan).__name__ == loan_type][0]

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]
        if not client:
            raise Exception("No such client!")
        client = client[0]
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        if loan_type in self.VALID_LOAN_TYPES:
            increased_loans = [loan.increase_interest_rate() for loan in self.loans if type(loan).__name__ == loan_type]
            return f"Successfully changed {len(increased_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates = [client.increase_clients_interest() for client in self.clients if
                                client.interest < min_rate]
        return f"Number of clients affected: {len(changed_client_rates)}."

    def get_statistics(self):
        active_clients = len(self.clients)
        total_income = sum([client.income for client in self.clients])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(
            self.clients) if self.clients else 0
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = 0
        for c in self.clients:
            for loan in c.loans:
                granted_sum += loan.amount

        print(self.clients)
        print([c.loans for c in self.clients])
        result = [f"Active Clients: {active_clients}",
                  f"Total Income: { total_income:.2f}",
                  f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}",
                  ]
        return "\n".join(result)

"""
        def _find_client_by_id(self, client_id):
            client = [client for client in self.clients if client.client_id == client_id]
            return client[0] if client else None

        def _find_loans_by_type(self, loan_type):
            return [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]

        def _find_clients_by_interest_rate(self, min_rate):
            return [client for client in self.clients if client.interest < min_rate]
"""
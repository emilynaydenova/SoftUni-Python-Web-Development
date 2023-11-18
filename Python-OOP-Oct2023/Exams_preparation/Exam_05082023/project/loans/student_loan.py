from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST_RATE_TO_ADD = 0.2

    def __init__(self):
        self.interest_rate = 1.5
        self.amount = 2000.0
        super().__init__(self.interest_rate, self.amount)

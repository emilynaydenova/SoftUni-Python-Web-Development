from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE_TO_ADD = 0.5

    def __init__(self):
        self.interest_rate = 3.5
        self.amount = 50000.0
        super().__init__(self.interest_rate, self.amount)

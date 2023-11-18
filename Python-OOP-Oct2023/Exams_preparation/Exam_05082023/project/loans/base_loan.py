from abc import ABC, abstractmethod


class BaseLoan(ABC):
    INTEREST_RATE_TO_ADD = 0
    #  interest rate used to calculate interest is typically expressed
    #  as an annual percentage rate (APR)

    @abstractmethod
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    def increase_interest_rate(self):
        #  in percent -лихвен процент по заема
        self.interest_rate += self.INTEREST_RATE_TO_ADD

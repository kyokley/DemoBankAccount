from utils import send_email

PREFERRED_BALANCE = 1000

class BankAccount(object):
    def __init__(self, balance=0):
        self._balance = balance
        self.preferred = self._balance >= PREFERRED_BALANCE

    def get_balance(self):
        return self._balance

    def deposit(self, val):
        if val < 0:
            raise Exception('Only positive values are allowed')
        self._balance += val

        if not self.preferred and self._balance >= PREFERRED_BALANCE:
            self.preferred = True
            send_email("Congrats! You've qualified for preferred status!")

    def withdraw(self, val):
        if val < 0:
            raise Exception('Only positive values are allowed')
        elif self._balance - val < 0:
            raise Exception('Oh no! Not enough funds!')
        self._balance -= val

        if self.preferred and self._balance < PREFERRED_BALANCE:
            self.preferred = False
            send_email("Balance is too to maintain preferred status")

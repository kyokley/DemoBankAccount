import unittest

from bank_account import BankAccount

class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(balance=0)

    def test_positive_deposit(self):
        self.account.deposit(100)

        expected = 100
        actual = self.account.get_balance()
        self.assertEqual(expected, actual)

    def test_negative_deposit(self):
        self.assertRaises(Exception,
                          self.account.deposit,
                          -100)

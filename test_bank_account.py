import unittest
import mock

from bank_account import BankAccount

class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(balance=0)

    def test_positive_deposit(self):
        self.account.deposit(100)

        expected = 100
        actual = self.account.get_balance()
        self.assertEqual(expected, actual)
        self.assertFalse(self.account.preferred)

    def test_negative_deposit(self):
        self.assertRaises(Exception,
                          self.account.deposit,
                          -100)

    @mock.patch('bank_account.send_email', autospec=True)
    def test_preferred(self, mock_send_email):
        self.account.deposit(1000)

        expected = 1000
        actual = self.account.get_balance()
        self.assertEqual(expected, actual)
        mock_send_email.assert_called_once_with("Congrats! You've qualified for preferred status!")
        self.assertTrue(self.account.preferred)

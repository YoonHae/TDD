from bank_business import Account
import unittest


class CustomTests(unittest.TestCase):
    # before test
    def setUp(self):
        self.account = Account(10000)
    # test case of initialize method
    def test_account(self):
        self.assertIsNotNone(self.account, "객체 없어")


    # test case of balance method
    def test_balance(self):
        balance = self.account.balance()
        self.assertEqual(balance, 10000, "잔액 달라")

        acc = Account(1000)
        self.assertEqual(acc.balance(), 1000, "잔액 달라")

        try:
            acc = Account(0)  # 0원으로 계좌개설 불가
            self.fail("0원으로 계좌개설 불가")
        except Exception as e:
            self.assertTrue(True)


    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.balance(), 11000, "잔액 달라")


    def test_withdraw(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.balance(), 9000, "잔액 달라")

        try:
            self.account.withdraw(10000)
            self.fail("잔액보다 큰 금액은 출금할 수 없음")
        except Exception as e:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

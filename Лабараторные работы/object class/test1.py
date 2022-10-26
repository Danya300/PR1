from bibl1 import college
import unittest


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.b1 = college(100, 1)
        self.b2 = college(90, 2)
        self.b3 = college(90, 3)
        self.b4 = college(90, 4)

    def test_account_deposit(self):
        stud = 'ул. Воронина,2 в колледже 4 группах находятся 115 студентов'
        self.b2.allstud()
        self.assertEqual(self.b2.allstud(), stud)


if __name__ == '__main__':
    unittest.main()

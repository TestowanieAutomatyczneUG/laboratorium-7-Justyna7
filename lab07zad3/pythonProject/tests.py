import unittest
from main import *


class StatementTest(unittest.TestCase):

    def setUp(self):
        self.temp = statement

    def open_files(self, i, p):
        with open(i, 'r') as invoice:
            i = json.load(invoice)
        with open(p, 'r') as plays:
            p = json.load(plays)
        return i, p

#     def test_coverage(self):
#         invoice, plays = self.open_files("Invoice.json", 'Plays.json')
#         self.assertEqual("\
# Statement for BigCo\
# \n Hamlet: $650.00 (55 seats)\
# \n As You Like It: $580.00 (35 seats)\
# \n Othello: $500.00 (40 seats)\
# \nAmount owed is $1,730.00\
# \nYou earned 47 credits\
# \n", self.temp(invoice, plays))

    def test_coverage2(self):
        invoice, plays = self.open_files("Invoice2.json", 'Plays3.json')
        self.assertEqual("\
Statement for BigCo\
\n Hamlet: $400.00 (15 seats)\
\n As You Like It: $450.00 (35 seats)\
\n Othello: $500.00 (40 seats)\
\nAmount owed is $1,350.00\
\nYou earned 15 credits\
\n", self.temp(invoice, plays))

    def test_Error(self):
        invoice, plays = self.open_files("Invoice.json", 'Plays2.json')
        self.assertRaises(ValueError, self.temp, invoice, plays)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

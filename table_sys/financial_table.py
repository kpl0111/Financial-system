class financial_table:
    def __init__(self):
        self.total_salary, self.total_income, self.other_outcome, self.final_profit = 0, 0, 0, 0

    def printstr(self):
        res = 'total salary: ' + str(self.total_salary) + '\n'
        res += 'total income: ' + str(self.total_income) + '\n'
        res += 'other outcome: ' + str(self.other_outcome) + '\n'
        res += 'final profit: ' + str(self.final_profit)
        return res
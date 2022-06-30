class salary_table:
    def __init__(self):
        self.sid, self.salarybase, self.bonus, self.docked, self.final = 'empty', 0, 0, 0, 0

    def tostr(self):
        return self.sid + ',' + str(self.salarybase) + ',' + str(self.bonus) + ',' + str(self.docked) + ',' + str(self.final)
    
    def fromstr(self, tstr):
        self.sid, self.salarybase, self.bonus, self.docked, self.final = tstr.split(',')
        self.salarybase = float(self.salarybase)
        self.bonus, self.docked, self.final = float(self.bonus), float(self.docked), float(self.final)
    
    def printstr(self):
        res = 'Staff id: ' + self.sid + '\n'
        res += 'Basic salary: ' + str(self.salarybase) + '\n'
        res += 'Total Bonus: ' + str(self.bonus) + '\n'
        res += 'Total dokecd: ' + str(self.docked) + '\n'
        res += 'Final salary: ' + str(self.final)
        return res
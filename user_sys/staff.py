from user_sys.user import user

class staff(user):
    def __init__(self):
        super().__init__()
        self.name, self.sid, self.age, self.seniority, self.salary = 'empty', 'empty', -1, -1, -1
    
    def get_salary_tb(self, salary_list : list):
        tmp = None
        for i in salary_list:
            if i.sid == self.sid:
                tmp = i
                break
        return tmp

    def tostr(self):
        # print('fk')
        return super().tostr() + ' ' + self.sid + ' ' + self.name + ' '+ str(self.age) + ' ' + str(self.seniority) + ' ' + str(self.salary)

    def fromstr(self, tstr):
        self.uid, self.pwd, self.utype, self.sid, self.name, self.age, self.seniority, self.salary = tstr.split()
        self.pwd = self.pwd[len(self.uid):]
        self.age, self.seniority, self.salary = int(self.age), int(self.seniority), float(self.salary)
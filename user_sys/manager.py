from user_sys.FM import FM
from table_sys import *

class manager(FM):
    def __init__(self):
        super().__init__()

    def mdf_salary_base(self, sid, mdf, tdbs):
        pass

    def settle_season(self, tdbs):
        salary_list = []
        for i, j in enumerate(tdbs.stafflist):
            salary_list.append(salary_table())
            salary_list[i].sid = j.sid
            salary_list[i].salary_base = j.salary
            salary_list[i].final = j.salary
        for i, j in enumerate(tdbs.salary_recs):
            for k in range(len(salary_list)):
                if salary_list[k].sid == j.sid:
                    if j.mdf > 0:
                        salary_list[k].bonus += j.mdf
                    else:
                        salary_list[k].docked += j.mdf
                    salary_list[k].final += j.mdf
                    break 
        return salary_list

    def get_report(self, tdbs):
        for i, j in enumerate(tdbs.salary):
            pass

    def archive_season(self, tdbs):
        pass
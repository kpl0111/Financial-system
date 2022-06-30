import UI.log_panel 
import tkinter as tk

def staff(tmd):
    window = tk.Tk()  # 创建窗口
    window.title("职工窗口")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    t = tk.Text(window, height=8)
    t.pack()
    t.insert('end', "输入需要的信息")

    def query_salary():
        res = tmd.query_salary()
        if res == None:
            t.delete('1.0', 'end')
            t.insert('end', '目前尚未结算工资')
        else:
            t.delete('1.0', 'end')
            t.insert('end', res.printstr())

    def enroll_back():
        window.destroy()
        tmd.logout()
        UI.log_panel.log_panel(tmd)
        return

    def sec_exit():
        tmd.logout()
        window.quit()
    
    window.protocol('WM_DELETE_WINDOW', sec_exit)
    but1 = tk.Button(window, text='查询工资单', width=10, height=2, command=query_salary)
    but1.pack()
    but3 = tk.Button(window, text="退出", width=10, height=2, command=enroll_back)
    but3.pack()
    #window.mainloop()  # 结束（不停循环刷新）
import UI.log_panel
import tkinter as tk

def dba(tmd):
    # 用户操作界面
    window = tk.Tk()  # 创建窗口
    window.title("数据库管理员")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    t = tk.Text(window, height=4)
    t.pack()
    lbl = tk.Label(window, text='DBA为调试模式, 上方输入相关信息, 下方输入类型', height=3)
    lbl.pack()
    t1 = tk.Text(window, height=4)
    t1.pack()

    def add_account():
        res = tmd.register(t.get('1.0', 'end-1c'), t1.get('1.0', 'end-1c'))
        t1.delete('1.0', 'end')
        t.delete('1.0', 'end')
        if res:
            t.insert('end', '新建账号成功')
        else:
            t.insert('end', '新建失败')

    def reset_acc():
        res = tmd.reset_acc(t.get('1.0', 'end-1c'), t1.get('1.0', 'end-1c'))
        t1.delete('1.0', 'end')
        t.delete('1.0', 'end')
        if res:
            t.insert('end', '重置账号成功')
        else:
            t.insert('end', '重置失败')

    def enroll_back():
        window.destroy()
        tmd.logout()
        UI.log_panel.log_panel(tmd)
        return

    def sec_exit():
        tmd.logout()
        window.quit()
    
    window.protocol('WM_DELETE_WINDOW', sec_exit)
    but1 = tk.Button(window, text="添加账户", width=10, height=2, command=add_account)
    but1.pack()
    but2 = tk.Button(window, text="重置账户密码", width=10, height=2, command=reset_acc)
    but2.pack()
    but3 = tk.Button(window, text="退出", width=10, height=2, command=enroll_back)
    but3.pack()
    # window.mainloop()  # 结束（不停循环刷新）
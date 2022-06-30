import tkinter as tk
from user_sys import *
import UI.cashier_panel
import UI.dba_panel
import UI.manager_panel
import UI.staff_panel

def reset_pwd(tmd):
    window = tk.Tk()  # 创建窗口
    window.title("工作")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    j = tk.Label(window,
                 text="账号",  # 文本,可变换
                 font=("黑体", 12),  # 字体和大小
                 width=10, height=2  # 字体所占的宽度和高度
                 )
    j.pack()
    e = tk.Entry(window, show=None)
    e.pack()
    j1 = tk.Label(window,
                  text="确认密码",  # 文本,可变换
                  font=("黑体", 12),  # 字体和大小
                  width=10, height=2  # 字体所占的宽度和高度
                  )
    j1.pack()
    e1 = tk.Entry(window, show='*')
    e1.pack()
    j2 = tk.Label(window,
                  text="新密码",  # 文本,可变换
                  font=("黑体", 12),  # 字体和大小
                  width=10, height=2  # 字体所占的宽度和高度
                  )
    j2.pack()
    e2 = tk.Entry(window, show='*')
    e2.pack()
    t1 = tk.Text(window, height=4)
    t1.pack()

    def enroll_back():
        # 返回用户界面
        window.destroy()
        log_panel(tmd)
        return

    def resetpwd():
        # 重置密码函数
        s1, s2, s3 = e.get(), e1.get(), e2.get()
        res = tmd.tlogin(s1, s2)
        t1.delete('1.0', 'end')
        if not res:
            t1.insert('end', '重置失败')
            return
        res = tmd.reset_pwd(s2, s3)
        if res:
            t1.insert('end', '重置成功')
        else:
            t1.insert('end', '重置失败')

    but1 = tk.Button(window, text="确认重置", width=10, height=2, command=resetpwd)
    but1.pack()
    but2 = tk.Button(window, text="返回登录", width=10, height=2, command=enroll_back)
    but2.pack()

def log_panel(tmd):
    window = tk.Tk()  # 创建窗口
    window.title("用户登录")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    # 窗口的label
    k = tk.Label(window,
                 textvar="用户名",  # 文本,可变换
                 font=('Arial', 12),  # 字体和大小
                 width=10, height=2  # 字体所占的宽度和高度
                 )
    k.pack()  # 固定窗口

    e = tk.Entry(window, show=None)  # 输入的用户名
    e.pack()
    j = tk.Label(window,
                 text="密码",  # 文本,可变换
                 font=("黑体", 12),  # 字体和大小
                 width=10, height=2  # 字体所占的宽度和高度
                 )
    j.pack()
    ming = tk.Entry(window, show='*') # 输入框
    ming.pack()

    j1 = tk.Label(window,
                  text="信息提示",  # 文本,可变换
                  font=("黑体", 12),  # 字体和大小
                  width=10, height=2  # 字体所占的宽度和高度
                  )
    j1.pack()
    t = tk.Text(window, width=30, height=2)
    t.pack()

    def insert_end():
        # 用户登录信息操作，根据用户信息进入相应界面
        # 从输入框获取信息
        username = e.get()
        password = ming.get()
        pass #进行操作
        if not tmd.tlogin(username, password):
            strs = "用户名或密码错误"
            t.delete('1.0', 'end')
            t.insert("end", strs)
        else:
            if type(tmd.usr) == staff:
                window.destroy()
                UI.staff_panel.staff(tmd)
            elif type(tmd.usr) == dba:
                window.destroy()
                UI.dba_panel.dba(tmd)
            elif type(tmd.usr) == cashier:
                window.destroy()
                UI.cashier_panel.cashier(tmd)
            else: 
                window.destroy()
                UI.manager_panel.manager(tmd)

    def set_accout():
        # 重置密码
        window.destroy()
        reset_pwd(tmd)

    but1 = tk.Button(window, text="登录", width=10, height=2, command=insert_end)
    but1.pack()
    but3 = tk.Button(window, text="重置密码", width=10, height=2, command=set_accout)
    but3.pack()
    # e.get()  # 可以得到输入的内容

    # 以上是窗口的主体
    window.mainloop()  # 结束（不停循环刷新）


if __name__ == '__main__':
    log_panel()
    # use_enroll()
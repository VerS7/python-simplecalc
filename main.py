from tkinter import *


class Program:
    def __init__(self):
        """Window"""
        self.window = Tk()
        self.window.title('Different base calculator')
        self.window.resizable(width=False,height=False)
        """Variables"""
        self.num = StringVar()
        self.num1 = StringVar()
        self.base = IntVar()
        self.base1 = IntVar()
        self.base2 = IntVar()
        self.operator = True
        """Widgets"""
        # first input
        self.inpt = Entry(textvariable=self.num, justify=CENTER, font=('Arial Bold', 10)).grid(column=0, row=0, padx=5)
        # second input
        self.inpt1 = Entry(textvariable=self.num1, justify=CENTER, font=('Arial Bold', 10)).grid(column=2, row=0, padx=5)
        # first select base
        self.selectbase = Spinbox(textvariable=self.base, from_=2, to=36, justify=CENTER).grid(column=0, row=1, padx=5)
        # second select base
        self.selectbase1 = Spinbox(textvariable=self.base1, from_=2, to=36, justify=CENTER).grid(column=2, row=1, padx=5)
        # third select base
        self.selectbase2 = Spinbox(textvariable=self.base2, from_=2, to=36, justify=CENTER).grid(column=0, row=3, padx=5)
        # result label
        self.lbl = Label(justify=CENTER, text='Result', font=('Arial Bold', 15))
        self.lbl.grid(column=1, row=2, columnspan=2, padx=5)
        # count result
        self.countbtn = Button(text='Count result', font=('Arial Bold', 11), command=self.count_result)
        self.countbtn.grid(column=0, row=2, padx=0, ipadx=25)
        # change base
        self.basebtn = Button(text='+', font=('Arial Bold', 10), command=self.change_operator)
        self.basebtn.grid(column=1, row=0, padx=10, ipadx=5)
        """Error label"""
        self.errlbl = Label(justify=CENTER, text='', wraplength=False, font=('Arial', 11))
        self.errlbl.grid(column=1, row=3, columnspan=2)
        """Run app"""
        self.window.mainloop()

    def change_operator(self):
        """Changes operator and button text"""
        if self.operator:
            self.operator = False
            self.basebtn.config(text='x')
        else:
            self.operator = True
            self.basebtn.config(text='+')

    def convert_base(self, num, to_base=10, from_base=10):
        """Converts number from base to base"""
        n = int(num, from_base) if isinstance(num, str) else num
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            n, m = divmod(n, to_base)
            res += alphabet[m]
        return res[::-1]

    def count_result(self):
        """Counts result of two inputs"""
        self.errlbl.config(text="")
        try:
            firstnum = self.convert_base(self.num.get(), 10, self.base.get())
            secondnum = self.convert_base(self.num1.get(), 10, self.base1.get())
            if self.operator:
                self.lbl.config(text=self.convert_base(int(firstnum)+int(secondnum), self.base2.get(), 10))
            else:
                self.lbl.config(text=self.convert_base(int(firstnum)*int(secondnum), self.base2.get(), 10))
        except Exception as e:
            self.errlbl.config(text="Can't count result.")
            print(e)


if __name__ == "__main__":
     App = Program()


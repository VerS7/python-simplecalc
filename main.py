from tkinter import *


class Program:
    def __init__(self):
        """Window"""
        self.window = Tk()
        self.window.title('2/10 calculator')
        self.window.resizable(width=False,height=False)
        """Variables"""
        self.var = IntVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

    def countBase10(self):
        """Return base10 int"""
        return self.var.get() + self.var1.get()

    def countBase2(self):
        """Return base2 int"""
        return int(self.to_base2(self.to_base10(self.var.get()) + self.to_base10(self.var1.get())))

    def count_result(self):
        try:
            """update error status"""
            self.errlbl.config(text='')
            """if from base2"""
            if bool(self.var2.get()):
                """if to base2"""
                if bool(self.var3.get()):
                    self.lbl1.config(text=self.countBase2())
                else:
                    self.lbl1.config(text=self.countBase10())
            else:
                if bool(self.var3.get()):
                    self.lbl1.config(text=self.countBase2())
                else:
                    self.lbl1.config(text=self.countBase10())
        except Exception as e:
            print(e)
            self.errlbl.config(text="Can't count result.")

    def to_base2(self, a):
        """Int to base2"""
        n = ''
        k = ''
        while a > 0:
            n = n + str(a % 2)
            a = a // 2
        n = list(reversed(n))
        for j in range(len(n)):
            k += n[j]
        return k

    def to_base10(self, a):
        """Base2 to int"""
        a = str(a)
        k = 0
        for i in range(len(a)):
            k += int(a[len(a) - i - 1]) * int(2 ** i)
        return k

    def main(self):
        """Widgets"""
        # left input
        self.inpt = Entry(textvariable=self.var, justify=CENTER, font=('Arial', 15))
        self.inpt.grid(column=0, row=0)
        # right input
        self.inpt1 = Entry(textvariable=self.var1, justify=CENTER, font=('Arial', 15))
        self.inpt1.grid(column=1, row=0)
        # placeholder label
        self.lbl = Label(justify=CENTER, text='Result', wraplength=False, padx=50, font=('Arial', 15))
        self.lbl.grid(column=2, row=1)
        # result label
        self.lbl1 = Label(justify=CENTER, text='0', wraplength=False, padx=50, font=('Arial', 15))
        self.lbl1.grid(column=2, row=2)
        # From int-base2 checkbox
        self.cbtn = Checkbutton(text='from base 2', variable=self.var2, font=('Arial', 15))
        self.cbtn.grid(column=0, row=1)
        # To int-base2 checkbox
        self.cbtn1 = Checkbutton(text='To base 2', variable=self.var3, font=('Arial', 15))
        self.cbtn1.grid(column=1, row=1)
        # Count result button
        self.countbtn = Button(text='Count result', padx=160, font=('Arial', 15), command=self.count_result)
        self.countbtn.grid(column=0, row=2, columnspan=2)
        """Error label"""
        self.errlbl = Label(justify=CENTER, text='', wraplength=False, font=('Arial', 15))
        self.errlbl.grid(column=0, row=3)
        """Window loop"""
        self.window.mainloop()


if __name__ == "__main__":
    x = Program()
    x.main()

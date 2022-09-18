from tkinter import *


class Program:
    def __init__(self):
        """Window"""
        self.window = Tk()
        self.window.title('2/10 calculator')
        self.window.resizable(width=False,height=False)
        """Vars"""
        self.var = IntVar()
        self.var1 = IntVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()
        """Widgets"""
        self.inpt = Entry(textvariable=self.var, justify=CENTER, font=('Arial', 15))
        self.inpt.grid(column=0, row=0)

        self.inpt1 = Entry(textvariable=self.var1, justify=CENTER, font=('Arial', 15))
        self.inpt1.grid(column=1, row=0)

        self.lbl = Label(justify=CENTER, text='Result', wraplength=False, padx=50, font=('Arial', 15))
        self.lbl.grid(column=2, row=1)

        self.lbl1 = Label(justify=CENTER, text='0', wraplength=False, padx=50, font=('Arial', 15))
        self.lbl1.grid(column=2, row=2)

        self.rbtn = Radiobutton(text='From base 10', variable=self.var2, value=1, font=('Arial', 15))
        self.rbtn.grid(column=0, row=1)

        self.rbtn1 = Radiobutton(text='From base 2', variable=self.var2, value=0, font=('Arial', 15))
        self.rbtn1.grid(column=1, row=1)

        self.rbtn2 = Radiobutton(text='To base 10', variable=self.var3, value=1, font=('Arial', 15))
        self.rbtn2.grid(column=0, row=2)

        self.rbtn3 = Radiobutton(text='To base 2', variable=self.var3, value=0, font=('Arial', 15))
        self.rbtn3.grid(column=1, row=2)

        self.countbtn = Button(text='Count result', padx=160, font=('Arial', 15), command=self.count_result)
        self.countbtn.grid(column=0, row=3, columnspan=2)
        """Window loop"""
        self.window.mainloop()

    def count_sum(self):
        if self.var2.get():
            """sum from base 10"""
            return self.var.get() + self.var1.get()
        else:
            """sum from base 2"""
            return self.to_base2(self.to_base10(self.var.get()) + self.to_base10(self.var1.get()))

    def count_result(self):
        if self.var3.get():
            self.lbl1.config(text=self.count_sum())
        else:
            if self.check_base():
                self.lbl1.config(text=self.to_base2(self.count_sum()))
            else:
                print('NaN')

    def check_base(self):
        for i in self.var.get(), self.var1.get():
            print(i)
            if i != '0' or i != '1':
                return False
            return True

    def to_base2(self, a):
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
        a = str(a)
        k = 0
        for i in range(len(a)):
            k += int(a[len(a) - i - 1]) * int(2 ** i)
        return k

    def main(self):
        pass


if __name__ == "__main__":
    x = Program()

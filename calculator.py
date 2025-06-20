import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')

        # Create display
        self.display = ttk.Entry(root, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4,
                          padx=5, pady=5, sticky='nsew')

        # Button layout
        self.create_buttons()

        # Configure grid
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row = 1
        col = 0

        for button in button_texts:
            if button == 'C':
                ttk.Button(self.root, text=button, command=lambda: self.clear()).grid(
                    row=5, column=0, columnspan=4, sticky='nsew')
            else:
                ttk.Button(self.root, text=button,
                           command=lambda x=button: self.button_click(x)).grid(
                    row=row, column=col, sticky='nsew', padx=2, pady=2)
                col += 1
                if col > 3:
                    col = 0
                    row += 1

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

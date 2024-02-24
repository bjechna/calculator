import tkinter as tk
import tkinter.font as tkfont


def write(char):
    entry.config(state="normal")
    entry.insert(tk.INSERT, char)
    entry.config(state="disabled")


def cls():
    entry.config(state="normal")
    entry.delete('1.0', tk.END)
    entry.config(state="disabled")


def equal():
    solution = eval(entry.get('1.0', tk.END))
    cls()
    write(solution)


def backspace():
    newtext = entry.get('1.0', tk.END)[:-2]
    cls()
    write(newtext)


root = tk.Tk()
root.geometry("327x429")
root.title("Calculator")
root.resizable(False, False)

buttons = {"(": ")",
           ")": ")",
           "CLS": cls,
           "BACK": backspace,
           "7": "7",
           "8": "8",
           "9": "9",
           "/": "/",
           "4": "4",
           "5": "5",
           "6": "6",
           "*": "*",
           "1": "1",
           "2": "2",
           "3": "3",
           "-": "-",
           "0": "0",
           ",": ".",
           "=": equal,
           "+": "+"}

buttonsize = 9
entryfont = tkfont.Font(size=28)
buttonfont = tkfont.Font(size=10)
bg = "darkgray"
specialbg = "orange"

mainframe = tk.Frame(root, bg="gray")
mainframe.pack(fill="both", expand=True)

entryframe = tk.Frame(mainframe, height=50)
entryframe.pack(fill="both")
entryframe.grid_propagate(False)


entry = tk.Text(entryframe, state="disabled", font=entryfont, cursor="arrow")
entry.grid()

# Buttons
buttonframe = tk.Frame(mainframe, bg="red")
buttonframe.pack(fill="both")

for key, value in buttons.items():
    if isinstance(value, str):
        button = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text=key, bg=specialbg, font=buttonfont, command=lambda: write(value))
    else:
        button = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text=key, bg=specialbg, font=buttonfont, command=value)
    button.pack()


root.mainloop()
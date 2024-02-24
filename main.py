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
    pass


root = tk.Tk()
root.geometry("350x550")
root.title("Calculator")
root.resizable(False, False)

buttonsize = 8
entryfont = tkfont.Font(size=28)
buttonfont = tkfont.Font(size=10)

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


button1 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="(", font=buttonfont, command=lambda: write("("))
button1.grid(row=0, column=0)

button2 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text=")", font=buttonfont, command=lambda: write(")"))
button2.grid(row=0, column=1)

button3 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="CLS", font=buttonfont, command=cls)
button3.grid(row=0, column=2)

button4 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="BACK", font=buttonfont, command=backspace)
button4.grid(row=0, column=3)

button5 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="7", font=buttonfont, command=lambda: write("7"))
button5.grid(row=1, column=0)

button6 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="8", font=buttonfont, command=lambda: write("8"))
button6.grid(row=1, column=1)

button7 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="9", font=buttonfont, command=lambda: write("9"))
button7.grid(row=1, column=2)

button8 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="/", font=buttonfont, command=lambda: write("/"))
button8.grid(row=1, column=3)

button9 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="4", font=buttonfont, command=lambda: write("4"))
button9.grid(row=2, column=0)

button10 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="5", font=buttonfont, command=lambda: write("5"))
button10.grid(row=2, column=1)

button11 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="6", font=buttonfont, command=lambda: write("6"))
button11.grid(row=2, column=2)

button12 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="*", font=buttonfont, command=lambda: write("*"))
button12.grid(row=2, column=3)

button13 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="1", font=buttonfont, command=lambda: write("1"))
button13.grid(row=3, column=0)

button14 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="2", font=buttonfont, command=lambda: write("2"))
button14.grid(row=3, column=1)

button15 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="3", font=buttonfont, command=lambda: write("3"))
button15.grid(row=3, column=2)

button16 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="-", font=buttonfont, command=lambda: write("-"))
button16.grid(row=3, column=3)

button17 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="0", font=buttonfont, command=lambda: write("0"))
button17.grid(row=4, column=0)

button18 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text=",", font=buttonfont, command=lambda: write(","))
button18.grid(row=4, column=1)

button19 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="=", font=buttonfont, command=equal)
button19.grid(row=4, column=2)

button20 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="+", font=buttonfont, command=lambda: write("+"))
button20.grid(row=4, column=3)

root.mainloop()
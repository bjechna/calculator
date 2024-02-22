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

root.mainloop()
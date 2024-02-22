import tkinter as tk
import tkinter.font as tkfont

def write(char):
    entry.config(state="normal")
    entry.insert(tk.INSERT, char)
    entry.config(state="disabled")


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

buttonframe = tk.Frame(mainframe, bg="red")
buttonframe.pack()

button1 = tk.Button(buttonframe, height=int(buttonsize/2), width=buttonsize, text="(", font=buttonfont, command=lambda: write("("))
button1.grid(row=0, column=0)

root.mainloop()
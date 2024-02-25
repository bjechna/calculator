import tkinter as tk  # Importing tkinter
import tkinter.font as tkfont  # Importing fonts for tkinter


def write(char):  # Function for entering characters to entry
    entry.config(state="normal")  # Setting entry state to normal so I can modify it
    entry.insert(tk.INSERT, char)  # Adding character
    entry.config(state="disabled")  # Setting entry state back to disabled


def cls():  # Function for clearing entry
    entry.config(state="normal")  # Setting entry state to normal so I can modify it
    entry.delete('1.0', tk.END)  # Deleting all text inside entry
    entry.config(state="disabled")  # Setting entry state back to disabled


def equal():  # Function for displaying solution
    try:  # Error handling
        solution = eval(entry.get('1.0', tk.END))  # Getting text from entry and solve it
        cls()  # Clearing entry
        write(solution)  # Writing solution in entry
    except SyntaxError:  # Checking if there is syntax error
        cls()  # Clearing entry
        write("ERROR")  # Writing error in entry


def backspace():  # Function for deleting last character from entry
    newtext = entry.get('1.0', tk.END)[:-2]  # Getting text from entry without last character
    cls()  # Clearing entry
    write(newtext)  # Writing new text in entry


def create_button(key, value, row, column):  # Function for creating button
    specialkeys = ["CLS", "BACK", "(", ")", "-", "+", "*", "/", "="]  # Keys that will have different color
    bg = "darkgray"  # Setting standard background color
    if key in specialkeys:  # Checking if key is special. If so, background color will be orange
        bg = "orange"  # Changing background color to orange

    if isinstance(value, str):  # Checking if value of key is string. If yes button will do write() function, else it will do different function
        button = tk.Button(buttonframe,  # Creating button in buttonframe
                           height=int(buttonsize/2),  # Setting button height
                           width=buttonsize,  # Setting button width
                           text=key,  # Setting button text
                           bg=bg,  # Setting button background color
                           font=buttonfont,  # Setting font of text in button
                           command=lambda: write(value))  # Writing in entry value
    else:
        button = tk.Button(buttonframe,  # Creating button in buttonframe
                           height=int(buttonsize/2),  # Setting button height
                           width=buttonsize,  # Setting button width
                           text=key,  # Setting button text
                           bg=bg,  # Setting button background color
                           font=buttonfont,  # Setting font of text in button
                           command=value)  # Doing specific for this button function

    button.grid(row=row, column=column)  # Griding button in buttonframe


root = tk.Tk()  # Creating window
root.geometry("327x429")  # Setting window geometry
root.title("Calculator")  # Setting window title
root.resizable(False, False)  # Turning off window resize

# Creating buttons dictionary {"Text in button": "What it will write"/Specific function}
buttons = {"(": "(",
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

buttonsize = 9  # Setting button size
entryfont = tkfont.Font(size=28)  # Setting font for entry
buttonfont = tkfont.Font(size=10)  # Setting font for buttons

mainframe = tk.Frame(root, bg="gray")  # Creating frame which will cover all window
mainframe.pack(fill="both", expand=True)  # Packing mainframe

entryframe = tk.Frame(mainframe, height=50)  # Creating frame for entry
entryframe.pack(fill="both")  # Packing entryframe
entryframe.grid_propagate(False)  # Turning off grid propagate


entry = tk.Text(entryframe, state="disabled", font=entryfont, cursor="arrow")  # Creating entry as Text object
entry.grid()  # Griding entry

# Buttons
buttonframe = tk.Frame(mainframe, bg="red")  # Creating frame for buttons
buttonframe.pack(fill="both")  # Packing buttonframe

row = 0  # Setting row for button that will be created
column = 0  # Setting column for button that will be created
for key, value in buttons.items():  # Loop for each key and value in buttons dictionary
    create_button(key, value, row, column)  # Creating button
    column += 1  # Incrementing column variable so next button will be gridded next to the previous one
    if column > 3:  # Checking if column variable is more than 3. If true then set column to 0 and increment row
        column = 0  # Changing column variable to 0 so next button will be on left side of button frame
        row += 1  # Incrementing row variable so there will be next row for buttons

root.mainloop()  # Enabling window

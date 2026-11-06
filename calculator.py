
import tkinter as tk
import math

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("360x540")
root.resizable(False, False)
root.configure(bg="#202124")

expression = ""

def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        allowed = {
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "pi": math.pi,
            "e": math.e
        }

        result = eval(expression, {"__builtins__": {}}, allowed)
        history.append(f"{expression} = {result}")
        expression = str(result)
        display_var.set(expression)

    except Exception:
        display_var.set("Invalid Expression")
        expression = ""

def scientific(function):
    global expression
    expression += function + "("
    display_var.set(expression)

def history_window():
    window = tk.Toplevel(root)
    window.title("Calculation History")
    window.geometry("350x300")

    tk.Label(window, text="Calculation History",
             font=("Arial", 15, "bold")).pack(pady=10)

    history_list = tk.Listbox(window, width=42, height=12)
    history_list.pack(padx=10, pady=10)

    for item in history:
        history_list.insert(tk.END, item)

display_var = tk.StringVar()
history = []

display = tk.Entry(root, textvariable=display_var,
                   font=("Arial", 22), justify="right",
                   bd=10, relief="flat")
display.pack(fill="x", padx=12, pady=15, ipady=12)

buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "⌫"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "=", "+", ")"],
    ["sqrt", "sin", "cos", "tan", "log"],
    ["pi", "e", "^", "%", "History"]
]

def handle_button(value):
    if value == "C":
        clear()
    elif value == "⌫":
        backspace()
    elif value == "=":
        calculate()
    elif value == "History":
        history_window()
    elif value in ["sqrt", "sin", "cos", "tan", "log"]:
        scientific(value)
    elif value == "pi":
        press("pi")
    elif value == "e":
        press("e")
    elif value == "^":
        press("**")
    elif value == "%":
        press("/100")
    else:
        press(value)

button_frame = tk.Frame(root, bg="#202124")
button_frame.pack(padx=8, pady=5)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 12, "bold"),
            width=6,
            height=2,
            bg="#3c4043",
            fg="white",
            activebackground="#5f6368",
            command=lambda v=value: handle_button(v)
        )
        button.grid(row=r, column=c, padx=3, pady=4)

root.mainloop() 

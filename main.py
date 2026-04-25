import tkinter as tk

# Function to update display
def press(num):
    expression.set(expression.get() + str(num))

# Function to evaluate expression
def equalpress():
    try:
        total = str(eval(expression.get()))
        expression.set(total)
    except:
        expression.set("Error")

# Function to clear
def clear():
    expression.set("")

# Main window
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.configure(bg="#1e1e1e")

expression = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, relief="flat",
                 bg="#2d2d2d", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Button style
btn_color = "#3c3f41"
operator_color = "#ff9500"
equal_color = "#28a745"

def create_button(text, row, col, color, command):
    tk.Button(root, text=text, fg="white", bg=color,
              font=('Arial', 14), width=5, height=2,
              command=command).grid(row=row, column=col, padx=5, pady=5)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text in ['+', '-', '*', '/']:
        create_button(text, row, col, operator_color, lambda t=text: press(t))
    elif text == 'C':
        create_button(text, row, col, "#dc3545", clear)
    else:
        create_button(text, row, col, btn_color, lambda t=text: press(t))

# Equal button
tk.Button(root, text='=', fg="white", bg=equal_color,
          font=('Arial', 14), width=22, height=2,
          command=equalpress).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
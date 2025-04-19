import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Entry widget for input/output
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the entry
def click(button_text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + button_text)

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Clear button
clear_btn = tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Make grid expand with window
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

# Run the application
window.mainloop()

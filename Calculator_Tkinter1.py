import tkinter as tk
from tkinter import *
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == '%':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 % num2
        
        result_label.config(text=f"Result: {result}", fg="green")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
# Create main window
root = tk.Tk()
root.title("Simple Calculator")
# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=20)
# Create entry widgets
entry1 = tk.Entry(input_frame, width=10)
entry1.grid(row=0, column=0, padx=10)
entry2 = tk.Entry(input_frame, width=10)
entry2.grid(row=0, column=1, padx=10)
# Create operation dropdown
operations = ['+', '-', '*', '/', '%']
operation_var = tk.StringVar()
operation_dropdown = tk.OptionMenu(input_frame, operation_var, *operations)
operation_dropdown.grid(row=0, column=2, padx=10)
# Create calculate button
calculate_button = tk.Button(input_frame, text="Calculate", command=calculate, bg="blue", fg="white")
calculate_button.grid(row=0, column=3, padx=10)
# Create result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="green")
result_label.pack(pady=20)
root.mainloop()

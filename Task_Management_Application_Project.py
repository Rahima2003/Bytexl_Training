import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x400")

        self.tasks = []

        # Create UI elements
        self.title_label = ttk.Label(root, text="Task Manager", font=("Arial", 20))
        self.title_label.pack(pady=20)

        self.task_entry = ttk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.deadline_entry = ttk.Entry(root, width=30)
        self.deadline_entry.pack(pady=10)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=20)

        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.show_tasks()

    def add_task(self):
        task = self.task_entry.get()
        deadline = self.deadline_entry.get()

        if task and deadline:
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                self.tasks.append((task, deadline))
                self.show_tasks()
                self.task_entry.delete(0, tk.END)
                self.deadline_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
        else:
            messagebox.showerror("Error", "Task and deadline fields cannot be empty.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.show_tasks()
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task, deadline in self.tasks:
            self.task_listbox.insert(tk.END, f"{task} - Due: {deadline}")

# Create Tkinter window
root = tk.Tk()
app = TaskManagerApp(root)

# Set background color
root.configure(bg='#e6e6e6')

# Run the Tkinter event loop
root.mainloop()

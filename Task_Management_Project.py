# Initialize task data
tasks = []

# Function to add a new task
def add_task(title, description, due_date, category):
    tasks.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'category': category,
        'completed': False
    })
    print("Task added successfully!")

# Function to mark a task as complete
def mark_task_complete(title):
    for task in tasks:
        if task['title'] == title:
            task['completed'] = True
            print("Task marked as complete!")
            return
    print("Task not found.")

# Function to set a reminder for a task
def set_reminder(title, reminder):
    for task in tasks:
        if task['title'] == title:
            task['reminder'] = reminder
            print("Reminder set successfully!")
            return
    print("Task not found.")

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task in tasks:
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}, Category: {task['category']}, Status: {status}")

# Main function
def main():
    while True:
        print("\n1. Add Task\n2. Mark Task as Complete\n3. Set Reminder\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            category = input("Enter task category: ")
            add_task(title, description, due_date, category)
        elif choice == '2':
            title = input("Enter task title to mark as complete: ")
            mark_task_complete(title)
        elif choice == '3':
            title = input("Enter task title to set a reminder: ")
            reminder = input("Enter reminder date and time (YYYY-MM-DD HH:MM): ")
            set_reminder(title, reminder)
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


    



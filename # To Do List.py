import os
import datetime
import tkinter as tk

# Suppress the Tkinter deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

def add_task():
    task = task_input.get()
    if task != "": 
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("ToDoList_rafi.txt", "a") as f:
            f.write(f"{date_time} - {task}\n")
        task_input.delete(0, tk.END)
        display_tasks()
    else:
        output_label.config(text="Task cannot be empty.")

def delete_task():
    index = int(index_input.get()) - 1
    try:
        with open("ToDoList_rafi.txt", "r") as f:
            lines = f.readlines()
        if index < 0 or index >= len(lines):
            raise IndexError
        with open("ToDoList_rafi.txt", "w") as f:
            for i, line in enumerate(lines):
                if i != index:
                    f.write(line)
        index_input.delete(0, tk.END)
        display_tasks()
    except IndexError:
        output_label.config(text="Invalid index. Please enter a valid index.")

def display_tasks():
    try:
        with open("ToDoList_rafi.txt", "r") as f:
            task_list.delete(0, tk.END)
            for index, line in enumerate(f):
                task_list.insert(tk.END, f"{index+1}. {line.rstrip()}")
        output_label.config(text="To-Do List:")
    except FileNotFoundError:
        output_label.config(text="To-Do List is empty.")

# Create the GUI
root = tk.Tk()
root.title("To Do List")

# Create widgets
task_label = tk.Label(root, text="Task:")
task_input = tk.Entry(root, width=100)
add_button = tk.Button(root, text="Add Task", command=add_task)
index_label = tk.Label(root, text="Index:")
index_input = tk.Entry(root, width=100)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
output_label = tk.Label(root)
task_list = tk.Listbox(root, width=100, height=20)

# Pack widgets
task_label.pack()
task_input.pack()
add_button.pack()
index_label.pack()
index_input.pack()
delete_button.pack()
output_label.pack()
task_list.pack()

# Display the GUI
display_tasks()
root.mainloop()

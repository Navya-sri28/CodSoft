import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x600")
        self.root.config(bg="#87CEEB")  # Sky Blue background

        self.tasks = []
        self.completed_tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18), bg="#87CEEB")
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=40, font=("Helvetica", 14), bg="#e8e8e8")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#d0d0d0")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=15, font=("Helvetica", 14), bg="#ffffff", selectbackground="#d0d0d0")
        self.task_listbox.pack(pady=10)

        self.mark_complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_complete, bg="#d0f0c0")
        self.mark_complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ffcccb")
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, bg="#add8e6")
        self.save_button.pack(pady=5)

        self.load_tasks()
        self.update_task_count()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def mark_task_complete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks.pop(selected_task_index)
            self.completed_tasks.append(completed_task)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
        self.update_task_count()

    def update_task_count(self):
        total_tasks = len(self.tasks) + len(self.completed_tasks)
        completed_tasks = len(self.completed_tasks)
        self.title_label.config(text=f"To-Do List - Total: {total_tasks}, Completed: {completed_tasks}")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task}\n")
            for task in self.completed_tasks:
                f.write(f"[Completed] {task}\n")
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    if task.startswith("[Completed] "):
                        self.completed_tasks.append(task[len("[Completed] "):])
                    else:
                        self.tasks.append(task)
            self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

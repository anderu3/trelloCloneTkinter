import tkinter as tk
from tkinter import simpledialog

windowBackgroundColor = "#87CEFA"
topTextBackgroundColor = "#B0E0E6"

class AddTask(tk.Frame):
    def __init__(self, window, list_name):
        super().__init__(window, bg=windowBackgroundColor, padx=5, pady=5, bd=2, relief=tk.FLAT)
        self.window = window
        self.list_name = list_name
        self.create_task_button()

    def create_task_button(self):
        title_label = tk.Label(self, text=self.list_name, bg=windowBackgroundColor, font=("Calibri", 12, "bold"))
        title_label.pack(anchor=tk.W)

        add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        add_task_button.pack(anchor=tk.W, pady=5)

        self.bind("<Key>", self.add_task)

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter name of new task:")
        task_module = tk.Label(self, text=task_name, bg=topTextBackgroundColor, padx=5, pady=5, bd=2, relief=tk.GROOVE)
        task_module.pack(anchor=tk.W, padx=5, pady=5)

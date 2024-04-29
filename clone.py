import tkinter as tk
from tkinter import simpledialog
from addtaskmodule import AddTask

windowBackgroundColor = "#87CEFA"
topTextBackgroundColor = "#B0E0E6"

class TrelloClone:
    def __init__(self, window):
        self.window = window
        self.window.title("Trello Clone Project")
        self.lists = []

        add_list_button = tk.Button(self.window, text="Add a List", command=self.add_list)
        add_list_button.pack(side=tk.LEFT, padx=7.5, pady=7.5)

    def add_list(self):
        list_name = simpledialog.askstring("Add a List", "Enter name of new list:")
        new_list_addition = AddTask(self.window, list_name)
        self.lists.append(new_list_addition)
        new_list_addition.pack(side=tk.LEFT, anchor=tk.NW, padx=7.5, pady=7.5)
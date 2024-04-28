import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import messagebox

# Modular variables
windowBackgroundColor = "#87CEFA"
topTextBackgroundColor = "#B0E0E6"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# Create window widget
window = tk.Tk()
window.title("Trello Clone Project")
window.configure(background=windowBackgroundColor)
# Open window in center of the screen with 1200x800 dimensions, changable line 5-6
screen_x = int((window.winfo_screenwidth() / 2) - WINDOW_WIDTH / 2)
screen_y = int((window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_x}+{screen_y}')

# Create empty background to imitate Trello color gradient
title_frame = tk.Frame(window, bg=topTextBackgroundColor, bd=0, relief=tk.SOLID)
title_frame.pack(fill=tk.X)

# Text on top
title_card = tk.Label(title_frame, text="Trello Clone Project Board", font=("Calibri", 24), bg=topTextBackgroundColor, fg="black")
title_card.pack(pady=10)
    
def add_list():
    new_list_name = tk.simpledialog.askstring("Add a list", "Enter the name of the new list:")
    if new_list_name:
        list_frame = tk.Frame(board_frame, bg="lightgray", padx=5, pady=5, bd=2, relief=tk.RAISED)
        list_label = tk.Label(list_frame, text=new_list_name, bg="lightgray", font=("Helvetica", 12, "bold"))
        list_label.grid(row = 1, column = 1)
        # list_label.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.X)
        list_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.Y)
    else:
        messagebox.showwarning("Warning", "List name cannot be empty!")

board_frame = tk.Frame(window, bg="white")
board_frame.pack(fill=tk.BOTH, expand=True)

add_list_button = tk.Button(board_frame, text="Add a list...", command=add_list)
add_list_button.pack(side=tk.LEFT, padx=10, pady=10)
   

























window.mainloop()
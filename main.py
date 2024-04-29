import tkinter as tk
from clone import TrelloClone

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
windowBackgroundColor = "#87CEFA"
topTextBackgroundColor = "#B0E0E6"

window = tk.Tk()
window.configure(bg=windowBackgroundColor)
screen_x = int((window.winfo_screenwidth() / 2) - WINDOW_WIDTH / 2)
screen_y = int((window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{screen_x}+{screen_y}')

title_frame = tk.Frame(window, bg=topTextBackgroundColor, bd=0, relief=tk.SOLID)
title_frame.pack(fill=tk.X)

title_card = tk.Label(title_frame, text="Trello Clone Project Board", font=("Calibri", 24), bg=topTextBackgroundColor, fg="black")
title_card.pack(pady=10)

trello_clone = TrelloClone(window)



window.mainloop()

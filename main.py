import tkinter as tk

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




























window.mainloop()
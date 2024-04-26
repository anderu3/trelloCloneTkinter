import tkinter as tk

windowBackgroundColor = "#87CEFA"
topTextBackgroundColor = "#B0E0E6"


window = tk.Tk()
window.title("Trello Clone Project")
window.configure(background=windowBackgroundColor)
window.geometry("1200x800+700+250")


title_frame = tk.Frame(window, bg=topTextBackgroundColor, bd=0, relief=tk.SOLID)
title_frame.pack(fill=tk.X)

title_card = tk.Label(title_frame, text="Trello Clone Project Board", font=("Calibri", 24), bg=topTextBackgroundColor, fg="black")
title_card.pack(pady=10)





























window.mainloop()

# Imports 

import tkinter as tk
import time

# Adding Time 

def update_time():
	current = time.strftime("%H:%M:%S")
	label.config(text=current)
	window.after(1000, update_time)


# Window Configuration 

window = tk.Tk()
window.overrideredirect(True)
window.geometry("300x200")
window.configure(bg="black")

# Time Font And Color Settigns 

label = tk.Label(
     window,
     font=(" Code New Roman ", 32), bg="black", fg="lime", anchor="center")
     
     
label.pack(expand=True)

# Quit Button Functions And Styling 

quit_button= tk.Button(
    window, 
    text="Quit", 
    font=("Code New Roman", 16),
    bg="black",
    fg="lime",
    command= window.destroy,
    )
    
quit_button.pack(pady=10)

# Ending Functions 

update_time()

window.mainloop()



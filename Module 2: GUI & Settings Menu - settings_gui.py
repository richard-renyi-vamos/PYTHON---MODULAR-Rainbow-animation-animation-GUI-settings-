# settings_gui.py
import tkinter as tk
from tkinter import simpledialog
import rainbow_animation  # This imports the rainbow animation module

def change_radius():
    new_radius = simpledialog.askinteger("Input", "Set new radius for the rainbow:",
                                         parent=root, minvalue=100, maxvalue=300)
    if new_radius:  # If a new radius was provided
        global radius
        radius = new_radius
        # Here, you might want to update the rainbow_animation module's radius
        # This requires modifying the rainbow_animation module to allow changing the radius

root = tk.Tk()
root.title("Rainbow Animation Settings")

change_radius_btn = tk.Button(root, text="Change Radius", command=change_radius)
change_radius_btn.pack()

root.mainloop()

from plyer import battery
import tkinter as tk
from tkinter import Menu

def update_battery_label():
    battery_info = battery.status
    percentage = battery_info.get("percentage","N/A")
    plugged = battery_info.get("plugged", "N/A")
    battery_label.config(text=f"Battery Percentage: {percentage}%\nPlugged: {plugged}")

    


screen = tk.Tk()
screen.title('Battery')

# create a menubar
menubar = Menu(screen)
screen.config(menu=menubar)

# create a menu

file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=screen.destroy
)


# add the File menu to the menubar
menubar.add_cascade(
    label='File',
    menu=file_menu
)

# create a label to display battery info
battery_label = tk.Label(screen, text="Battery Percentage: N/A%\nPlugged: N/A")
battery_label.pack()

# update the battery label initially
update_battery_label()

# update the battery label every 10 seconds
screen.after(10000, update_battery_label)
screen.mainloop()

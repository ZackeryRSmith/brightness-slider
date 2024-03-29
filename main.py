import tkinter as tk
from tkinter import ttk
from os import system, popen

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Adjust brightness')

MIN=0.2
global SCREEN

# slider current value
current_value = tk.DoubleVar()

def getmonitors() -> list:
    """ Gets the monitor names using xrandr """

    # gets the command output
    output = popen("xrandr --listmonitors").read()

    # filters through the command output to get only the names
    lines = [line for line in output.split("\n")[1:-1] ]
    monitors = [line.split(" ")[-1] for line in lines]

    return monitors

def get_current_value(): return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    value_label.configure(text=get_current_value())
    system(f"xrandr --output {chosen.get()} --brightness {get_current_value()}")

screens, chosen = getmonitors(), tk.StringVar()
chosen.set(screens[0])

# Create dropdown
menu = tk.OptionMenu(root, chosen, *screens)
menu.grid(
        column=2,
        row=1
)

# label for the slider
slider_label = ttk.Label(
    root,
    text='Slider:'
)
slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
slider = ttk.Scale(
    root,
    from_=MIN,
    to=1,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)
slider.grid(
    column=1,
    row=0,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    root,
    text='Brightness multiplier: '
)
current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

if __name__ == "__main__":
    root.mainloop()

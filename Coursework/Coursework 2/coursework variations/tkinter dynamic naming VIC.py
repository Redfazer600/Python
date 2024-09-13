from tkinter import *

window = Tk()

widget_list = []
variable_list = []


for i in range(5):
    string_variable = StringVar()
    string_variable.set(f'{i}')
    variable_list.append(string_variable)

for i in range(5):
    label = Label(
        window,
        textvariable=variable_list[i]
    )
    widget_list.append(label)
    label.pack()

window.mainloop()

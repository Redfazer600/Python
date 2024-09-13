from tkinter import *

window = Tk()

widgetList = []

for i in range(5):
    widgetRow = []

    textlabel = Label(window, text='hello')
    textlabel.grid(row=i, column=0)
    widgetRow.append(textlabel)

    toggleButton = Button(window, text='toggle button', command=lambda: print('Button Toggled :D'))
    toggleButton.grid(row=i, column=1)
    widgetRow.append(toggleButton)

    editButton = Button(window, text='edit button', command=lambda: print('Button edited'))
    editButton.grid(row=i, column=2)
    widgetRow.append(editButton)

    removeButton = Button(window, text='remove button', command=lambda: print('button removed'))
    removeButton.grid(row=i, column=3)
    widgetRow.append(removeButton)

    widgetList.append(widgetRow)


for widgetRow in widgetList:
        widgetRow[3].config(command=lambda: print('IT FUCKING WORKS'))


window.mainloop()


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
#
# for sublist in my_list:
#     sublist[2] = 999
#
# print(my_list)

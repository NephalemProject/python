from tkinter import *
from backend import Database

database = Database()

# functions

def get_selected(event):
    global selected
    if l1.curselection():
        index = l1.curselection()[0]
        selected = l1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[2])
        e3.delete(0, END)
        e3.insert(END, selected[3])
        e4.delete(0, END)
        e4.insert(END, selected[4])

def view_command():
    l1.delete(0, END)
    for row in database.view():
        l1.insert(END, row)

def search_command():
    l1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        l1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    database.delete(selected[0])
    view_command()

def update_command():
    database.update(selected[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

window = Tk()

window.wm_title("Book Database")
window.resizable(False, False)

#labels

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

# entries

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

# listbox

l1 = Listbox(window, width = 35, height = 6)
l1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2, sticky=(N,W,E,S))

# scrollbar

sb1 = Scrollbar(window)
sb1.grid(row = 3, column = 2, sticky=(N,S))
l1.configure(yscrollcommand = sb1.set)
sb1.configure(command = l1.yview)

# bind

l1.bind('<<ListboxSelect>>', get_selected)

# buttons

b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Find Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Remove Selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()

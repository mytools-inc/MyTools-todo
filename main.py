''' 
    __author__: "Aleksa Maletic, MyTools"
    __copyright__: "Copyright 2019, MyTools"
    __credits__: "Aleksa Maletic"

    __maintainer__: "Aleksa Maletic"
    __email__: "mytools@gmail.com"
    __version__: "1.0"
    __status__: "Production"
    
'''
from tkinter import *
import tkinter as ttk
import tkinter.messagebox

main_window = ttk.Tk()                          
main_window.title("Your daily to do tasks>")
main_window.geometry("450x490")
main_window.configure(background = "#1a2228")
main_window.resizable(False, False) #prozor ne moze promjeniti velicinu
main_window.iconbitmap(r"favicon.ico")

#lista todoa(task-ova) [TEST]
list_todoa = []
#list_todoa = ["@"]

def show_help1():
    v_info = ("\nThis app is created by Aleksit0(Github).\nIt is made in Python 3.7 using tkinter(ttk, a library for Graphical User Interface or GUI.")
    show_help = tkinter.messagebox.showinfo("CONTACT/INFO", "If you found this app good contact me on:\n~Github(Aleksit0)" + v_info)

btn_show_help = ttk.Button(main_window, text = "CONTACT", background = "#3CB371", foreground = "black", activebackground = "#FF851B", relief = "sunken", border = 0, command = show_help1)
btn_show_help.place(x = 65, y = 440)
#lista todoa(task-ova)
listbox_todoa = ttk.Listbox(main_window, background = "#edece6", foreground = "black")
listbox_todoa.place(x = 65, y = 230, width = 320, height = 200)

#blank label
blank_label = Label(main_window, text = "Enter to do: ", background = "#1a2228", foreground = "white")
blank_label.place(x = 180, y = 140)

def update_listu_todoa():
    #onemoguci dodavanje istih todoa
    #delete_todo()
    #dodavanje todoa u listu
    for todo in list_todoa:
        listbox_todoa.insert(ttk.END, todo)
#dugme dodaj todo(task)

def add_todo():
    #dobijamo value entrija
    todo = unos_todoa.get()
    #if statement za prazan prostor
    if todo != "":
        #dodavanje u listu
        listbox_todoa.insert(ttk.END, todo)
        #update listbox
        update_listu_todoa()
    else:
        blank_label["text"] = "Please enter a task!"
    unos_todoa.delete(0, ttk.END)

dodaj_todo = ttk.Button(main_window, text = "Add todo", background = "#3CB371", foreground = "black", activebackground = "#FF851B", relief = "sunken", command = add_todo, border = 0)
dodaj_todo.place(x = 70, y = 40, width = 150, height = 100)

#dugme ukloni jedan todo(task)


def delete_one_todo():
    listbox_todoa.delete(ttk.ANCHOR)

def delete_all_todos():
    confirmed = tkinter.messagebox.askyesno("Confirm", "Do you really want to delete all tasks?")
    if confirmed == True:
        listbox_todoa.delete(0, ttk.END)

ukloni_todo = ttk.Button(main_window, text = "Delete todo", background = "#3CB371", foreground = "black", activebackground = "#FF851B", relief = "sunken", command = delete_one_todo, border = 0)
ukloni_todo.place(x = 230, y = 40, width = 150, height = 100)

#dugme ukloni sve todo-e(task-ove)
ukloni_sve = ttk.Button(main_window, text = "Clear all", background = "#3CB371", foreground = "black", activebackground = "#FF851B", relief = "sunken", command = delete_all_todos, border = 0)
ukloni_sve.place(x = 327,y = 200)

#unos todo-a(task-a)
unos_todoa = Entry(main_window, background = "#edece6")
#unos_todoa.get()
unos_todoa.place(x = 98, y = 165, width = 250, height = 30)

#todo label
label_lista_todoa = Label(main_window, text = "Your todos: ", background = "#1a2228", foreground = "white")
label_lista_todoa.place(x = 180, y = 200)

main_window.mainloop()
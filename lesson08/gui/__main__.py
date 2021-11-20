from tkinter import Tk, Button, StringVar, Entry, Menu, Listbox, END, messagebox
from tkinter import filedialog as fd

from lesson07.kmda import user_helper
from lesson07.kmda.user_list import UserList


class Win:
    def __init__(self):
        self.win = Tk()
        self.win.title("First window")
        self.win.geometry("400x500+100+100")
        self.message_text1 = StringVar()
        self.message_text1.set("enter value")
        self.message_text2 = StringVar()
        self.message_text2.set("enter value")
        self.message_text3 = StringVar()
        self.message_text3.set("enter op")
        self.message_text4 = StringVar()
        self.message_text4.set("result")
        btn1 =Button(self.win, text="show", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        btn2 =Button(self.win, text="read", command=self.btn_read_click)
        btn2.grid(row=2, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry1 = Entry(textvariable=self.message_text1)
        message_entry1.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry2 = Entry(textvariable=self.message_text2)
        message_entry2.grid(row=2, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry3 = Entry(textvariable=self.message_text3)
        message_entry3.grid(row=3, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry4 = Entry(textvariable=self.message_text4)
        message_entry4.grid(row=4, column=2, ipadx=10, ipady=6, padx=10, pady=10)

        self.languages_listbox = Listbox()
        self.languages_listbox.grid(row=1, rowspan=4, column=3, ipadx=10, ipady=6, padx=10, pady=10)



        file_menu = Menu()
        file_menu.add_command(label="New")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        main_menu = Menu()
        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Edit")
        main_menu.add_cascade(label="View")
        main_menu.add_cascade(label="Calc",command=self.btn_read_click)
        self.win.config(menu=main_menu)


        self.win.mainloop()

    def btn_click(self):
        self.message_text4.set(self.text)

    def btn_read_click(self):
        x = int(self.message_text1.get())
        y = int(self.message_text2.get())
        op = self.message_text3.get()
        if op == "+":
            self.text=x+y;
        elif op == "*":
            self.text=x*y;
        self.message_text4.set(self.text)
        log_text = f"{x} {op} {y} = {self.text}"
        self.languages_listbox.insert(END, log_text)

    def open_file(self):
        name= fd.askopenfilename()
        users = UserList(user_helper.get_users_from_csv(name))
        self.languages_listbox.delete(0,END)
        for user in users.get_users():
            self.languages_listbox.insert(END, user)
        messagebox.showinfo("GUI Python",name)

if __name__ == '__main__':
    my_win = Win()

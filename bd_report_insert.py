import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

db = sqlite3.connect('report.db')
connect = db.cursor()

def add_bd_emloyee():

    root1 = tk.Toplevel()


    def add():
        try:
            connect.execute('''INSERT INTO employees(name, name_latin, code, number_identific) VALUES (?, ?, ?, ?)''',
                        (ent1.get(), ent2.get(), ent3.get(), ent4.get()))
            db.commit()
            tk.messagebox.showinfo("Повідомлення", "Дані успішно внесено в базу даних!")
        except Exception as e:
            tk.messagebox.showerror("Помилка", "Помилка: " + format(e))
        



    lb1 = tk.Label(root1, text="Введіть Ім'я співробітника:")
    lb1.grid(row=0, column=0)

    lb2 = tk.Label(root1, text="Введіть Ім'я співробітника латиницею:")
    lb2.grid(row=1, column=0)

    lb3 = tk.Label(root1, text="Введіть код:")
    lb3.grid(row=2, column=0)

    lb4 = tk.Label(root1, text="Введіть ідентифікаційний номер:")
    lb4.grid(row=3, column=0)

    ent1 = tk.Entry(root1)
    ent1.grid(row=0, column=1)

    ent2 = tk.Entry(root1)
    ent2.grid(row=1, column=1)

    ent3 = tk.Entry(root1)
    ent3.grid(row=2, column=1)

    ent4 = tk.Entry(root1)
    ent4.grid(row=3, column=1)

    btn_add = tk.Button(root1, text='Додати в БД', command=add)
    btn_add.grid(row=4, column=0)

    btn_exit = tk.Button(root1, text='Закрити', command=root1.destroy)
    btn_exit.grid(row=4, column=1)

def add_bd_customers():

    root1 = tk.Toplevel()


    def add():
        try:
            connect.execute('''INSERT INTO customers(name, city) VALUES (?, ?)''',
                        (ent1.get(), ent2.get()))
            db.commit()
            tk.messagebox.showinfo("Повідомлення", "Дані успішно внесено в базу даних!")
        except Exception as e:
            tk.messagebox.showerror("Помилка", "Помилка: " + format(e))
        



    lb1 = tk.Label(root1, text="Введіть назву Замовника:")
    lb1.grid(row=0, column=0)

    lb2 = tk.Label(root1, text="Введіть місце розташування:")
    lb2.grid(row=1, column=0)

    ent1 = tk.Entry(root1)
    ent1.grid(row=0, column=1)

    ent2 = tk.Entry(root1)
    ent2.grid(row=1, column=1)

    btn_add = tk.Button(root1, text='Додати в БД', command=add)
    btn_add.grid(row=2, column=0)

    btn_exit = tk.Button(root1, text='Закрити', command=root1.destroy)
    btn_exit.grid(row=2, column=1)

def add_bd_equipment():

    root1 = tk.Toplevel()


    def add():
        try:
            connect.execute('''INSERT INTO equipment (type, serial_number, customer, type_of_equipment) VALUES (?, ?, ?, ?)''',
                        (ent1.get(), ent2.get(), ent3.get(), ent4.get()))
            db.commit()
            tk.messagebox.showinfo("Повідомлення", "Дані успішно внесено в базу даних!")
        except Exception as e:
            tk.messagebox.showerror("Помилка", "Помилка: " + format(e))
        



    lb1 = tk.Label(root1, text="Введіть назву обладнання:")
    lb1.grid(row=0, column=0)

    lb2 = tk.Label(root1, text="Введіть серійний номер обладнання:")
    lb2.grid(row=1, column=0)

    lb3 = tk.Label(root1, text="Введіть назву Замовника:")
    lb3.grid(row=2, column=0)

    lb4 = tk.Label(root1, text="Виберіть тип обладнання:")
    lb4.grid(row=3, column=0)

    ent1 = tk.Entry(root1)
    ent1.grid(row=0, column=1)

    ent2 = tk.Entry(root1)
    ent2.grid(row=1, column=1)

    ent3 = tk.Entry(root1)
    ent3.grid(row=2, column=1)

    ent4 = ttk.Combobox(root1, values=[
                                    "Сепаратор", 
                                    "Декантер"])
    ent4.grid(row=3, column=1)

    btn_add = tk.Button(root1, text='Додати в БД', command=add)
    btn_add.grid(row=4, column=0)

    btn_exit = tk.Button(root1, text='Закрити', command=root1.destroy)
    btn_exit.grid(row=4, column=1)

def add_bd_norm():

    root1 = tk.Toplevel()


    def add():
        try:
            connect.execute('''replace into norma (day_salary_norm, country) values (?, ?)''',
                          (ent2.get(), ent1.get()))
            db.commit()
            tk.messagebox.showinfo("Повідомлення", "Дані успішно внесено в базу даних!")
        except Exception as e:
            tk.messagebox.showerror("Помилка", "Помилка: " + format(e))

    lb1 = tk.Label(root1, text="Виберіть країну відрядження:")
    lb1.grid(row=0, column=0)

    lb2 = tk.Label(root1, text="Введіть норму добових:")
    lb2.grid(row=1, column=0)

    ent1 = ttk.Combobox(root1, values=[
                                    "по Україні", 
                                    "За межами України"])
    ent1.grid(row=0, column=1)

    ent2 = tk.Entry(root1)
    ent2.grid(row=1, column=1)

    btn_add = tk.Button(root1, text='Додати в БД', command=add)
    btn_add.grid(row=4, column=0)

    btn_exit = tk.Button(root1, text='Закрити', command=root1.destroy)
    btn_exit.grid(row=4, column=1)


import tkinter as tk
from tkinter import ttk
# from tkinter import *
# from tkinter import Menu
from tkinter import messagebox
import autocomplete
import autocomplete_test
import sqlite3
import bd_report_insert
import Calendar
import My_Calendar
from datetime import datetime
import def_report_date_to_db
import printing_files
import createExcel
import formatting_Excel
import word_docs

autocomplete_name = []
arr_report_data = []
arr_payments = []
arr_pay = []
arr_paid_card = []

try:
    db = sqlite3.connect('report.db')
    connect = db.cursor()
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS employees (id integer primary key, name text, name_latin text, code text,             
                number_identific text)''')
    emploees_fetch = connect.execute('''SELECT * FROM employees''')
    try:
        emploees_array_turtle = emploees_fetch.fetchall()
        if emploees_array_turtle:
            autocomplete_name.clear()
            for a in emploees_array_turtle:
                a = list(a)
                del a[0]                
                autocomplete_name.append(a)
            # print(autocomplete_name)
    except Exception as e:
        tk.messagebox.showerror("Помилка", "Помилка: " + format(e))
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS customers (id integer primary key, name text, city text)''')
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS equipment (id integer primary key, type text, serial_number text, customer text, type_of_equipment text)''')
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS payments (id integer primary key, report_code text, date date, description text, sum real, paid_by_card boolean)''')
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS report (id integer primary key, code text, date date, emploee text, date_of_start date, date_of_finish date, 
                days integer, norma_salary_day real, salary_trip real, sum real, sum_paid real, balance real, customer text, city text)''')
    connect.execute(
                '''CREATE TABLE IF NOT EXISTS norma (id integer primary key, day_salary_norm REAL, country text UNIQUE)''')
    select_norma = connect.execute('''SELECT day_salary_norm FROM norma  WHERE country="по Україні"''')
    norma_day = 0.0
    try:
        arr_norma = list(select_norma.fetchone())
        for el in arr_norma:
            norma_day = el
    except Exception as e:
        pass
    select_payments = connect.execute('''SELECT description FROM payments''')
    arr_payments_autocomlete = []
    try:
        arr_payments_fetch = list(select_payments.fetchall())
        arr_payments_autocomlete.clear()
        for el in arr_payments_fetch:
            arr_payments_autocomlete.append(el[0])
        # print(arr_payments_autocomlete)
    except Exception as e:
        tk.messagebox.showerror("Помилка", "Помилка: " + format(e))
    db.commit()
except Exception as e:
    tk.messagebox.showerror("Помилка", "Помилка: " + format(e))

def tablePaymentsUpdate():    
    if arr_payments:        
        # treeview.insert('', 'end', values=arr_payments[len(arr_payments)-1])
        for i in treeview.get_children():
            treeview.delete(i)
        for payment in arr_payments:
            treeview.insert('', 'end', values=payment)
    else: 
        for i in treeview.get_children():
            treeview.delete(i)
    
    if arr_paid_card:        
        # treeview.insert('', 'end', values=arr_payments[len(arr_payments)-1])
        for i in treeview_card.get_children():
            treeview_card.delete(i)
        for payment in arr_paid_card:
            treeview_card.insert('', 'end', values=payment)
    else: 
        for i in treeview_card.get_children():
            treeview_card.delete(i)    

def add_report(ent_data_name, ent_data_date, ent_data_code, ent_data_start_bt, ent_data_finish_bt, ent_data_days_bt, ent_data_sum_day, ent_data_sum_trip, ent_data_name_lat, ent_data_number, arr_payments, arr_paid_card, ent_data_customer, ent_data_city):
    arr_report_data.clear()
    arr_report_data.append(ent_data_name)
    arr_report_data.append(ent_data_date)
    arr_report_data.append(ent_data_code)
    arr_report_data.append(ent_data_start_bt)
    arr_report_data.append(ent_data_finish_bt)
    arr_report_data.append(ent_data_days_bt)
    arr_report_data.append(ent_data_sum_day)
    arr_report_data.append(ent_data_sum_trip)
    arr_report_data.append(ent_data_name_lat)
    arr_report_data.append(ent_data_number)
    arr_report_data.append(arr_payments)
    arr_report_data.append(arr_paid_card)
    arr_report_data.append(ent_data_customer)
    arr_report_data.append(ent_data_city)

    dict_report_data = {'name' : ent_data_name, 'date' : ent_data_date, 'code' : ent_data_code, 'start_bt' : ent_data_start_bt, 'finish_bt' : ent_data_finish_bt, 'days_bt' : ent_data_days_bt, 'sum_day' : ent_data_sum_day, 'sum_trip' : ent_data_sum_trip, 'name_lat' : ent_data_name_lat, 'number' : ent_data_number, 'payments' : arr_payments, 'paid_card' : arr_paid_card, 'customer' : ent_data_customer, 'city' : ent_data_city}

    print(dict_report_data['payments'])

    arr_payment_sum = 0
    arr_payment_sum = arr_payment_sum + float(dict_report_data['sum_trip'])
    arr_payment_sum_card = 0
    print(arr_payments)
    for i in arr_payments:
        arr_payment_sum = arr_payment_sum + float(i[3])
    for i in arr_payments:
        if i[4]:
            arr_payment_sum_card = arr_payment_sum_card + float(i[3])
    arr_report_data.append(arr_payment_sum)
    arr_report_data.append(arr_payment_sum_card)
    arr_payments_balance = arr_payment_sum - arr_payment_sum_card
    arr_report_data.append(arr_payments_balance)
    # arr_report_data.append(ent_data_customer)
    # arr_report_data.append(ent_data_city)
    root_mbx=tk.Toplevel()
    mbx = tk.Message(root_mbx, text=# "Ім'я: \t\t\t\t" + arr_report_data[0] +
                                            # "\nДата: \t\t\t\t" + arr_report_data[1] + 
                                            # "\nКод: \t\t\t\t" + arr_report_data[2] +
                                            # "\nДата початку відрядження: \t" + arr_report_data[3] +
                                            # "\nДата закінчення відрядження: \t" + arr_report_data[4] +
                                            # "\nКількість днів у відрядженні: \t" + arr_report_data[5] +
                                            # "\nНорма добових: \t\t\t" + arr_report_data[6] +
                                            # "\nСума добових: \t\t\t" + arr_report_data[7],
                                            # "\nСума витрат: " + arr_report_data[1] +
                                            # "\nСплачено з корп. рах.: " + arr_report_data[1] +
                                            # "\nБаланс: " + arr_report_data[1]
                                            "Імʼя: \t\t\t\t" + dict_report_data.get('name') + 
                                            "\nДата: \t\t\t\t" + dict_report_data.get('date') + 
                                            "\nКод: \t\t\t\t" + dict_report_data.get('code') +
                                            "\nМісто: \t\t\t\t" + dict_report_data.get('city') +
                                            "\nЗамовник: \t\t\t" + dict_report_data.get('customer') +
                                            "\nДата початку відрядження: \t" + dict_report_data.get('start_bt') +
                                            "\nДата закінчення відрядження: \t" + dict_report_data.get('finish_bt') +
                                            "\nКількість днів у відрядженні: \t" + dict_report_data.get('days_bt') +
                                            "\nНорма добових: \t\t\t" + dict_report_data.get('sum_day') +
                                            "\nСума добових: \t\t\t" + dict_report_data.get('sum_trip') +
                                            "\nСума витрат: \t\t\t" + str(arr_payment_sum) +
                                            "\nСплачено готівкою: \t\t" + str(round(float(arr_payment_sum - arr_payment_sum_card - float(dict_report_data.get('sum_trip'))), 2)) +
                                            "\nСплачено з корп. рах.: \t\t" + str(arr_payment_sum_card) +
                                            "\nБаланс: \t\t\t\t" + str(round(arr_payments_balance, 2)),
                                            width=750
                                            )
    mbx.pack(side=tk.TOP, anchor="nw")

    treeview1 = ttk.Treeview(root_mbx)
    treeview1.pack(side=tk.TOP,fill=tk.BOTH, expand=1)

    treeview1["columns"]=("one","two","three", "four", "five")
    treeview1.column("#0", width=50, minwidth=50, stretch=tk.NO)
    treeview1.column("one", width=100, minwidth=100, stretch=tk.NO)
    treeview1.column("two", width=100, minwidth=100, stretch=tk.NO)
    treeview1.column("three", width=400, minwidth=200)
    treeview1.column("four", width=100, minwidth=50, stretch=tk.NO)
    treeview1.column("five", width=160, minwidth=50, stretch=tk.NO)

    treeview1.heading("#0",text="ID",anchor=tk.W)
    treeview1.heading("one", text="Код",anchor=tk.W)
    treeview1.heading("two", text="Дата",anchor=tk.W)
    treeview1.heading("three", text="Найменування",anchor=tk.W)
    treeview1.heading("four", text="Сума",anchor=tk.W)
    treeview1.heading("five", text="Сплачено з корп. р.",anchor=tk.W)

    if arr_payments:
        # treeview.insert('', 'end', values=arr_payments[len(arr_payments)-1])
        for i in treeview1.get_children():
            treeview1.delete(i)
        for payment in arr_payments:
            treeview1.insert('', 'end', values=payment)
    else: 
        for i in treeview1.get_children():
            treeview1.delete(i)

    frm_buttons = tk.Frame(root_mbx)
    frm_buttons.pack(side=tk.TOP, anchor="nw")

    # btn_save_report = tk.Button(frm_buttons, text='Зберегти', command=lambda: save_report())
    btn_save_report = tk.Button(frm_buttons, text='Зберегти', command=lambda: (def_report_date_to_db.data_to_db(arr_report_data, root_mbx), save_report()))
    # btn_save_report.bind('<Button-1>', lambda event: createExcel.fill_xls(arr_report_data))
    # btn_save_report.bind('<Button-1>', lambda event: ((formatting_Excel.test_func(arr_report_data, 'template.xlsx', word_docs.filename_create('AR', arr_report_data[2]))), (word_docs.order_from_list(arr_report_data, 'template.docx', word_docs.filename_create('OR', arr_report_data[2])))))
    # btn_save_report.bind('<Button-1>', lambda event: word_docs.order_from_list(arr_report_data, 'template.docx', word_docs.filename_create('OR', arr_report_data[2])))
    btn_save_report.pack(side=tk.LEFT)

    btn_save_print_report = tk.Button(frm_buttons, text='Зберегти і надрукувати', command=lambda: print('btn_save_report'))
    btn_save_print_report.pack(side=tk.LEFT)

    btn_print_report = tk.Button(frm_buttons, text='Надрукувати', command=lambda: print('btn_save_report'))
    btn_print_report.pack(side=tk.LEFT)

    btn_cancel_without = tk.Button(frm_buttons, text='Відміна', command=lambda: root_mbx.destroy())
    btn_cancel_without.pack(side=tk.LEFT)

def add_report_print():
    print('add_report_print')

def report_cancel():
    root.destroy()
    root.quit()

def ins_row_arr():
    def ins_pay_arr(ent_code, ent_date, ent_desc, ent_sum, paidByCard):
        arr_pay = [ent_code, ent_date, ent_desc, ent_sum, paidByCard]
        arr_payments.append(arr_pay)
        if paidByCard == True:
            arr_paid_card.append(arr_pay)
        tablePaymentsUpdate()
        ins_root.destroy()
    ins_root = tk.Toplevel()
    ins_root.minsize(width=1550,height=60)

    frm_ent_date = tk.Frame(ins_root)
    frm_ent_date.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
    lbl1 = tk.Label(frm_ent_date, text='Дата платежу:')
    lbl1.pack(side=tk.LEFT, anchor="nw")
    ent_date = tk.Entry(frm_ent_date, width=10)
    ent_date.bind('<Button-1>', lambda event: entry_date(ent_date))
    ent_date.pack(side=tk.LEFT, anchor="nw")

    frm_ent_desc = tk.Frame(ins_root)
    frm_ent_desc.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
    lbl2 = tk.Label(frm_ent_desc, text='Найменування платежу:')
    lbl2.pack(side=tk.LEFT, anchor="nw")
    ent_desc = autocomplete.AutocompleteEntry(arr_payments_autocomlete, frm_ent_desc, width=50)
    ent_desc.pack(side=tk.LEFT, anchor="nw")

    frm_ent_sum = tk.Frame(ins_root)
    frm_ent_sum.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
    lbl3 = tk.Label(frm_ent_sum, text='Сума:')
    lbl3.pack(side=tk.LEFT, anchor="nw")
    ent_sum = tk.Entry(frm_ent_sum, width=10)
    ent_sum.pack(side=tk.LEFT, anchor="nw")

    frm_check_card = tk.Frame(ins_root)
    frm_check_card.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
    lbl4 = tk.Label(frm_check_card, text='Сплачено з корпоративного рахунку:')
    lbl4.pack(side=tk.LEFT, anchor="nw")
    paidByCard = tk.BooleanVar()
    paidByCard.set(0)
    check_card = tk.Checkbutton(frm_check_card, variable=paidByCard, onvalue=1, offvalue=0)
    check_card.pack(side=tk.LEFT, anchor="nw")

    main_frame_toplevel_btn = tk.Frame(ins_root)
    main_frame_toplevel_btn.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
    ins_btn = tk.Button(main_frame_toplevel_btn, text='Додати платіж', command=lambda:ins_pay_arr(ent_data_code.get(), ent_date.get(), ent_desc.get(), ent_sum.get(), paidByCard.get()))
    ins_btn.pack(side=tk.LEFT, anchor="nw", padx=5)
    ins_btn_cancel = tk.Button(main_frame_toplevel_btn, text='Відміна', command=lambda:ins_root.destroy())
    ins_btn_cancel.pack(side=tk.LEFT, anchor="nw")

def del_row_arr():    
    if arr_payments:        
        item = treeview.selection()[0]
        del arr_payments[treeview.index(item)]        
        arr_paid_card.clear()
        for payment in arr_payments:
            if payment[3] == True:
                arr_paid_card.append(payment)
        tablePaymentsUpdate()
    else: 
        tk.messagebox.showinfo('Увага!', 'Відсутні записи для видалення')

def edt_row_arr():
        
    if treeview.selection():
        item = treeview.selection()[0]
        def ins_pay_arr(ent_date, ent_desc, ent_sum, paidByCard):
            arr_pay = [ent_date, ent_desc, ent_sum, paidByCard]
            arr_payments[treeview.index(item)] = arr_pay
            arr_paid_card.clear()
            for payment in arr_payments:
                if payment[3] == True:
                    arr_paid_card.append(payment)
            tablePaymentsUpdate()
            ins_root.destroy()
        # ins_root = tk.Toplevel()
        # ent_date = tk.Entry(ins_root)
        # ent_date.insert(0, arr_payments[treeview.index(item)][0])
        # ent_date.bind('<Button-1>', lambda event: entry_date(ent_date))
        # ent_date.grid(row=0, column=0)
        # ent_desc = tk.Entry(ins_root)
        # ent_desc.insert(0, arr_payments[treeview.index(item)][1])
        # ent_desc.grid(row=0, column=1)
        # ent_sum = tk.Entry(ins_root)
        # ent_sum.insert(0, arr_payments[treeview.index(item)][2])
        # ent_sum.grid(row=0, column=2)
        # paidByCard = BooleanVar()
        # paidByCard.set(arr_payments[treeview.index(item)][3])
        # check_card = tk.Checkbutton(ins_root, variable=paidByCard, onvalue=1, offvalue=0)
        # check_card.grid(row=0, column=3)
        # ins_btn = tk.Button(ins_root, text='Змінити', command=lambda:ins_pay_arr(ent_date.get(), ent_desc.get(), ent_sum.get(), paidByCard.get()))
        # ins_btn.grid(row=0, column=4)

        ins_root = tk.Toplevel()
        ins_root.minsize(width=1550,height=60)

        frm_ent_date = tk.Frame(ins_root)
        frm_ent_date.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
        lbl1 = tk.Label(frm_ent_date, text='Дата платежу:')
        lbl1.pack(side=tk.LEFT, anchor="nw")
        ent_date = tk.Entry(frm_ent_date, width=10)
        ent_date.insert(0, arr_payments[treeview.index(item)][0])
        ent_date.bind('<Button-1>', lambda event: entry_date(ent_date))
        ent_date.pack(side=tk.LEFT, anchor="nw")

        frm_ent_desc = tk.Frame(ins_root)
        frm_ent_desc.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
        lbl2 = tk.Label(frm_ent_desc, text='Найменування платежу:')
        lbl2.pack(side=tk.LEFT, anchor="nw")
        ent_desc = autocomplete.AutocompleteEntry(arr_payments_autocomlete, frm_ent_desc, width=50)
        ent_desc.delete(0,tk.END)
        ent_desc.pack()
        ent_desc.bind('<Button-1>', lambda event: (ent_desc.delete(0,tk.END), ent_desc.insert(0, arr_payments[treeview.index(item)][1])))

        frm_ent_sum = tk.Frame(ins_root)
        frm_ent_sum.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
        lbl3 = tk.Label(frm_ent_sum, text='Сума:')
        lbl3.pack(side=tk.LEFT, anchor="nw")
        ent_sum = tk.Entry(frm_ent_sum, width=10)
        ent_sum.insert(0, arr_payments[treeview.index(item)][2])
        ent_sum.pack(side=tk.LEFT, anchor="nw")

        frm_check_card = tk.Frame(ins_root)
        frm_check_card.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
        lbl4 = tk.Label(frm_check_card, text='Сплачено з корпоративного рахунку:')
        lbl4.pack(side=tk.LEFT, anchor="nw")
        paidByCard = tk.BooleanVar()
        paidByCard.set(0)
        paidByCard.set(arr_payments[treeview.index(item)][3])
        check_card = tk.Checkbutton(frm_check_card, variable=paidByCard, onvalue=1, offvalue=0)
        check_card.pack(side=tk.LEFT, anchor="nw")

        main_frame_toplevel_btn = tk.Frame(ins_root)
        main_frame_toplevel_btn.pack(side=tk.LEFT, anchor="nw", fill=tk.Y, padx=15)
        ins_btn = tk.Button(main_frame_toplevel_btn, text='Змінити', command=lambda:ins_pay_arr(ent_date.get(), ent_desc.get(), ent_sum.get(), paidByCard.get()))
        ins_btn.pack(side=tk.LEFT, anchor="nw", padx=5)
        ins_btn_cancel = tk.Button(main_frame_toplevel_btn, text='Відміна', command=lambda:ins_root.destroy())
        ins_btn_cancel.pack(side=tk.LEFT, anchor="nw")


    else: tk.messagebox.showinfo('Увага!', 'Виберіть елемент для редагування!')

def result_arr_def():
    name = ent_data_name.get()
    latin_name = ent_data_name_lat.get()
    code = ent_data_code.get()
    identific_number = ent_data_number.get()

    if not name and not latin_name and not code and not identific_number:
        result_arr.clear()
        # for element in autocompl_test_arr:
        for element in autocomplete_name:
            result_arr.append(element)
    else:
        # Працює начебто добре :)
        result_arr.clear()
        temp_arr = []
        temp_arr.append(name)
        temp_arr.append(latin_name)
        temp_arr.append(code)
        temp_arr.append(identific_number)

        for elem in autocomplete_name:
            i = 0
            for elem1 in temp_arr:
                if elem1:
                    if elem1 == elem[i]:
                        if elem not in result_arr:
                            result_arr.append(elem)
                i = i + 1
        if len(result_arr) == 1:
            ent_data_name.delete(0,tk.END) 
            ent_data_name.insert(0, result_arr[0][0])
            ent_data_name.selection('<FocusOut>')

            ent_data_name_lat.delete(0,tk.END) 
            ent_data_name_lat.insert(0, result_arr[0][1])
            ent_data_name_lat.selection('<FocusOut>')   

            ent_data_code.delete(0,tk.END) 
            ent_data_code.insert(0, result_arr[0][2])
            ent_data_code.selection('<FocusOut>')   

            ent_data_number.delete(0,tk.END) 
            ent_data_number.insert(0, result_arr[0][3]) 
            ent_data_number.selection('<FocusOut>')   

def choose_arr_in(ind):
    result_arr_def()
    autocompl_fill.clear()
    for elem in result_arr:
        autocompl_fill.append(elem[ind])
    print(autocompl_fill)

def choose_arr_out():
    result_arr_def()

def entry_date(dt_data):
    dt = My_Calendar.date_selection()
    dt_data.delete(0, 'end')
    dt_data.insert(0, dt)

    if ent_data_start_bt.get() and ent_data_finish_bt.get():
        date_start = datetime.strptime(ent_data_start_bt.get(), '%d.%m.%y')
        date_finish = datetime.strptime(ent_data_finish_bt.get(), '%d.%m.%y')
        days_in_bt = ((date_finish-date_start).days + 1)
        ent_data_days_bt.delete(0,tk.END)
        ent_data_days_bt.insert(0, days_in_bt)
    
    if ent_data_days_bt.get():
        sum_pay_days = float(ent_data_days_bt.get()) * float(ent_data_sum_day.get())
        ent_data_sum_trip.delete(0,tk.END)
        ent_data_sum_trip.insert(0, sum_pay_days)
    
    if ent_data_code.get() and ent_data_date.get():
        code_date_yy = ent_data_date.get()[-2:]
        code_date_mm = ent_data_date.get()[:5]
        code_date_dd = code_date_mm[:2]
        code_date_mm = code_date_mm[-2:]
        code_date = code_date_yy + code_date_mm + code_date_dd
        ent_data_code.delete(0,tk.END)
        ent_data_code.insert(0, result_arr[0][2] + code_date)

def save_report():
    # def_report_date_to_db.data_to_db(arr_report_data, root_mbx)
    formatting_Excel.test_func(arr_report_data, 'template.xlsx', word_docs.filename_create('AR', arr_report_data[2]))
    word_docs.order_from_list(arr_report_data, 'template.docx', word_docs.filename_create('OR', arr_report_data[2]))

root = tk.Tk()
root.title("Звіт")

autocompl_test_arr = [["Qwerty", 123, "asdfg"], ["Poiuy", 45678, "bnm,"], ["Asdfg", 67890, "zxcv"], ["Rghm", 9876, "uioplk"], ["Qwerty", 567, "jhgfsgh"], ["Pqwoiuy", 45435678, "esfrwbnm,"]]
autocompl_fill = []
result_arr = []


main_menu = tk.Menu(root)
root.configure(menu=main_menu)
first_item = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=first_item)
first_item.add_command(label="New")
first_item.add_command(label="Exit", command=root.destroy)
second_item = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Data Base", menu=second_item)
second_item.add_command(label="Додавання співробітника в БД", command=bd_report_insert.add_bd_emloyee)
second_item.add_command(label="Додавання Замовника в БД", command=bd_report_insert.add_bd_customers)
second_item.add_command(label="Додавання обладнання в БД", command=bd_report_insert.add_bd_equipment)
second_item.add_command(label="Зміна норми добових в БД", command=bd_report_insert.add_bd_norm)

toolbar = tk.Frame(root, bg="#A1A1A1")
toolbar.pack(side=tk.TOP,fill=tk.X)

tool_btn1 = tk.Button(toolbar, text="Cut")
tool_btn1.grid(row=0, column=0, padx=2, pady=2)

tool_btn2 = tk.Button(toolbar, text="Copy")
tool_btn2.grid(row=0, column=1, padx=2, pady=2)

image = tk.PhotoImage(file="Print.gif")
tool_btn3 = tk.Button(toolbar, image=image)
tool_btn3.grid(row=0, column=2, padx=2, pady=2)


frm_data = tk.LabelFrame(root, text="Дані звіту:", font="Ubuntu, 13")
frm_data.pack(side=tk.TOP, fill=tk.X)

frm_col1 = tk.Frame(frm_data)
frm_col1.pack(side=tk.LEFT, fill=tk.BOTH)

lbl_data1 = tk.Label(frm_col1, text='ПІБ:', font="Ubuntu, 12")
lbl_data1.pack(anchor="e", pady=1)

lbl_data2 = tk.Label(frm_col1, text='Дата звіту:', font="Ubuntu, 12")
lbl_data2.pack(anchor="e", pady=1)

lbl_data3 = tk.Label(frm_col1, text='Код звіту:', font="Ubuntu, 12")
lbl_data3.pack(anchor="e", pady=1)

lbl_data4 = tk.Label(frm_col1, text='Дата початку відрядження:', font="Ubuntu, 12")
lbl_data4.pack(anchor="e", pady=1)

lbl_data5 = tk.Label(frm_col1, text='Дата закінчення відрядження:', font="Ubuntu, 12")
lbl_data5.pack(anchor="e", pady=1)

lbl_data6 = tk.Label(frm_col1, text='Кількість днів у відрядженні:', font="Ubuntu, 12")
lbl_data6.pack(anchor="e", pady=1)

lbl_data7 = tk.Label(frm_col1, text='Норма добових:', font="Ubuntu, 12")
lbl_data7.pack(anchor="e", pady=1)

lbl_data8 = tk.Label(frm_col1, text='Сума добових:', font="Ubuntu, 12")
lbl_data8.pack(anchor="e", pady=1)

frm_col2 = tk.Frame(frm_data)
frm_col2.pack(side=tk.LEFT, fill=tk.BOTH)

ent_data_name = autocomplete.AutocompleteEntry(autocompl_fill, frm_col2, width=35)
ent_data_name.pack(pady=1)
ent_data_name.bind('<FocusIn>', lambda event: choose_arr_in(0))
ent_data_name.bind('<FocusOut>', lambda event: choose_arr_out())

ent_data_date = tk.Entry(frm_col2, width=35)
ent_data_date.bind('<Button-1>', lambda event: entry_date(ent_data_date))
ent_data_date.pack(pady=1)

ent_data_code = autocomplete.AutocompleteEntry(autocompl_fill, frm_col2, width=35)
ent_data_code.pack(pady=1)
ent_data_code.bind('<FocusIn>', lambda event: choose_arr_in(2))
ent_data_code.bind('<FocusOut>', lambda event: choose_arr_out())

ent_data_start_bt = tk.Entry(frm_col2, width=35)
ent_data_start_bt.bind('<Button-1>', lambda event: entry_date(ent_data_start_bt))
ent_data_start_bt.pack(pady=1)

ent_data_finish_bt = tk.Entry(frm_col2, width=35)
ent_data_finish_bt.bind('<Button-1>', lambda event: entry_date(ent_data_finish_bt))
ent_data_finish_bt.pack(pady=1)

ent_data_days_bt = tk.Entry(frm_col2, width=35)
ent_data_days_bt.pack(pady=1)

ent_data_sum_day = tk.Entry(frm_col2, width=35)
ent_data_sum_day.insert(0, norma_day)
ent_data_sum_day.pack(pady=1)

ent_data_sum_trip = autocomplete.AutocompleteEntry(autocompl_test_arr, frm_col2, width=35)
ent_data_sum_trip.pack(pady=1)

frm_col3 = tk.Frame(frm_data)
frm_col3.pack(side=tk.LEFT, fill=tk.BOTH)

lbl_data9 = tk.Label(frm_col3, text='ПІБ (Лат.):', font="Ubuntu, 12")
lbl_data9.pack(anchor="e", pady=1)

lbl_data10 = tk.Label(frm_col3, text='Ідентифікаційний номер:', font="Ubuntu, 12")
lbl_data10.pack(anchor="e", pady=1)

lbl_data11 = tk.Label(frm_col3, text='Замовник:', font="Ubuntu, 12")
lbl_data11.pack(anchor="e", pady=1)

lbl_data12 = tk.Label(frm_col3, text='Місто:', font="Ubuntu, 12")
lbl_data12.pack(anchor="e", pady=1)

frm_col4 = tk.Frame(frm_data)
frm_col4.pack(side=tk.LEFT, fill=tk.BOTH)

ent_data_name_lat = autocomplete.AutocompleteEntry(autocompl_fill, frm_col4, width=35)
ent_data_name_lat.pack(pady=1)
ent_data_name_lat.bind('<FocusIn>', lambda event: choose_arr_in(1))
ent_data_name_lat.bind('<FocusOut>', lambda event: choose_arr_out())

ent_data_number = autocomplete.AutocompleteEntry(autocompl_fill, frm_col4, width=35)
ent_data_number.pack(pady=1)
ent_data_number.bind('<FocusIn>', lambda event: choose_arr_in(3))
ent_data_number.bind('<FocusOut>', lambda event: choose_arr_out())

ent_data_customer = autocomplete.AutocompleteEntry(autocompl_fill, frm_col4, width=35)
ent_data_customer.pack(pady=1)
ent_data_customer.bind('<FocusIn>', lambda event: choose_arr_in(3))
ent_data_customer.bind('<FocusOut>', lambda event: choose_arr_out())

ent_data_city = autocomplete.AutocompleteEntry(autocompl_fill, frm_col4, width=35)
ent_data_city.pack(pady=1)
ent_data_city.bind('<FocusIn>', lambda event: choose_arr_in(3))
ent_data_city.bind('<FocusOut>', lambda event: choose_arr_out())

frm_payments = tk.LabelFrame(root, text="Витрати", font="Ubuntu, 12")
frm_payments.pack(side=tk.TOP, pady=10, fill=tk.BOTH, expand=1)

treeview = ttk.Treeview(frm_payments)
treeview.pack(side=tk.TOP,fill=tk.BOTH, expand=1)

treeview["columns"]=("one","two","three", "four", "five")
treeview.column("#0", width=50, minwidth=270, stretch=tk.NO)
treeview.column("one", width=100, minwidth=100, stretch=tk.NO)
treeview.column("two", width=100, minwidth=150, stretch=tk.NO)
treeview.column("three", width=400, minwidth=200)
treeview.column("four", width=100, minwidth=50, stretch=tk.NO)
treeview.column("five", width=160, minwidth=50, stretch=tk.NO)

treeview.heading("#0",text="ID",anchor=tk.W)
treeview.heading("one", text="Код",anchor=tk.W)
treeview.heading("two", text="Дата",anchor=tk.W)
treeview.heading("three", text="Найменування",anchor=tk.W)
treeview.heading("four", text="Сума",anchor=tk.W)
treeview.heading("five", text="Сплачено з корп. р.",anchor=tk.W)

frm_paid_card = tk.LabelFrame(root, text="Сплачено з кредитного рахунку", font="Ubuntu, 12")
frm_paid_card.pack(side=tk.TOP, pady=10, fill=tk.BOTH, expand=1)

treeview_card = ttk.Treeview(frm_paid_card)
treeview_card.pack(side=tk.TOP,fill=tk.BOTH, expand=1)

treeview_card["columns"]=("one","two","three", "four", "five")
treeview_card.column("#0", width=50, minwidth=270, stretch=tk.NO)
treeview_card.column("one", width=100, minwidth=100, stretch=tk.NO)
treeview_card.column("two", width=100, minwidth=150, stretch=tk.NO)
treeview_card.column("three", width=400, minwidth=200)
treeview_card.column("four", width=100, minwidth=50, stretch=tk.NO)
treeview_card.column("five", width=160, minwidth=50, stretch=tk.NO)

treeview_card.heading("#0",text="ID",anchor=tk.W)
treeview_card.heading("one", text="Код",anchor=tk.W)
treeview_card.heading("two", text="Дата",anchor=tk.W)
treeview_card.heading("three", text="Найменування",anchor=tk.W)
treeview_card.heading("four", text="Сума",anchor=tk.W)
treeview_card.heading("five", text="Сплачено з корп. р.",anchor=tk.W)

tablePaymentsUpdate()

frm_btn_payment = tk.Frame(root)
frm_btn_payment.pack(pady=10, padx=5, anchor="nw")

btn_add_payment = tk.Button(frm_btn_payment, text='Додати платіж', command=ins_row_arr)
btn_add_payment.pack(side=tk.LEFT, padx=1)
btn_del_payment = tk.Button(frm_btn_payment, text='Видалити платіж', command=del_row_arr)
btn_del_payment.pack(side=tk.LEFT, padx=1)
btn_edt_payment = tk.Button(frm_btn_payment, text='Редагувати платіж', command=edt_row_arr)
btn_edt_payment.pack(side=tk.LEFT, padx=1)

frm_btn_report = tk.Frame(root)
frm_btn_report.pack(pady=10, padx=5, anchor="ne")

btn_add_report = tk.Button(frm_btn_report, text='Зберегти звіт', command=lambda:add_report(ent_data_name.get(), ent_data_date.get(), ent_data_code.get(), ent_data_start_bt.get(), ent_data_finish_bt.get(), ent_data_days_bt.get(), ent_data_sum_day.get(), ent_data_sum_trip.get(), ent_data_name_lat.get(), ent_data_number.get(), arr_payments, arr_paid_card, ent_data_customer.get(), ent_data_city.get()))
btn_add_report.pack(side=tk.LEFT, padx=1)

btn_add_report_print = tk.Button(frm_btn_report, text='Зберегти і надрукувати звіт', command=add_report_print)
btn_add_report_print.pack(side=tk.LEFT, padx=1)

btn_report_cancel = tk.Button(frm_btn_report, text='Відмінити', command=report_cancel)
btn_report_cancel.pack(side=tk.LEFT, padx=1)

status_bar = tk.Label(root, relief=tk.SUNKEN, anchor=tk.W, text="Mission Complete!")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
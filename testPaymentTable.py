import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Звіт")

arr_report_data = []
arr_payments = []
arr_pay = []
arr_paid_card = []

def add_report(ent_data_name, ent_data_date, ent_data_code, ent_data_start_bt, ent_data_finish_bt, ent_data_days_bt, ent_data_sum_day, ent_data_sum_trip, ent_data_name_lat, ent_data_number, arr_payments, arr_paid_card):
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
    print(arr_report_data)
    # mbx = tk.messagebox.askokcancel("Звіт", "Ім'я: " + arr_report_data[0] +
    #                                         "\nДата: " + arr_report_data[1] + 
    #                                         "\nКод: " + arr_report_data[2] +
    #                                         "\nДата початку відрядження: " + arr_report_data[3] +
    #                                         "\nДата закінчення відрядження: " + arr_report_data[4] +
    #                                         "\nКількість днів у відрядженні: " + arr_report_data[5] +
    #                                         "\nНорма добових: " + arr_report_data[6] +
    #                                         "\nСума добових: " + arr_report_data[7]
    #                                         # "\nСума витрат: " + arr_report_data[1] +
    #                                         # "\nСплачено з корп. рах.: " + arr_report_data[1] +
    #                                         # "\nБаланс: " + arr_report_data[1]
    #                                         )
    root_mbx=tk.Toplevel()
    mbx = tk.Message(root_mbx, text="Ім'я: \t\t\t\t" + arr_report_data[0] +
                                            "\nДата: \t\t\t\t" + arr_report_data[1] + 
                                            "\nКод: \t\t\t\t" + arr_report_data[2] +
                                            "\nДата початку відрядження: \t" + arr_report_data[3] +
                                            "\nДата закінчення відрядження: \t" + arr_report_data[4] +
                                            "\nКількість днів у відрядженні: \t" + arr_report_data[5] +
                                            "\nНорма добових: \t\t\t" + arr_report_data[6] +
                                            "\nСума добових: \t\t\t" + arr_report_data[7],
                                            # "\nСума витрат: " + arr_report_data[1] +
                                            # "\nСплачено з корп. рах.: " + arr_report_data[1] +
                                            # "\nБаланс: " + arr_report_data[1]
                                            width=750
                                            )
    mbx.pack()

def add_report_print():
    print('add_report_print')

def report_cancel():
    root.destroy()
    root.quit()

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

def ins_row_arr():
    def ins_pay_arr(ent_date, ent_desc, ent_sum, paidByCard):
        arr_pay = [ent_date, ent_desc, ent_sum, paidByCard]
        arr_payments.append(arr_pay)
        if paidByCard == True:
            arr_paid_card.append(arr_pay)
        tablePaymentsUpdate()
        ins_root.destroy()
    ins_root = tk.Toplevel()
    frm_ent_date = tk.LabelFrame(ins_root, text="Дата платежу")
    frm_ent_date.grid(row=0, column=0)
    ent_date = tk.Entry(frm_ent_date)
    ent_date.grid(row=0, column=0)
    frm_ent_desc = tk.LabelFrame(ins_root, text="Назва товару чи послуги")
    frm_ent_desc.grid(row=0, column=1)
    ent_desc = tk.Entry(frm_ent_desc, width=50)
    ent_desc.grid(row=0, column=0)
    frm_ent_sum = tk.LabelFrame(ins_root, text="Сума")
    frm_ent_sum.grid(row=0, column=2)
    ent_sum = tk.Entry(frm_ent_sum, width=10)
    ent_sum.grid(row=0, column=0)
    frm_check_card = tk.LabelFrame(ins_root, text="Сплачено з корпоративного рахунку")
    frm_check_card.grid(row=0, column=3)
    paidByCard = BooleanVar()
    paidByCard.set(0)
    check_card = tk.Checkbutton(frm_check_card, variable=paidByCard, onvalue=1, offvalue=0)
    check_card.grid(row=0, column=3, padx=110)
    ins_btn = tk.Button(ins_root, text='Додати платіж', command=lambda:ins_pay_arr(ent_date.get(), ent_desc.get(), ent_sum.get(), paidByCard.get()))
    ins_btn.grid(row=1, column=0, columnspan=4, sticky='ew')

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
        ins_root = tk.Toplevel()
        ent_date = tk.Entry(ins_root)
        ent_date.insert(0, arr_payments[treeview.index(item)][0])
        ent_date.grid(row=0, column=0)
        ent_desc = tk.Entry(ins_root)
        ent_desc.insert(0, arr_payments[treeview.index(item)][1])
        ent_desc.grid(row=0, column=1)
        ent_sum = tk.Entry(ins_root)
        ent_sum.insert(0, arr_payments[treeview.index(item)][2])
        ent_sum.grid(row=0, column=2)
        paidByCard = BooleanVar()
        paidByCard.set(arr_payments[treeview.index(item)][3])
        check_card = tk.Checkbutton(ins_root, variable=paidByCard, onvalue=1, offvalue=0)
        check_card.grid(row=0, column=3)
        ins_btn = tk.Button(ins_root, text='Змінити', command=lambda:ins_pay_arr(ent_date.get(), ent_desc.get(), ent_sum.get(), paidByCard.get()))
        ins_btn.grid(row=0, column=4)
    else: tk.messagebox.showinfo('Увага!', 'Виберіть елемент для редагування!')

frm_data = tk.LabelFrame(root, text="Дані звіту:", font="Ubuntu, 12")
frm_data.pack(side=tk.TOP, fill=tk.X)

lbl_data1 = tk.Label(frm_data, text='ПІБ:', font="Ubuntu, 10")
lbl_data1.grid(row=0, column=0, sticky=E)

lbl_data2 = tk.Label(frm_data, text='Дата звіту:', font="Ubuntu, 10")
lbl_data2.grid(row=1, column=0, sticky=E)

lbl_data3 = tk.Label(frm_data, text='Код звіту:', font="Ubuntu, 10")
lbl_data3.grid(row=2, column=0, sticky=E)

lbl_data4 = tk.Label(frm_data, text='Дата початку відрядження:', font="Ubuntu, 10")
lbl_data4.grid(row=3, column=0, sticky=E)

lbl_data5 = tk.Label(frm_data, text='Дата закінчення відрядження:', font="Ubuntu, 10")
lbl_data5.grid(row=4, column=0, sticky=E)

lbl_data6 = tk.Label(frm_data, text='Кількість днів у відрядженні:', font="Ubuntu, 10")
lbl_data6.grid(row=5, column=0, sticky=E)

lbl_data7 = tk.Label(frm_data, text='Норма добових:', font="Ubuntu, 10")
lbl_data7.grid(row=6, column=0, sticky=E)

lbl_data8 = tk.Label(frm_data, text='Сума добових:', font="Ubuntu, 10")
lbl_data8.grid(row=7, column=0, sticky=E)

lbl_data9 = tk.Label(frm_data, text='ПІБ (Лат.):', font="Ubuntu, 10")
lbl_data9.grid(row=0, column=3, sticky=E)

lbl_data10 = tk.Label(frm_data, text='Ідентифікаційний номер:', font="Ubuntu, 10")
lbl_data10.grid(row=1, column=3, sticky=E)

ent_data_name = tk.Entry(frm_data, width=35)
ent_data_name.grid(row=0, column=1, sticky=W, padx=5)

ent_data_date = tk.Entry(frm_data, width=35)
ent_data_date.grid(row=1, column=1, sticky=W, padx=5)

ent_data_code = tk.Entry(frm_data, width=35)
ent_data_code.grid(row=2, column=1, sticky=W, padx=5)

ent_data_start_bt = tk.Entry(frm_data, width=35)
ent_data_start_bt.grid(row=3, column=1, sticky=W, padx=5)

ent_data_finish_bt = tk.Entry(frm_data, width=35)
ent_data_finish_bt.grid(row=4, column=1, sticky=W, padx=5)

ent_data_days_bt = tk.Entry(frm_data, width=35)
ent_data_days_bt.grid(row=5, column=1, sticky=W, padx=5)

ent_data_sum_day = tk.Entry(frm_data, width=35)
ent_data_sum_day.grid(row=6, column=1, sticky=W, padx=5)

ent_data_sum_trip = tk.Entry(frm_data, width=35)
ent_data_sum_trip.grid(row=7, column=1, sticky=W, padx=5)

ent_data_name_lat = tk.Entry(frm_data, width=35)
ent_data_name_lat.grid(row=0, column=4, sticky=W, padx=5)

ent_data_number = tk.Entry(frm_data, width=35)
ent_data_number.grid(row=1, column=4, sticky=W, padx=5)

frm_payments = tk.LabelFrame(root, text="Витрати", font="Ubuntu, 12")
frm_payments.pack(side=tk.TOP, pady=10, fill=tk.BOTH, expand=1)

treeview = ttk.Treeview(frm_payments)
treeview.pack(side=tk.TOP,fill=tk.BOTH, expand=1)

treeview["columns"]=("one","two","three", "four")
treeview.column("#0", width=50, minwidth=270, stretch=tk.NO)
treeview.column("one", width=100, minwidth=150, stretch=tk.NO)
treeview.column("two", width=400, minwidth=200)
treeview.column("three", width=100, minwidth=50, stretch=tk.NO)
treeview.column("four", width=160, minwidth=50, stretch=tk.NO)

treeview.heading("#0",text="ID",anchor=tk.W)
treeview.heading("one", text="Дата",anchor=tk.W)
treeview.heading("two", text="Найменування",anchor=tk.W)
treeview.heading("three", text="Сума",anchor=tk.W)
treeview.heading("four", text="Сплачено з корп. р.",anchor=tk.W)

frm_paid_card = tk.LabelFrame(root, text="Сплачено з кредитного рахунку", font="Ubuntu, 12")
frm_paid_card.pack(side=tk.TOP, pady=10, fill=tk.BOTH, expand=1)

treeview_card = ttk.Treeview(frm_paid_card)
treeview_card.pack(side=tk.TOP,fill=tk.BOTH, expand=1)

treeview_card["columns"]=("one","two","three", "four")
treeview_card.column("#0", width=50, minwidth=270, stretch=tk.NO)
treeview_card.column("one", width=100, minwidth=150, stretch=tk.NO)
treeview_card.column("two", width=400, minwidth=200)
treeview_card.column("three", width=100, minwidth=50, stretch=tk.NO)
treeview_card.column("four", width=160, minwidth=50, stretch=tk.NO)

treeview_card.heading("#0",text="ID",anchor=tk.W)
treeview_card.heading("one", text="Дата",anchor=tk.W)
treeview_card.heading("two", text="Найменування",anchor=tk.W)
treeview_card.heading("three", text="Сума",anchor=tk.W)
treeview_card.heading("four", text="Сплачено з корп. р.",anchor=tk.W)

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

btn_add_report = tk.Button(frm_btn_report, text='Зберегти звіт', command=lambda:add_report(ent_data_name.get(), ent_data_date.get(), ent_data_code.get(), ent_data_start_bt.get(), ent_data_finish_bt.get(), ent_data_days_bt.get(), ent_data_sum_day.get(), ent_data_sum_trip.get(), ent_data_name_lat.get(), ent_data_number.get(), arr_payments, arr_paid_card))
btn_add_report.pack(side=tk.LEFT, padx=1)

btn_add_report_print = tk.Button(frm_btn_report, text='Зберегти і надрукувати звіт', command=add_report_print)
btn_add_report_print.pack(side=tk.LEFT, padx=1)

btn_report_cancel = tk.Button(frm_btn_report, text='Відмінити', command=report_cancel)
btn_report_cancel.pack(side=tk.LEFT, padx=1)

root.mainloop()
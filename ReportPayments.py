import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

arr_payments = []
arr_pay = []
arr_paid_card = []

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

frm_btn = tk.Frame(root)
frm_btn.pack(side=tk.LEFT, pady=10, padx=5, anchor="ne")

btn_add = tk.Button(frm_btn, text='Додати', command=ins_row_arr)
btn_add.pack(side=tk.LEFT, padx=5)
btn_del = tk.Button(frm_btn, text='Видалити', command=del_row_arr)
btn_del.pack(side=tk.LEFT, padx=5)
btn_edt = tk.Button(frm_btn, text='Редагувати', command=edt_row_arr)
btn_edt.pack(side=tk.LEFT, padx=5)

root.mainloop()
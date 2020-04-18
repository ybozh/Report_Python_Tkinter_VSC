import sqlite3
import tkinter as tk
from tkinter import messagebox


db = sqlite3.connect('report.db')
connect = db.cursor()
def data_to_db(arr_rep_data, win):
    try:       
        # print(arr_rep_data) 
        connect.execute('''INSERT INTO report(code, 
                                            date, 
                                            emploee, 
                                            date_of_start, 
                                            date_of_finish, 
                                            days,
                                            norma_salary_day, 
                                            salary_trip, 
                                            sum, 
                                            sum_paid, 
                                            balance, 
                                            customer, 
                                            city) 
                                            VALUES 
                                            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (arr_rep_data[2], 
                            arr_rep_data[1], 
                            arr_rep_data[0],
                            arr_rep_data[3],
                            arr_rep_data[4],
                            arr_rep_data[5], 
                            arr_rep_data[6],
                            arr_rep_data[7],
                            arr_rep_data[12],
                            arr_rep_data[13],
                            arr_rep_data[14],
                            arr_rep_data[15],
                            arr_rep_data[16]
                            ))
        db.commit()
        for arrs in arr_rep_data[10]:
            connect.execute('''INSERT INTO payments (report_code, 
                                                date, 
                                                description, 
                                                sum, 
                                                paid_by_card) 
                                                VALUES 
                                                (?, ?, ?, ?, ?)''',
                                (arrs[0], 
                                arrs[1], 
                                arrs[2],
                                arrs[3],
                                arrs[4]
                                ))
            db.commit()
        win.destroy()
        tk.messagebox.showinfo("Інформація", "Інформацію успішно збережено в БД!")
    except Exception as e:
        tk.messagebox.showerror("Помилка", "Помилка: " + format(e))

from datetime import datetime
from ttkcalendar import *


# aa = test2()
# a = datetime.strptime(aa, '%d.%m.%y')
# bb = test2()
# b = datetime.strptime(bb, '%d.%m.%y')
#
# c = a - b
# print('Фініш: ' + a.strftime('%d.%m.%y'))
# print('Старт: ' + b.strftime('%d.%m.%y'))
# print(c.days+1)

def date_selection():
    # import sys
    root_calendar = Tkinter.Tk()
    root_calendar.title('Ttk Calendar')
    ttkcal = Calendar(root_calendar, firstweekday=calendar.MONDAY)
    ttkcal.pack(expand=1, fill='both')

    def cls(root):
        root.quit()
        root.destroy()

    # if 'win' not in sys.platform:
    #     style = ttk.Style()
    #     style.theme_use('clam')

    root_calendar.bind('<Button-1>', lambda event: cls(root_calendar))
    root_calendar.mainloop()

    x = ttkcal.selection
    # print ('x is: ', x)
    dta = x.strftime('%d.%m.%y')

    return dta

import openpyxl
import locale
import datetime

 

def daytime_pref():
    now = datetime.datetime.now()
    y1 = str(now.year)
    y1 = y1[2:]
    m1 = int(now.month)
    m1 = str("%02i" % m1)
    d1 = int(now.day)
    d1 = str("%02i" % d1)
    print(d1)
    h1 = int(now.hour)
    h1 = str("%02i" % h1)
    m2 = int(now.minute)
    m2 = str("%02i" % m2)
    s2 = int(now.second)
    s2 = str("%02i" % s2)
    daytime_pref = str('%s_%s_%s_%s_%s_%s' % (y1,m1,d1,h1,m2,s2))
    return daytime_pref

def fill_xls(data):
    from datetime import datetime
    wb = openpyxl.load_workbook(filename='/home/bozhko/Документи/Report_Python/template.xlsx')
    sheet = wb.active

    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    myDate = datetime.strptime(data[1], "%d.%m.%y")
    data_date_of_report = myDate.strftime('%d %B')
    data_name = data[0]
    data_name_latin = data[8]
    data_ind_number = data[9]
    data_code = data[2]
    data_days = data[5]
    data_pay_day = round(float(data[6]), 2)
    description_of_day = f'Добові ({data_days}х{data_pay_day} грн)'
    sheet['E64'].value = description_of_day

    payments = data[10]
    row_count = 65
    for payment in payments:
        sheet['C'+ str(row_count)].value = payment[1]
        sheet['E'+ str(row_count)].value = payment[2]
        sheet['P'+ str(row_count)].value = float(payment[3])
        row_count += 1 

    payments_by_card = data[11]
    row_count = 29
    num_row = 1
    for payment in payments_by_card:
        sheet['A'+ str(row_count)].value = f'{num_row}. Корп. Рах {payment[1]}'
        sheet['H'+ str(row_count)].value = float(payment[3])
        row_count += 1 
        num_row += 1


    sheet['B17'].value = data_name
    sheet['F16'].value = data_name_latin
    sheet['O6'].value = data_date_of_report
    sheet['M6'].value = data_code
    sheet['W57'].value = data_days
    sheet['V57'].value = data_pay_day

    #Додавання дати до назви файлу
    import datetime
    date_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    name = "Avance_Report_"
    extention = ".xlsx"
    full_name = name + date_name + extention
    print(date_name)
    print(full_name)

    wb.save(filename=full_name)

    wb.close()

def insert_data_to_xlsx(data, sheet2):
    import openpyxl
    import locale
    import datetime
    from datetime import datetime

    locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
    myDate = datetime.strptime(data[1], "%d.%m.%y")
    data_date_of_report = myDate.strftime('%d %B')
    data_name = data[0]
    data_name_latin = data[8]
    data_ind_number = data[9]
    data_code = data[2]
    data_days = data[5]
    data_pay_day = round(float(data[6]), 2)
    description_of_day = f'Добові ({data_days}х{data_pay_day} грн)'
    sheet2['E64'].value = description_of_day

    payments = data[10]
    row_count = 65

    for payment in payments:
        sheet2['C'+ str(row_count)].value = payment[1]
        sheet2['E'+ str(row_count)].value = payment[2]
        sheet2['P'+ str(row_count)].value = float(payment[3])
        row_count += 1 

    payments_by_card = data[11]
    row_count = 29
    num_row = 1
    for payment in payments_by_card:
        sheet2['A'+ str(row_count)].value = f'{num_row}. Корп. Рах {payment[1]}'
        sheet2['H'+ str(row_count)].value = float(payment[3])
        row_count += 1 
        num_row += 1

    sheet2['B17'].value = data_name
    sheet2['F16'].value = data_name_latin
    sheet2['O6'].value = data_date_of_report
    sheet2['M6'].value = data_code
    sheet2['W57'].value = data_days
    sheet2['V57'].value = data_pay_day
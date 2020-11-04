def order(data_dict, template, filename):
    '''
    DOCSTRING: Функція, яка формує Наказ в форматі .docx з шаблону
    INPUT: Словник даних (dictionary), імʼя шаблонного файлу (str), імʼя вихідного файлу (str) 
    OUTPUT: збережено готовий файл з заданим імʼям - filename
    '''

    from docxtpl import DocxTemplate

    try:
        doc = DocxTemplate(template)
        doc.render(data_dict)
        doc.save(filename)
    except Exception as e:
        print(f'Помилка під час формування файлу "{filename}" з шаблону "{template}" - {e}')

def rodovyi(fraze):
    '''
    DOCSTRING: Функція, яка повертає фразу 'fraze' в родовому відмінку
    INPUT: Слово / Фраза ('fraze'), в якій необхідно змінити відмінок 
    OUTPUT: Слово / Фраза, в родовому відмінку
    '''
    import pymorphy2

    morph = pymorphy2.MorphAnalyzer(lang='uk')
    wrd = fraze.split()
    str1 = ''
    try:
        for el in wrd:
            if len(el)>2:
                a = morph.parse(el)[0]
                b = a.inflect({'gent'}) 
                c = b.word
            else: c = el
            if el.istitle():
                c = c.title() 
            if str1:
                str1 = str1 +' ' + c
            else:
                str1 = str1 + c
        return(str1)
    except Exception as e:
        print(f'Помилка під час перетворення фрази "{fraze}" в родовий відмінок - {e}')

def filename_create(type, code):
    '''
    DOCSTRING: Функція, яка формує назву файлу в залежності від необхідного типу, дати і коду
    INPUT: Тип файлу для звіту - type (str), код - code (str)
    OUTPUT: Назва файлу (str) в залежності від дати і типу
    '''
    import datetime
    date_name = datetime.datetime.now().strftime('__%Y_%m_%d_%H_%M_%S')
    try:
        if type == 'AR':
            name = "AR__"
            extention = ".xlsx"
        elif type == 'OR':
            name = "OR__"
            extention = ".docx"
        else:
            print(f'Тип файлу {type} не визначено')
        full_name = name + code + date_name + extention
        return full_name
    except Exception as e:
        print(f'Помилка при формуванні назви файлу - {e}')

def order_from_list(data_list, template, filename):
    '''
    DOCSTRING: Функція, яка формує Наказ в форматі .docx з шаблону
    INPUT: Масив даних (list), імʼя шаблонного файлу (str), імʼя вихідного файлу (str) 
    OUTPUT: збережено готовий файл з заданим імʼям - filename
    '''

    from docxtpl import DocxTemplate
    # print(data_list)
    data_dict = {'date' : data_list[1], 'code' : data_list[2], 'name' : rodovyi(data_list[0]), 'start_bt' : data_list[3], 'finish_bt' : data_list[4], 'customer' : data_list[12], 'city' : data_list[13], 'job_type' : rodovyi('технічна консультація')}
    # print(data_dict)
    try:
        doc = DocxTemplate(template)
        doc.render(data_dict)
        doc.save(filename)
    except Exception as e:
        print(f'Помилка під час формування файлу "{filename}" з шаблону "{template}" - {e}')





if __name__ == "__main__":

    data_list = ['Божко Юрій Володимирович', '16.04.20', 'BOY200416', '07.04.20', '16.04.20', '10', '427.30', '4273.0', 
    'Yurii Bozhko', '12345678', [['BOY200416', '07.04.20', 'Проживання в готелі', '3848484', True], ['BOY200416', '07.04.20', 'Проживання в готелі', '3848484', True], ['BOY200416', '07.04.20', 'Проживання в готелі', '3848484', True]], 
    [['BOY200416', '07.04.20', 'Проживання в готелі', '3848484', True], ['BOY200416', '07.04.20', 'Проживання в готелі', '3848484', True]], 3848484.0, 3848484.0, 0.0, 'ТОВ "Дубномолоко"', 'м. Дубно']

    data_dict = {'date' : data_list[1], 'code' : data_list[2], 'name' : rodovyi(data_list[0]), 'start_bt' : data_list[3], 'finish_bt' : data_list[4], 'customer' : data_list[15], 'city' : data_list[16], 'job_type' : rodovyi('технічна консультація')}


    order(data_dict, 'template.docx', filename_create('OR', data_dict['code']))


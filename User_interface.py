def output_data(data):
    print(data)

def input_data(data=''):
    return input(data)

def print_data_console(list_data:list):#Вывод данных в консоль в читаемом формате  

    for i,data in enumerate(list_data):
        if data=='ID':
            ID_=list_data[i+1]
            Surname=list_data[i+3]
            Name =list_data[i+5]
            Fathername = list_data[i+7]
            Telefon = list_data[i+9]
            Comment = list_data[i+11]
            output_data('_'*200)
            output_data(f'|ID:{ID_}|Фамилия: {Surname}\t|Имя: {Name}\t|Отчество: {Fathername}\t|Телефон:{Telefon}\t|Комментарий: {Comment}')
    output_data('\n')
    
    
    

def text_menu(number):# Техт выводимый в основное меню 
    if number=='welcome_text':
        return 'Вас приветствует программа "Телефонная книга".\nВыберете какие операции будете выполнять:\n0 - Вывести всю базу в консоль.\n1 - Добавить в телефонный справочник.\n2 - Поиск в телефонном справочнике.\n3 - Удалить данные из телефонного справочника.\n4 - Изменить данные в телефонном справочнике.\n5 - Экспорт данных.\n6 - Импорт данных.\nДля выхода из программы "Телефонная книга" нажмите любой символ кроме 1-6 и Enter или Enter.\n=> '
    
    elif number=='text_end':
        return 'Программа ""Телефонная книга" закончила работу\n'
    elif number=='0':
        return 'Вывод базы данных в консоль.'    
    elif number=='1':
        return 'Добавление данных в телефонный справочник.'
    elif number=='2':
        return 'Поиск данных в телефонном справочнике.'
    elif number=='3':
        return 'Удаление данных из телефонного справочника.'
    elif number=='4':
        return 'Изменение данные в телефоном справочнике.'
    elif number=='5':
        return 'Экспорт данных.'
    elif number=='6':
        return 'Импорт данных.'
    elif number=='text_menu_repet':
        return 'Для продолжения программы "Телефонная книга"  нажмите Enter. Для выхода из программы "Телефонная книга" введите любой символ и Enter.\n=> '
    


def text_logg (text_data):# Техт логов
    if text_data=='text_start_program':
        return 'Старт программы "Телефонная книга"'
    elif text_data=='text_end':
        return 'Программа ""Телефонная книга" закончила работу\n'
    elif text_data=='0':
        return 'Пользователь выбрал пункт меню => Вывод базы данных в консоль.' 
    elif text_data=='1':
        return 'Пользователь выбрал пункт меню => Добавление данных в телефонный справочник.'
    elif text_data=='2':
        return 'Пользователь выбрал пункт меню => Поиск данных в телефонном справочнике.'
    elif text_data=='3':
        return 'Пользователь выбрал пункт меню => Удаление данных из телефонного справочника.'
    elif text_data=='4':
        return 'Пользователь выбрал пункт меню => Изменение данные в телефоном справочнике.'
    elif text_data=='5':
        return 'Пользователь выбрал пункт меню => Экспорт данных.'
    elif text_data=='6':
        return 'Пользователь выбрал пункт меню => Импорт данных.'
    elif text_data=='text_repet_start':
        return 'Пользователь выбрал продолжение работы программы "Телефонная книга"'


def text_metod_add (text_data):# Техт вывода в меню Добавить  
    if text_data=='id_new':
        return 'ID: '
    elif text_data=='surname':
        return 'Введите фамилию: '
    elif text_data=='name':
        return 'Введите имя: '
    elif text_data=='fathername':
        return 'Введите отчество: '
    elif text_data=='telefon':
        return 'Введите телефон в формате +79876543210: '
    elif text_data=='comment':
        return 'Введите комментарий: '
    elif text_data=='alarm_surname':
        return 'Фамилия введена не правильно, введите её заново: '
    elif text_data=='alarm_name':
        return 'Имя введена не правильно, введите его заново: '
    elif text_data=='alarm_fathername':
        return 'Отчество введена не правильно, введите его заново: '
    elif text_data=='alarm_telefon':
        return 'Телефон введена не правильно, введите его заново: '

def text_metod_add_logg (text_data): #Техт логов в меню Добавить
    if text_data=='surname':
        return 'Пользователь ввёл фамилию: '
    elif text_data=='name':
        return 'Пользователь ввёл имя: '
    elif text_data=='fathername':
        return 'Пользователь ввёл отчество: '
    elif text_data=='telefon':
        return 'Пользователь ввёл телефон: '
    elif text_data=='comment':
        return 'Пользователь ввёл комментарий: ' 

    elif text_data=='alarm_surname':
        return 'Пользователь ввёл фамилию не  корректно.'
    elif text_data=='alarm_name':
        return 'Пользователь ввёл имя не  корректно.'
    elif text_data=='alarm_fathername':
        return 'Пользователь ввёл отчество не корректно.'
    elif text_data=='alarm_telefon':
        return 'Пользователь ввёл телефон не корректно.'
   

def text_search_data_menu (text_data):  # Техт вывода в меню Поиск
    if text_data=='working_mode_search':
        return '\nВыберите по каким данным будет происходит запрос: \n1 - ID.\n2 - Фамилия. \n3 - Имя.\n4 - Отчество. \n5 - Телефон. \n6 - Комментарий.\nДля выхода из меню "Поиск в телефонном справочнике" нажмите любой символ кроме 1-6 и Enter или Enter.\n=>'
    
    
    elif text_data=='ID':
        return 'Введите ID для поиска: '
    elif text_data=='surname':
        return 'Введите Фамилию для поиска: '    
    elif text_data=='name':
        return 'Введите Имя для поиска: '    
    elif text_data=='fathername':
        return 'Введите Отчество для поиска: '
    elif text_data=='telefon':
        return 'Введите Телефон для поиска в формате +79991234568: '
    elif text_data=='comment':
        return 'Введите Комментарий для поиска: '
    elif text_data=='no_search':
        return 'Поиск по введенным данным не чего не нашёл.'
    
    elif text_data=='alarm_ID':
        return 'ID введён не правильно, введите его заново: '
    elif text_data=='alarm_surname':
        return 'Фамилия введён не правильно, введите её заново: '    
    elif text_data=='alarm_name':
        return 'Имя введён не правильно, введите его заново: '    
    elif text_data=='alarm_fathername':
        return 'Отчество введёно не правильно, введите его заново: '
    elif text_data=='alarm_telefon':
        return 'Телефон введёно не правильно, введите его заново: '



def text_search_data_logg (text_data):  # Техт вывода в меню Поиск
    if text_data=='ID_search':
        return 'Пользователь выбрал поиск по ID.'
    elif text_data=='surname_search':
        return 'Пользователь выбрал поиск по фамилии.'    
    elif text_data=='name_search':
        return 'Пользователь выбрал поиск по Имени.'    
    elif text_data=='fathername_search':
        return 'Пользователь выбрал поиск по Отчеству.'
    elif text_data=='telefon_search':
        return 'Пользователь выбрал поиск по Телефону.'
    elif text_data=='comment_search':
        return 'Пользователь выбрал поиск по Комментариям.'
    elif text_data=='end_search':
        return 'Выход из меню "Поиск в телефонном справочнике" .'

    elif text_data=='ID':
        return 'Пользователь ввёл ID для поиска:'
    elif text_data=='surname':
        return 'Пользователь ввёл Фамилию для поиска: '        
    elif text_data=='name':
        return 'Пользователь ввёл Имя для поиска: '
    elif text_data=='fathername':
        return 'Пользователь ввёл Отчество для поиска: '
    elif text_data=='telefon':
        return 'Пользователь ввёл Телефон для поиска: '
    elif text_data=='comment':
        return 'Пользователь ввёл Комментарий для поиска: '
    elif text_data=='no_search':
        return 'Поиск по введенным данным не чего не нашёл.'
    
    elif text_data=='alarm_ID':
        return 'Для поиска ID введён не правильно. '
    elif text_data=='alarm_surname':
        return 'Для поиска Фамилия введёна не правильно. '    
    elif text_data=='alarm_name':
        return 'Для поиска Имя введёно не правильно. '    
    elif text_data=='alarm_fathername':
        return 'Для поиска Отчество введёно не правильно. '
    elif text_data=='alarm_telefon':
        return 'Для поиска Телефон введён не правильно. '
    elif text_data=='alarm_comment':
        return 'Для поиска Комментарии введёны не правильно. '
    
    
def text_delete_data (text_data):
    if text_data=='text_working_mode':
        return 'Совпадений больше 1.\nДля удаления всех совпадений  нажмите Enter. Для удаления первого найденного введите любой символ и Enter.'


def text_delete_data_logg (text_data):
    if text_data=='working_mode_enter':
        return 'Совпадений больше 1. Пользователь выбрал удалить все совпадения.'
    elif text_data=='working_mode_symbol_enter':
        return 'Совпадений больше 1. Пользователь выбрал удалить первое найденное совпадение. '




def text_del_data_menu(text_data):
    if text_data=='working_mode_del':
        return '\nВыберите по каким данным будет происходит удаление : \n1 - ID.\n2 - Фамилия. \n3 - Имя.\n4 - Отчество. \n5 - Телефон. \n6 - Комментарий.\nДля выхода из меню "Поиск в телефонном справочнике" нажмите любой символ кроме 1-6 и Enter или Enter.\n=>'
    elif text_data=='len_zero_list_del':
        return '\nПо введенным данным не чего не найдено.\n'
    elif text_data=='print_del_list_data':
        return '\nТаблица с удалёнными данными:'
    elif text_data=='print_new_list_data':
        return '\nТаблица с новыми  данными:'
    
    
    elif text_data=='ID':
        return 'Введите ID для удаления данных в виде положительных чисел: '
    elif text_data=='surname':
        return 'Введите Фамилию для удаления данных: '    
    elif text_data=='name':
        return 'Введите Имя для удаления данных: '    
    elif text_data=='fathername':
        return 'Введите Отчество для удаления данных: '
    elif text_data=='telefon':
        return 'Введите Телефон для удаления данных в формате +79991234568: '
    elif text_data=='comment':
        return 'Введите Комментарий для удаления данных: '
    elif text_data=='end_del':
        return 'Пользователь выбрал выход из меню "Удалить данные из телефонного справочника"'
    
    
    elif text_data=='alarm_ID':
        return 'ID введён не правильно, введите его заново: '
    elif text_data=='alarm_surname':
        return 'Фамилия введён не правильно, введите её заново: '    
    elif text_data=='alarm_name':
        return 'Имя введён не правильно, введите его заново: '    
    elif text_data=='alarm_fathername':
        return 'Отчество введёно не правильно, введите его заново: '
    elif text_data=='alarm_telefon':
        return 'Телефон введёно не правильно, введите его заново: '
    
    elif text_data=='working_mode_no_ID':
        return 'Если хотите ввести ID заново введите Enter. Если хотите выйти из  меню " Изменить данные в телефонном справочнике." введите любой символ и нажмите Enter.'




def text_del_data_menu_logg(text_data):

    if text_data=='ID_del':
        return 'Пользователь выбрал Удаление данных по ID.'
    elif text_data=='surname_del':
        return 'Пользователь выбрал Удаление данных по фамилии.'    
    elif text_data=='name_del':
        return 'Пользователь выбрал Удаление данных по Имени.'    
    elif text_data=='fathername_del':
        return 'Пользователь выбрал Удаление данных по Отчеству.'
    elif text_data=='telefon_del':
        return 'Пользователь выбрал Удаление данных по Телефону.'
    elif text_data=='comment_del':
        return 'Пользователь выбрал Удаление данных по Комментариям.'
    elif text_data=='end_del':
        return 'Выход из меню "Удалить данные из телефонного справочника".'

    elif text_data=='ID':
        return 'Пользователь ввёл ID для Удаления данных: '
    elif text_data=='surname':
        return 'Пользователь ввёл Фамилию для Удаления данных:: '        
    elif text_data=='name':
        return 'Пользователь ввёл Имя для Удаления данных:: '
    elif text_data=='fathername':
        return 'Пользователь ввёл Отчество для Удаления данных:: '
    elif text_data=='telefon':
        return 'Пользователь ввёл Телефон для Удаления данных:: '
    elif text_data=='comment':
        return 'Пользователь ввёл Комментарий для Удаления данных:: '
    
    
    elif text_data=='alarm_ID':
        return 'ID для Удаления данных пользователь ввёл неправильно.'
    elif text_data=='alarm_surname':
        return 'Фамилию для Удаления данных пользователь ввёл неправильно.'    
    elif text_data=='alarm_name':
        return 'Имя для Удаления данных пользователь ввёл неправильно.'    
    elif text_data=='alarm_fathername':
        return 'Отчество для Удаления данных пользователь ввёл неправильно.'
    elif text_data=='alarm_telefon':
        return 'Телефон для Удаления данных пользователь ввёл неправильно.'
    elif text_data=='alarm_comment':
        return 'Комментарий для Удаления данных пользователь ввёл неправильно.'



def text_change_data_menu(text_data):
    if text_data=='ID':
        return 'Для изменения данных в контакте Телефонного справочника введите ID контакта.ID вводиться в виде положительного числа:'
    elif text_data=='alarm_ID':
        return 'ID введён не правильно, введите его заново: '
    elif text_data=='phonebook':
        return 'Телефонный справочник целиком:\n'
    elif text_data=='change_line_ phonebook':
        return 'Строка Телефонного справочника, в которой будут производиться изменения :'
    elif text_data=='ID_confirmation':
        return '\nЕсли ID введён правильно нажмите Enter.Если хотите поменять ID  введите 1 и нажмите Enter.Для выхода в основное меню введите любой символ кроме 1 и нажмите Enter. => '
    elif text_data=='end_change':
        return 'Выход из меню " Изменить данные в телефонном справочнике".'
    elif text_data=='working_mode_change':
        return '\nВыберите в каких данных будут происходит изменения : \n1 - Фамилия. \n2 - Имя.\n3 - Отчество. \n4 - Телефон. \n5 - Комментарий.\nДля выхода из меню "Поиск в телефонном справочнике" нажмите любой символ кроме 1-5 и Enter или Enter.\n=>'
    

   
    elif text_data=='surname':
        return 'Для внесения изменений введите новую Фамилию: '    
    elif text_data=='name':
        return 'Для внесения изменений введите новое Имя: '    
    elif text_data=='fathername':
        return 'Для внесения изменений введите новое Отчество: '
    elif text_data=='telefon':
        return 'Для внесения изменений введите новый Телефон в формате +79991234568: '
    elif text_data=='comment':
        return 'Для внесения изменений введите новый Комментарий: '
    
    
    
    
    elif text_data=='alarm_surname':
        return 'Фамилия введён не правильно, введите её заново: '    
    elif text_data=='alarm_name':
        return 'Имя введён не правильно, введите его заново: '    
    elif text_data=='alarm_fathername':
        return 'Отчество введёно не правильно, введите его заново: '
    elif text_data=='alarm_telefon':
        return 'Телефон введёно не правильно, введите его заново: '
    
    elif text_data=='no_ID_change':
        return 'По вашему запросу ID не найден.'
    elif text_data=='working_mode_no_ID':
        return 'Если хотите ввести ID заново введите Enter. Если хотите выйти из  меню " Изменить данные в телефонном справочнике." введите любой символ и нажмите Enter.'
    
    


def text_change_data_menu_logg(text_data):
    if text_data=='ID':
        return 'Пользователь ввёл ID для нахождения контакта и изменения в нём данных: '
    elif text_data=='alarm_ID':
        return 'Пользователь ввёл ID для нахождения контакта и изменения в нём данных Некорректно:'
    elif text_data=='ID_confirmation_mode_OK':
        return 'Пользователь подтвердил правильность ввода ID.'
    elif text_data=='ID_confirmation_mode_change':
        return 'Пользователь принял решение изменить ID для нахождения контакта и изменения в нём данных.'
    elif text_data=='end_change':
        return 'Пользователь выбрал выход из меню " Изменить данные в телефонном справочнике".'

    
    elif text_data=='surname_change':
        return 'Пользователь выбрал Изменение данных в поле Фамилии.'    
    elif text_data=='name_change':
        return 'Пользователь выбрал Изменение данных в поле Имя.'    
    elif text_data=='fathername_change':
        return 'Пользователь выбрал Изменение данных в поле Отчество.'
    elif text_data=='telefon_change':
        return 'Пользователь выбрал Изменение данных в поле Телефон.'
    elif text_data=='comment_change':
        return 'Пользователь выбрал Изменение данных в поле Комментарии.'
    

    
    elif text_data=='surname':
        return 'Пользователь ввёл новую Фамилию: '        
    elif text_data=='name':
        return 'Пользователь ввёл новое Имя: '
    elif text_data=='fathername':
        return 'Пользователь ввёл новое Отчество: '
    elif text_data=='telefon':
        return 'Пользователь ввёл новый Телефон: '
    elif text_data=='comment':
        return 'Пользователь ввёл новый Комментарий: '
    
    
    
    elif text_data=='alarm_surname':
        return 'Новая Фамилия введена неправильно. '    
    elif text_data=='alarm_name':
        return 'Новое Имя введено неправильно.'    
    elif text_data=='alarm_fathername':
        return 'Новое Отчество введено неправильно.'
    elif text_data=='alarm_telefon':
        return 'Новый Телефон введён неправильно. '
    
    elif text_data=='no_ID_change':
        return 'По запросу ID не найден.'


def text_export_data_menu(text_data):
    if text_data=='file_name':
        return 'Введите имя файла для експорта БД: '
    elif text_data=='alarm_file_name':
        return 'Имя файла введено неправильно, введите его заново: '
    elif text_data=='file_export_OK':
        return 'Экспорт файла выполнен.'



def text_export_data_menu_logg(text_data):
    if text_data=='file_name':
        return 'Пользователь ввёл имя файла для експорта: '
    elif text_data=='alarm_file_name':
        return 'Пользователь ввёл имя файла некорректно.'
    elif text_data=='file_export_OK':
        return 'Экспорт файла выполнен.'


def text_import_data_menu(text_data):
    if text_data=='file_name':
        return 'Введите имя файла для импорта БД. Название вводиться без .txt: '
    elif text_data=='alarm_file_name':
        return 'Имя файла введено неправильно, введите его заново: '
    elif text_data=='file_break':
        return 'Файла с таким именем не существует .'
    elif text_data=='working_mode_file_break':
        return 'Если хотите продолжить работу в меню "Импорт данных" то нажмите Enter. Если хотите вейте из меню "Импорт данных" то введите любой символ и нажмите Enter. => '
    elif text_data=='impor_finish':
        return 'Импортирование файла выполнено.'




def text_import_data_menu_logg(text_data):
    if text_data=='file_name':
        return 'Введите имя файла для импорта БД: '
    elif text_data=='alarm_file_name':
        return 'Имя файла введено неправильно, введите его заново: '
    elif text_data=='file_break':
        return 'Оператор ввёл имя не существующего файла.'
    elif text_data=='working_mode_file_new_job':
        return 'Пользователь выбрал продолжение работы в меню "Импорт файла".'
    elif text_data=='working_mode_file_end':
        return 'Пользовать выбрал выход из меню  "Импорт файла".'
    elif text_data=='impor_finish':
        return 'Файл импортирован.'
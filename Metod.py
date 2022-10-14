from bisect import insort
from cgitb import reset
import json
import User_interface as ui
import ID_definition as id_def
import Check as ch
import Logger as logg
import File_links as fl


def read_break_json(adress_file):
    with open (adress_file,'r', encoding='utf-8') as data_file:
        data_string=data_file.read()
           
    
    new_data_string=data_string.split('"')

    data_atribut=['ID','Surname','Name','Fathername','Telefon','Comment']

    temp_data_list=[]

    for i,data in enumerate( new_data_string ):
        for at in  data_atribut:
            if data == at:
                temp_data_list.append(at)
                temp_data_list.append(new_data_string[i+2])
    

    return temp_data_list


def search_data (list_data,atribut,search):# Поис данных в списке

    
    search_data_list=[]

    dictionary_atribut=\
        {
            'ID':0,
            'Surname':2,
            'Name':4,
            'Fathername':6,
            'Telefon':8,
            'Comment':10
        }

    
    for i, dat in enumerate(list_data):
        if dat == atribut and list_data[i+1]==search:
            for ra in range(12):
                delta=dictionary_atribut.get(atribut)
                search_data_list.append(list_data[i-int(delta)+ra])
    return search_data_list


def delete_data (list_data:list,atribut,delete_data):# Удааление данных из списка

    """
    Удаление будет происходить всей строки целиком по atribut и delete_data.
    """

    dictionary_atribut=\
        {
            'ID':0,
            'Surname':2,
            'Name':4,
            'Fathername':6,
            'Telefon':8,
            'Comment':10
        }
    del_list_data=[]
    del_only_one=False
    delit_ID_list=[]
    
    if list_data.count(delete_data)>1:
        text_working_mode=ui.text_delete_data('text_working_mode')
        working_mode=ui.input_data(text_working_mode)
        if working_mode == '':
            logg.log_data(ui.text_delete_data_logg('working_mode_enter'))
            del_only_one=True
        else:
            logg.log_data(ui.text_delete_data_logg('working_mode_symbol_enter'))

    for  i, dat in enumerate (list_data):
        if dat == atribut and list_data[i+1]==delete_data:
            delta=dictionary_atribut.get(atribut)
            delit_ID_list.append(i-int(delta))
            
    
    
    for k,del_index in enumerate(delit_ID_list):
        for i in range(12):
            del_list_data.append(list_data[del_index-(k*12)])
            list_data.pop(del_index-(k*12))
        if del_only_one==False:
            break

            
            
    
    return del_list_data,list_data


def overwriting_data_json(list_data:list, address_file):# Перезапись данных в файл json

    zero_list={'0':1}

    while True:
        try:
            with open(address_file, 'w', encoding='utf8') as file:
                file.write(json.dump(zero_list,address_file, ensure_ascii=False ))
        except AttributeError:
            break
    
    for i,data in enumerate(list_data):

        if data == 'ID':
            id_new= list_data[i+1]
        elif data == 'Surname':
            surname=  list_data[i+1]
        elif data == 'Name':
            name=  list_data[i+1]
        elif data == 'Fathername':
            fathername=  list_data[i+1]
        elif data == 'Telefon':
            telefon =  list_data[i+1]
        elif data == 'Comment':
            comment =  list_data[i+1]

            person_dict = {'ID': id_new, 'Surname': surname, 'Name': name, 'Fathername':fathername,'Telefon':telefon, 'Comment': comment }

            with open(address_file, 'a', encoding='utf8') as file:
                file.write(json.dumps(person_dict, ensure_ascii=False, indent=4))
    

def change_data (data_list:list,ID_change,atribut,change_data_my):# Изменение данных в списке


    dictionary_atribut=\
        {
            'Surname':3,
            'Name':5,
            'Fathername':7,
            'Telefon':9,
            'Comment':11
        }

    for i,data in enumerate(data_list):
        if data=='ID' and data_list[i+1]==ID_change:
            delta=dictionary_atribut.get(atribut)
            data_list.pop(i+delta)
            data_list.insert(i+delta,change_data_my)
            break

    return data_list


def export_data_txt(address_file_json,address_file_txt,file_name):# Запись в файл при экспортирование 
    data_list=read_break_json(address_file_json)
    
    new_address= address_file_txt+f'\{file_name}.txt'

    with open (new_address,'a',encoding='utf-8') as data:
        for i, da in enumerate(data_list):
            if da=='ID':
                temp=da+':'+data_list[i+1]+','
                data.write(temp)
            elif da=='Surname':
                temp=da+':'+data_list[i+1]+','
                data.write(temp)
            elif da=='Name':
                temp=da+':'+data_list[i+1]+','
                data.write(temp)
            elif da=='Fathername':
                temp=da+':'+data_list[i+1]+','
                data.write(temp)
            elif da=='Telefon':
                temp=da+':'+data_list[i+1]+','
                data.write(temp)
            elif da=='Comment':
                temp=da+':'+data_list[i+1]+',\n'
                data.write(temp)

    return


def import_data_txt (address_file_json,address_file_txt,file_name): # Чтение из файл и запись в файл json
    
    data_list=[]
    da_list=[]
    new_address_file=address_file_txt+f'\{file_name}.txt'

    try:
        data=open(new_address_file,'r',encoding='utf-8')
        for da in data:
            da=da.replace('\ufeff','')
            da=da.replace(':',',')
            da_list=da.split(',')
            for d in da_list:
                data_list.append(d)
            da_list.clear()
        data.close

        overwriting_data_json(data_list, address_file_json)
    except:
        return False

    return True



def output_data_console_menu():# Вывод базы данных в консоль.
    adress_file=fl.file_links('file_json')
    
    data_list=read_break_json(adress_file)

    ui.print_data_console(data_list)
    


def add_data_menu(): #Добавление данных  
    file_new=fl.file_links('file_json')
    
    id_new= id_def.new_id(ui.text_metod_add('id_new'))
    ui.output_data(ui.text_metod_add('id_new')+id_new)

    surname= ch.imput_name(ui.text_metod_add('surname'),ui.text_metod_add('alarm_surname'),ui.text_metod_add_logg ('surname'),ui.text_metod_add_logg ('alarm_surname'))
    name = ch.imput_name(ui.text_metod_add('name'),ui.text_metod_add('alarm_name'), ui.text_metod_add_logg ('name'), ui.text_metod_add_logg ('alarm_name'))
    fathername = ch.imput_name(ui.text_metod_add('fathername'),ui.text_metod_add('alarm_fathername'),ui.text_metod_add_logg ('fathername'), ui.text_metod_add_logg ('alarm_fathername'))
    telefon = ch.imput_telefon (ui.text_metod_add('telefon'),ui.text_metod_add('alarm_telefon'),ui.text_metod_add_logg ('telefon'), ui.text_metod_add_logg ('alarm_telefon'))
    comment = ui.input_data(ui.text_metod_add('comment'))

    comment=comment.replace(' ','')
    if len(comment)>0:
        logg.log_data(ui.text_metod_add_logg ('comment')+comment)
    
    person_dict = {'ID': id_new, 'Surname': surname, 'Name': name, 'Fathername':fathername,'Telefon':telefon, 'Comment': comment }
    
    with open(file_new, 'a', encoding='utf8') as file:
        file.write(json.dumps(person_dict, ensure_ascii=False, indent=4,separators=(', ', ': ')))


def search_data_menu ():# Поиск по заданным параметрам
    
    adress_file=fl.file_links('file_json')
    
    data_list=read_break_json(adress_file)
    
    working_mode_search=ui.input_data(ui.text_search_data_menu ('working_mode_search'))

    if working_mode_search=='1':
        atribut='ID'
        logg.log_data(ui.text_search_data_logg('ID_search'))
        search =ch.imput_ID(ui.text_search_data_menu('ID'),ui.text_search_data_menu('alarm_ID'),ui.text_search_data_logg ('ID'),ui.text_search_data_logg ('alarm_ID'))

    elif working_mode_search=='2':
        logg.log_data(ui.text_search_data_logg('surname_search'))
        atribut='Surname'
        search =ch.imput_name(ui.text_search_data_menu('surname'),ui.text_search_data_menu('alarm_surname'),ui.text_search_data_logg ('surname'),ui.text_search_data_logg ('alarm_surname'))

    elif working_mode_search=='3':
        logg.log_data(ui.text_search_data_logg('name_search'))
        atribut='Name'
        search =ch.imput_name(ui.text_search_data_menu('name'),ui.text_search_data_menu('alarm_name'),ui.text_search_data_logg ('name'),ui.text_search_data_logg ('alarm_name'))

    elif working_mode_search=='4':
        logg.log_data(ui.text_search_data_logg('fathername_search'))
        atribut='Fathername'
        search =ch.imput_name(ui.text_search_data_menu('fathername'),ui.text_search_data_menu('alarm_fathername'),ui.text_search_data_logg ('fathername'),ui.text_search_data_logg ('alarm_fathername'))

    elif working_mode_search=='5':
        logg.log_data(ui.text_search_data_logg('telefon_search'))
        atribut='Telefon'
        search =ch.imput_telefon (ui.text_search_data_menu('telefon'),ui.text_search_data_menu('alarm_telefon'),ui.text_search_data_logg ('telefon'), ui.text_search_data_logg ('alarm_telefon'))

    elif working_mode_search=='6':
        logg.log_data(ui.text_search_data_logg('comment_search'))
        atribut='Comment'
        search =ui.input_data(ui.text_search_data_menu('comment'))

        logg.log_data(ui.text_search_data_logg('comment')+search)

    else:
        logg.log_data(ui.text_search_data_logg('end_search'))
        return
    


    search_data_list = search_data(data_list,atribut,search)

    if len (search_data_list)>0:
        ui.print_data_console(search_data_list)
    else:
        ui.output_data(ui.text_search_data_logg('no_search'))
        logg.log_data(ui.text_search_data_logg('no_search'))
        return
    
def del_data_menu():# удаление данных из БД

    address_file=fl.file_links('file_json')
    
    data_list=read_break_json(address_file)

    working_mode_del=ui.input_data(ui.text_del_data_menu ('working_mode_del'))

    if working_mode_del=='1':
        atribut='ID'
        logg.log_data(ui.text_del_data_menu_logg('ID_del'))
        delete_data_my =ch.imput_ID(ui.text_del_data_menu('ID'),ui.text_del_data_menu('alarm_ID'),ui.text_del_data_menu_logg('ID'),ui.text_del_data_menu_logg ('alarm_ID'))

    elif working_mode_del=='2':
        logg.log_data(ui.text_del_data_menu_logg('surname_del'))
        atribut='Surname'
        delete_data_my =ch.imput_name(ui.text_del_data_menu('surname'),ui.text_del_data_menu('alarm_surname'),ui.text_del_data_menu_logg ('surname'),ui.text_del_data_menu_logg ('alarm_surname'))

    elif working_mode_del=='3':
        logg.log_data(ui.text_del_data_menu_logg('name_del'))
        atribut='Name'
        delete_data_my =ch.imput_name(ui.text_del_data_menu('name'),ui.text_del_data_menu('alarm_name'),ui.text_del_data_menu_logg ('name'),ui.text_del_data_menu_logg ('alarm_name'))

    elif working_mode_del=='4':
        logg.log_data(ui.text_del_data_menu_logg('fathername_del'))
        atribut='Fathername'
        delete_data_my =ch.imput_name(ui.text_del_data_menu('fathername'),ui.text_del_data_menu('alarm_fathername'),ui.text_del_data_menu_logg ('fathername'),ui.text_del_data_menu_logg ('alarm_fathername'))

    elif working_mode_del=='5':
        logg.log_data(ui.text_del_data_menu_logg('telefon_del'))
        atribut='Telefon'
        delete_data_my =ch.imput_telefon (ui.text_del_data_menu('telefon'),ui.text_del_data_menu('alarm_telefon'),ui.text_del_data_menu_logg ('telefon'),ui.text_del_data_menu_logg ('alarm_telefon'))

    elif working_mode_del=='6':
        logg.log_data(ui.text_del_data_menu_logg('comment_del'))
        atribut='Comment'
        delete_data_my =ui.input_data(ui.text_del_data_menu('comment'))

        logg.log_data(ui.text_del_data_menu_logg('comment')+delete_data_my)

    else:
        ui.output_data(ui.text_del_data_menu('end_del'))
        logg.log_data(ui.text_del_data_menu_logg('end_del'))
        return
    


    delete_list, new_data_list= delete_data (data_list,atribut,delete_data_my)

    if len(delete_list)==0:
        ui.output_data(ui.text_del_data_menu('len_zero_list_del'))
        logg.log_data(ui.text_del_data_menu('len_zero_list_del'))
        return
    else:
        ui.output_data(ui.text_del_data_menu('print_del_list_data'))
        ui.print_data_console(delete_list)

        ui.output_data(ui.text_del_data_menu('print_new_list_data'))
        ui.print_data_console(new_data_list)

        overwriting_data_json(new_data_list, address_file)

    return



def change_data_menu():# Изменение данных в базе
    address_file=fl.file_links('file_json')
    
    data_list=read_break_json(address_file)

    ui.output_data(ui.text_change_data_menu('phonebook'))
    
    ui.print_data_console(data_list)

    while True:

        ID_change=ch.imput_ID(ui.text_change_data_menu('ID'),ui.text_change_data_menu('alarm_ID'),ui.text_change_data_menu_logg('ID'),ui.text_change_data_menu_logg ('alarm_ID'))

        search_list_data_ID = search_data(data_list,'ID',ID_change)
        
        if len(search_list_data_ID)==0:
            ui.output_data(ui.text_change_data_menu('no_ID_change'))
            logg.log_data(ui.text_change_data_menu_logg('no_ID_change'))

            working_mode_no_ID=ui.input_data(ui.text_change_data_menu ('working_mode_no_ID'))
            
            if working_mode_no_ID == '':
                logg.log_data(ui.text_change_data_menu_logg('ID_confirmation_mode_change'))
                continue
            else:
                ui.output_data(ui.text_change_data_menu('end_change'))
                logg.log_data(ui.text_change_data_menu_logg('end_change'))
                return

        
        
        ID_confirmation=ui.input_data(ui.text_change_data_menu('ID_confirmation'))
        
        ui.print_data_console(search_list_data_ID)

        if ID_confirmation=='':
            logg.log_data(ui.text_change_data_menu_logg('ID_confirmation_mode_OK'))
        
            working_mode_change=ui.input_data(ui.text_change_data_menu ('working_mode_change'))

            if working_mode_change=='1':
                logg.log_data(ui.text_change_data_menu_logg('surname_change'))
                atribut='Surname'
                change_data_my =ch.imput_name(ui.text_change_data_menu('surname'),ui.text_change_data_menu('alarm_surname'),ui.text_change_data_menu_logg ('surname'),ui.text_change_data_menu_logg ('alarm_surname'))
                break

            elif working_mode_change=='2':
                logg.log_data(ui.text_change_data_menu_logg('name_change'))
                atribut='Name'
                change_data_my =ch.imput_name(ui.text_change_data_menu('name'),ui.text_change_data_menu('alarm_name'),ui.text_change_data_menu_logg ('name'),ui.text_change_data_menu_logg ('alarm_name'))
                break

            elif working_mode_change=='3':
                logg.log_data(ui.text_change_data_menu_logg('fathername_change'))
                atribut='Fathername'
                change_data_my =ch.imput_name(ui.text_change_data_menu('fathername'),ui.text_change_data_menu('alarm_fathername'),ui.text_change_data_menu_logg ('fathername'),ui.text_change_data_menu_logg ('alarm_fathername'))
                break

            elif working_mode_change=='4':
                logg.log_data(ui.text_change_data_menu_logg('telefon_change'))
                atribut='Telefon'
                change_data_my =ch.imput_telefon (ui.text_change_data_menu('telefon'),ui.text_change_data_menu('alarm_telefon'),ui.text_change_data_menu_logg ('telefon'),ui.text_change_data_menu_logg ('alarm_telefon'))
                break

            elif working_mode_change=='5':
                logg.log_data(ui.text_change_data_menu_logg('comment_change'))
                atribut='Comment'
                change_data_my =ui.input_data(ui.text_change_data_menu('comment'))

                logg.log_data(ui.text_change_data_menu_logg('comment')+change_data_my)
                break

            else:
                ui.output_data(ui.text_change_data_menu('end_change'))
                logg.log_data(ui.text_change_data_menu_logg('end_change'))
                return

        
        
        elif ID_confirmation=='1':
            logg.log_data(ui.text_change_data_menu_logg('ID_confirmation_mode_change'))
            continue
        else:
            ui.output_data(ui.text_change_data_menu('end_change'))
            logg.log_data(ui.text_change_data_menu_logg('end_change'))
            return
    
    new_list_data = change_data (data_list,ID_change,atribut,change_data_my)

    overwriting_data_json(new_list_data, address_file)
    



def import_data_menu():# Импорт в базу данных
    address_file_json=fl.file_links('file_json')
    address_file_txt=fl.file_links('file_import')
    
    while True:
        file_name =ch.imput_name(ui.text_import_data_menu('file_name'),ui.text_import_data_menu('alarm_file_name'),ui.text_import_data_menu_logg ('file_name'),ui.text_import_data_menu_logg ('alarm_file_name'))

        file_OK=import_data_txt (address_file_json,address_file_txt,file_name)

        if file_OK==True:
            ui.output_data(ui.text_import_data_menu('impor_finish'))
            logg.log_data(ui.text_import_data_menu_logg('impor_finish'))
            return
        else:
            ui.output_data(ui.text_import_data_menu('file_break'))
            logg.log_data(ui.text_import_data_menu_logg('file_break'))
            working_mode_file_break=ui.input_data(ui.text_import_data_menu('working_mode_file_break'))
            if working_mode_file_break=='':
                logg.log_data(ui.text_import_data_menu_logg('working_mode_file_new_job'))
                continue
            else:
                logg.log_data(ui.text_import_data_menu_logg('working_mode_file_end'))
                return





def export_data_menu():# Экспорт из базы данных
    address_file_json=fl.file_links('file_json')
    address_file_txt=fl.file_links('file_export')
    file_name =ch.imput_name(ui.text_export_data_menu('file_name'),ui.text_export_data_menu('alarm_file_name'),ui.text_export_data_menu_logg ('file_name'),ui.text_export_data_menu_logg ('alarm_file_name'))

    

    export_data_txt(address_file_json,address_file_txt,file_name)

    ui.output_data(ui.text_export_data_menu('file_export_OK'))
    logg.log_data(ui.text_export_data_menu_logg('file_export_OK'))
    

    return
    

    

    

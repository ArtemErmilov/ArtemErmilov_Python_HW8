from bisect import insort
import User_interface as ui
import Logger as log
import Metod as met
from os import system



def start_PhoneBook():

    log.log_data(ui.text_logg('text_start_program'))
    new_start=True
    

    while True:
        
        if new_start==True:
            system ('cls')
            working_mode=ui.input_data(ui.text_menu('welcome_text'))
        else:
            
            working_mode=ui.input_data(ui.text_menu('text_menu_repet'))
            if working_mode=='':
                new_start=True
                log.log_data(ui.text_logg('text_repet_start'))
                continue
            else:
                 ui.output_data(ui.text_menu('text_end'))
                 log.log_data(ui.text_logg('text_end'))
                 break

        if working_mode=='0': # Вывод базы данных в консоль.
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.output_data_console_menu()
            new_start=False
        
        elif working_mode=='1':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.add_data_menu()
            new_start=False
        
        elif working_mode=='2':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.search_data_menu()
            new_start=False
        
        elif working_mode=='3':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.del_data_menu()
            new_start=False

        elif working_mode=='4':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.change_data_menu()
            new_start=False
        
        elif working_mode=='5':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.import_data_menu()
            new_start=False
        
        elif working_mode=='6':
            system ('cls')
            ui.output_data(ui.text_menu(working_mode))
            log.log_data(ui.text_logg(working_mode))
            met.export_data_menu()
            new_start=False

        
        else:
            ui.output_data(ui.text_menu('text_end'))
            log.log_data(ui.text_logg('text_end'))
            break


from cgitb import text
import User_interface as ui
import Logger as logg

def imput_ID (text_in:str,text_alarm,text_logg,text_logg_alarm):
    ID_number=ui.input_data(text_in)
    while True:
        try:
            logg.log_data(text_logg+ID_number)
            if int(ID_number)>=0:
                return ID_number
            else:
                logg.log_data(text_logg_alarm)
                ID_number=ui.input_data(text_alarm)
                continue               
        except:
            logg.log_data(text_logg_alarm)
            ID_number=ui.input_data(text_alarm)
            continue


def imput_name(text_in:str,text_alarm,text_logg,text_logg_alarm):
    new_text=ui.input_data(text_in)
    while True:
        logg.log_data(text_logg+new_text)
        new_text=new_text.replace(' ','')
        if len(new_text)>0:
            return new_text
        else:
            logg.log_data(text_logg_alarm)
            new_text=ui.input_data(text_alarm)
            continue

def imput_telefon (text_in:str,text_alarm,text_logg,text_logg_alarm):
    new_telefon=ui.input_data(text_in)
    while True:
        logg.log_data(text_logg+new_telefon)
        new_telefon=new_telefon.replace(' ','')
        new_telefon
        if new_telefon[0]=='+' and len(new_telefon)==12 and new_telefon[1:].isdigit() ==True:
            return new_telefon
        else:
            logg.log_data(text_logg_alarm)
            new_telefon=ui.input_data(text_alarm)
            continue
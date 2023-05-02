from collections import UserDict
from string import ascii_letters
from datetime import datetime, timedelta
import os
import locale
locale.setlocale(locale.LC_ALL, "")

#Теги до нотаток
class Tags:
    pass

#Процедури и функції з нотатками
class Record:
    def __init__(self) -> None:
        #Екземпляр словника нотаток та тег нотатки
        ex_note = Notes()
        ex_tag = Tags()
        ex_text = ''

    def add_note(self):
        print('add')

    def edit_note(self):
        print('edit')

    def del_note(self):
        print('del')

    def print_notes(self):
        print('print')

    def search_note(self):
        print('search')

#Довідник нотаток
class Notes(UserDict):
    pass
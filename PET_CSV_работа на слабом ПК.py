
def documentation ():
    '''предположила, что парсить данные можно в интерпретароре, т к рабочий ноут не тянет объемные excel и ВПР; мне нужно перевести файлы в csv, сопоставить и создать новый excel
    Будет три файла:
        1. file_1.csv
        2. file_2.csv
        которые буду парсить между собой
        3. файл Net_v_1C.xlsx
    '''
    pass

import csv
from openpyxl import Workbook     
from datetime import datetime

def create_total_file_xlsx ():

    list_total = [
         {'Примечание': 'нет в OZON' },
         {'Дата':0},
         {'Тип':0},
         {'IDD документа':0},
         {'Постинг':0},
         {'Артикул':0},
         {'Товар':0},
         {'Количество':0},
         {'Цена':0},
         {'Сумма':0}
        ]
    
    #чтобы текущая дата была в наименовании файла и когда бы не обратился саппорт, файл сформировался с уникальным наименованием    
    current_date = datetime.now()
    file_name = datetime.now().strftime ('Нет_в_1С_ОЗОН_%Y-%m-%d_%H-%M-%S.xlsx')
    #создание файла
    wb = Workbook ()
    ws = wb.active
    #наименования столбцов в виде констант, т к формат файла регламентирован для загрузки в обработку
    ws ['A1'] = 'Примечание'
    ws ['B1'] = 'Дата'
    ws ['C1'] = 'Тип'
    ws ['D1'] = 'IDD документа'
    ws ['E1'] = 'Постинг'
    ws ['F1'] = 'Артикул'
    ws ['G1'] = 'Товар'
    ws ['H1'] = 'Количество'
    ws ['I1'] = 'Цена'
    ws ['J1'] = 'Сумма'
    #запись в файл, наверно будет цикл потом
    ws.append ([1,2])
    wb.save (file_name)
    pass


def create_csv_from_xlsx ():
    #with open (file_name, 'wt') as fout:
     #   cout = csv.DictWriter (fout, ['Примечание', 'Дата', 'Тип', 'IDD документа', 'Постинг', 'Артикул', 'Товар', 'Количество','Цена','Сумма'] )
      #  cout.writeheader ()
       # cout.writerows (list_total)
    pass


def create_csv_1 ():
    pass

def create_csv_2 ():
    pass

def parsing ():
    pass


print (documentation.__doc__)
a = create_total_file_xlsx ()


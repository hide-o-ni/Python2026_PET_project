def documentation ():
    '\nТы здесь, потому что не можешь посчитать два числа -  помни об этом'
    pass

def summation (num1, num2):
    print ("\nСложение: ")
    return num1 + num2

def subtract (num1, num2):
    print ("\nВычитание: ")
    return num1 - num2

def product (num1, num2):
    print ("\nУмножение: ")
    return num1 * num2

def division (num1, num2):
    print ("\nДеление: ")
    if num2 != 0:
        return float (num1 / num2)
    else:
        print ("\nна 0 делить нельзя, умник")

def squared (num1, num2):
    print ("\n Первое число - это число для работы, второе число - степень")
    print ("\nВозведение в степень: ")
    return pow (num1, num2)


def squareroot (num1):
    #импорт проводится сразу при запуске модуля 
    #логично для одной операции вывести импорт в функцию
    import math 
    print ("\nКвадратный корень: ")    
    result =  math.sqrt (num1)
    return result




def menu ():
    print (end = "")
    print ("Калькулятор")
    print (f"1. Сложение. Введи число 1")
    print (f"2. Вычитание. Введи число 2")
    print (f"3. Умножение. Введи число 3")
    print (f"4. Деление. Введи число 4")
    print (f"5. Возведение в степень. Введи число 5")
    print (f"6. Квадратный корень. Введи число  6")
    print (f"0. Выход. Введи число 0")
    while True:
        try:
            number = int(input("\nну, давай номер операции:  "))
            return number
        except:
            print ("маму твою позвать, чтобы она за тебя номер ввела? не правильно ")
            



def check_any_number ():
    while True:
        try:
            any_number = float (input())
            if any_number:
                print ("\nпойдет, далее..")
                return any_number
        except:
            print ("\n и вроде же не так много от тебя требуется..это по-твоему число? ")
        




def calculator ():
    dir_calculator = {
        1: summation,
        2: subtract,
        3: product,
        4: division,
        5: squared
        }

    while True:
        print ("\n")
        task = menu ()

        if task == 0:
            print ("\nой фсе")
            break
        
        elif task == 6:
            num1 = check_any_number ()
            print ( squareroot (num1))
            break



        if  task in dir_calculator:
            print ("\nВведи первое число для расчетов: ")
            num1 = check_any_number ()
            if num1:
                print ("\nВведи второе число для расчетов: ")
                num2 =  check_any_number ()
                if num2:
                    result =  dir_calculator [task] (num1, num2)
                    print (result)
        else:
            print ("\nу тебя лапки, да? неправильно!")
    



    
#
print (documentation.__doc__)    
calculator ()

    
    
    

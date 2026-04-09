def menu (number):
    print (end = "")
    print ("Калькулятор")
    print (f"1. Сложение. Введите число 1", {number})
    print (f"2. Вычитание. Введите число 2", {number})
    print (f"3. Умножение. Введите число 3", {number})
    print (f"4. Деление. Введите число 4", {number})
    print (f"5. Квадратный корень. Введите число 5", {number})
    print (f"6. Возведение в степень. Введите число 6", {number})
    print (f"0. Выход. Введите число 0", {number})


def documentation ():
    'Ты здесь, потому что не можешь посчитать два числа -  помни об этом'
    pass

def chech_nums (num1, num2):
    if isinstance(num1, (int, float)) and isinstance (num2, (int, float)):
        return True


def calculator (number):
    menu = {
            '1': summation,
            '2': subtract,
            '3': product,
            '4': division,
            '5': squareroot,
            '6': squared
            }
    while True:
        task = menu ()

        if task == '0':
            break

        if task == '5':
            float (input (num1))
            return squareroot (num1)

        
        int (input(number))
        if number in list_menu:
            pass #ввод чисел 2 вида + вызов ф-ций
    else:
        print ("не так много от тебя требуется - ввести верное число меню")

def summation (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def product (num1, num2):
    return num1 * num2

def division (num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print ("на 0 делить нельзя, умник")

def squareroot (num1):
    #импорт проводится сразу при запуске модуля и нагружает память
    #логично для одной операции вывести импорт в функцию
    from math import sqrt
    return float(math.sqrt (num1))

def squared (num1, num2):
    return pow (num1, num2)
    



    
#
print (documentation.__doc__)    
calculator ()

    
    
    

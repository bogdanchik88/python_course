import random
from ctypes import *
import time
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
playgame = True
money = 1000

#Функция ввода значения
def getInput(digit, message):
    color(7)
    ret = ''
    while (ret == '' or not ret in digit):
       ret = input(message)
    return ret

# #Установка цвета текста
def color (c):
    windll.Kernel32.SetConsoleTextAttribute(h,c)

# #Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while(ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print('введите целое число: ')
    return ret

# #Вывод на экран цветного, обрамленного звездочками текста
def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print('*'*(len(s)))
    print(''+s)
    print('*'*(len(s)))




#АНИМАЦИЯ БРОСКА КОСТЕЙ
def getdice():
    count = random.randint(3,8)
    sleep = 3
    while(count > 0):
        color(count + 7)
        x = random.randint(1,6)
        y = random.randint(1,6)
        print(''*8,'--- ---')
        print(''*10,f'|{x}| |{y}|')
        print(''*8,'--- ---')
        sleep+=1
        count-=1
    return x+y

#Игра кости
def dice():
    global money
    while(playgame and money > 0):
        print()
        colorLine(3,'Добро пожаловать в игру КОСТИ!')
        color(14)
        print(f'У тебя на счету {money} рублей!')

        stavka = getIntInput(0,money,f'Какова ваша ставка?')# проблемное место-не вызывается


        playRound = True
        result = getdice()
        while(playRound and money > 0 and stavka >0):
            if (stavka > money):
                stavka = money
            color(11)
            print(f'Ваша ставка {stavka} рублей')
            print(f'сумма кубиков - {result}')
            x=getInput('0,1,2,3','каков ваш прогноз?, 0(выйти),1(больше),2(меньше),3(равно)')

            if(x != '0'):
                if(stavka>money):
                    stavka= money

                money-=stavka
                result2 = getdice()

                win = False
                if(result>result2):
                    if(x == '1'):
                        win = True
                elif(result<result2):
                    if(x == '2'):
                        win = True
                if(x!='3'):
                    if(win):
                        money+=stavka+stavka
                        pobeda(stavka)
                    else:
                        proigr(stavka)
                elif(x == '3'):
                    if(result==result2):
                        money+=stavka*2
                        pobeda(stavka*2)
                        stavka*=3
                result = result2
            else:
                money-=stavka
                playRound = False


#Основное тело
def main():
    global money
    while(playgame and money>0):
        colorLine(10,'Здравствуй, игрок!')
        color(14)
        print(f'У тебя на счету {money} рублей!')

        color(13)
        print('''Ты можешь сыграть в
                           1.рулетку
                           2.кости
                           3.однорукий бандит
                           0.покинуть игру''')
        color(13)
        #time.sleep(10)
        x=getInput('0,1,2,3','\nВ какую игру сыграешь? ')

        if x == '0':
            print('Жаль, что вы покинули игру')
            time.sleep(2)
            break
        elif x=='1':
            pass
        elif x=='2':
            dice()
        elif x=='3':
            pass







# a = getIntInput(1,100,'Введите число от 1 до 100: ')
# #Метод, загружающий сумму средств игрока из файла
# def loadMoney():
#     pass
#
# #Метод, записывающий сумму средств игрока в файл
def saveMoney():pass







def pobeda(result):
    color(14)
    print(f'Вы выиграли{result}рублей!!!!!!'
           f'у тебя осталось {money} денег!!!11111!!!!!!1!!!!!11!1111!!!1')


def proigr(result):
    color(14)
    print(f'Вы проиграли{result}рублей!!!!!!'
        f'у тебя осталось {money} денег!!!11111!!!!!!1!!!!!11!1111!!!1')



# def say(f):
#     print('Привет, ')
#     int(input(''))
#     a = 174398
#     b = 908874456
#     c = b-a
#     d = 1959028
#     o = c-d
#     g = 1234567
#     f = o-g
#     return f
# print(say('1000000000'))

main()
# ВКЛЮЧЕНИЕ КОДА

NUM2 = False
NUM5 = False
NUM6 = False
NUM8_LETTER = False
NUM8_NUMBER = False
NUM12 = False
NUM13 = False
NUM14_1 = False
NUM14_2 = False
NUM14_3 = False
NUM15 = False
NUM16 = False
NUM17 = False
NUM23 = False
NUM25_1 = False
NUM25_2 = False
NUM27 = False

THEORY_PEREVOD = False
THEORY = False
SYSTEM_TABL = True

# Формулы для задач

# 7 Задание

# Аудио 
# I=K*m*i*t
# I - Размер в битах
# K - Кол-во каналов (моно - 1, стерео - 2, квадро - 4)
# m - Частота дискретизации (1 кГц = 1000 Гц)
# i - разрешение в битах
# t - Время в секундах

# Фото 
# N=2**i
# I=x*y*i
# I - Размер в битах
# x - Длина
# y - Высота
# i - вес 1 цвета в битах
# N - Кол-во цветов (палитра)

# Видео
# По факту то же самое что фото, только появляются FPS (кадры в секунду)
# I = x*y*i*FPS*t


# 11 Задание
# I=K*i
# N=2**i
# I - Бит на 1 пароль
# K - Длина пароля
# N - Мощность алфавита
# i - Вес 1 символа

#    /8    /1024      /1024      /1024
# Бит → Байт → Килобайт → Мегабайт → Гигабайт



# ТАБЛИЦА СИСТЕМ

if SYSTEM_TABL == True:
    SYST = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*"
    X=int(input("Система счисления >>> "))
    z=""
    for i in SYST:
        if str(i)!=str(SYST[X]):
            z+=i
        else:
            break
    print(z)


# ПЕРЕВОД СИСТЕМ СЧИСЛЕНИЯ

if THEORY_PEREVOD == True:
    def PEREVOD(Z,SYS):
        AFT=""
        ALF="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while Z!=0:
            if Z%SYS<=9:
                AFT+=str(Z%SYS)
            else:
                AFT+=ALF[(Z%SYS)-10]
            Z=Z//SYS
        AFT=AFT[::-1]
        return(AFT)

    def OBR(A,SYSTEM):
        return int(str(A),SYSTEM)

#PEREVOD(Z,SYS) = Вызов функции перевода в любую систему из десятичной, Z,SYS передаваемые данные
#Z = Число которое мы переводим
#SYS = Система счисления в которую мы переводим
#AFT = Число после перевода
#ALF = Алфавит

#OBR(A, SYSTEM) = Вызов функции перевода в десятичную
#A = Число которое мы переводим
#SYSTEM = Система счисления из которой мы переводим

#ТЕОРИЯ ПО СРЕЗАМ
if THEORY == True:
    ALPHA="0123456789"
    a=ALPHA[:5] # Всё до числа с индексом 5 включительно
    b=ALPHA[5:] # Всё после числа с индексом 5 не включительно
    c=ALPHA[::-1] # Переворот числа
    d=ALPHA[5:7] # Числа начиная с индекса 5 не включительно до числа с индексом 7 включительно
    e=ALPHA[0] # Первое число
    f=ALPHA[-1] # Последнее число


#ТЕОРИЯ ПО ЛОГИЧЕСКИМ ОПЕРАЦИЯМ

# ¬ A, A = (not(A))
# A ∧ B, A ⋅ B = A and B
# A ∨ B, A + B = A or B
# A → B = A <= B
# A ↔ B, A ≡ B, A ∼ B = A==B
# A ⊕ B = A != B


#ТЕОРИЯ ПО ЧЕРЕПАХЕ

# Внутри без учета границ (n-1)(m-1)
# С учетом границ (n+1)(m+1)
# Площадь n*m
# Периметр (n+m)*2



#ОБРАЗЦЫ РЕШЕНИЯ ЗАДАЧ

# 2

if NUM2 == True:
    print("x y z w")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x or y) and (not(y==z)) and (not(w))) == 1:  #((x or y) and (not(y==z)) and (not(w))) - Логическое выражение
                        print(x,y,z,w)


# 5

if NUM5==True:
    def PEREVOD(Z,SYS):
        AFT=""
        ALF="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while Z!=0:
            if Z%SYS<=9:
                AFT+=str(Z%SYS)
            else:
                AFT+=ALF[(Z%SYS)-10]
            Z=Z//SYS
        AFT=AFT[::-1]
        return(AFT)

    for N in range(1, 10000):
        Z=PEREVOD(N,2)
        if N%3==0:
            Z=Z+Z[-3:]
        else:
            Z=Z+PEREVOD((N%3)*3,2)
        R=int(Z,2)
        if R>=200:
            print(N)
            break


# 6
if NUM6==True:
    import turtle
    from turtle import *

    t=turtle                # Чтобы не писать постоянно turtle.left(90) или turtle.forward(34*k)
    k=10                    # Чтобы линии были подлиннее
    screensize(1920,1080)   # Размеры окна
    t.left(90)              # Т.к. в питоне черепаха изначально смотрит вправо 

    for i in range(2):
        t.forward(14*k)
        t.left(270)
        t.back(12*k)
        t.right(90)

    t.up()                  # Поднять хвост

    t.forward(9*k)
    t.right(90)
    t.back(7*k)
    t.left(90)

    t.down()                # Опустить хвост

    for i in range(2):
        t.forward(13*k)
        t.right(90)
        t.forward(6*k)
        t.right(90)

    done()                  # Чтобы окно не закрывалось


# 8.1

if NUM8_LETTER==True:
    # Для слов из букв
    import itertools
    from itertools import *

    k=0
    for x in product("АКОРСТ", repeat=5):  # repeat= - длина слова
        WORD=""
        for i in x:
            WORD+=i
        k+=1  # Если узнать под каким номером
        if k%2==0:  # Четный номер
            if WORD[0]!="A" and WORD[0]!="С" and WORD[0]!="Т":  # Не начинается с А, С или Т
                if WORD.count("О")==2:  # Только 2 буквы О
                    print(k,WORD)


# 8.2

if NUM8_NUMBER==True:
    # Для слов из цифр
    import itertools
    from itertools import *

    k=0
    for x in product("0123456", repeat=7):  # repeat= - длина слова
        NUM=""
        for i in x:
            NUM+=i
        if NUM[0]!="0": # Т.к. числа не могут начинаться с 0
            NUM1=NUM  # Создаём дубликат строки если будем что-то менять
            NUM1=NUM1.replace("0","*").replace("2","*").replace("4","*").replace("6","*").replace("1","X").replace("3","X").replace("5","X") 
            if NUM1.count("*X")==2:  # Содержит ровно 2 сочетания вида чет+нечёт
                k+=1  # Если нужно посчитать кол-во
    print(k)
            

# 12

# Машину Тьюринга игнорируем, т.к. проще решить руками
# Смотрим исполнителя "Редактор"
if NUM12 == True:
    for n in range(3,10001):
        STROKA = "1"+ "2"*n
        
        while ("12" in STROKA) or ("322" in STROKA) or ("222" in STROKA):
            if "12" in STROKA:
                STROKA=STROKA.replace("12", "2", 1) # Заменить 12 на 2 только 1 раз
            if "322" in STROKA:
                STROKA=STROKA.replace("322", "21", 1)
            if "222" in STROKA:
                STROKA=STROKA.replace("222", "3", 1)
        SUMM=0
        for i in STROKA:
            SUMM+=int(i)
        
        if SUMM==15:
            print(n)
            break
            
# 13



# 14.1
# Значение ариф. выражения ALPHA записали в системе счисления с основанием X, определите кол-во цифр с числ значением 
if NUM14_1 == True:
    def PEREVOD(Z,SYS):
        AFT=""
        ALF="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while Z!=0:
            if Z%SYS<=9:
                AFT+=str(Z%SYS)
            else:
                AFT+=ALF[(Z%SYS)-10]
            Z=Z//SYS
        AFT=AFT[::-1]
        return(AFT)

    alph="ABCDEFGHIJKLMNOPQ"
    K=2*2187**2020+729**2021-2*243**2022+81**2023-2*27**2024-6561
    C=PEREVOD(K,27)
    counter=0
    for i in alph:
        counter+=C.count(i)
    print(counter)


# 14.2
# Операнды ариф. выражения записаны в системе счисления с основанием x, вычислите частное от деления ариф. выражения на y
if NUM14_2 == True:
    alph="0123456789ABCDEFGHIJKLMNOPQRS"
    for x in alph:
        A=int(f"923{x}874",29)+int(f"524{x}6152",29)
        if A%28==0:
            print(f"Для x = {x}, Ответ: {A//28}")


# 14.3
# Значение ариф. выражения где x - целое положительное не привышающее y записали в z-ричной системе счисления, определите значение x при котором в z-ричной записи содержится d чего-то
if NUM14_3==True:
    def PEREVOD(Z,SYS):
        AFT=""
        ALF="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while Z!=0:
            if Z%SYS<=9:
                AFT+=str(Z%SYS)
            else:
                AFT+=ALF[(Z%SYS)-10]
            Z=Z//SYS
        AFT=AFT[::-1]
        return(AFT)

    for x in range(1,3001):
        V = 9*11**210+8*11**150-x
        AFTER = PEREVOD(V,11)
        if AFTER.count("0")==60:
            print(x)


# 15
if NUM15 == True:
    P=list(range(15,41)) # Отрезок P от 15 до 40
    Q=list(range(21,63)) # Отрезок Q от 21 до 62
    A=[] 

    k=0
    for x in range(10,70):
        if ((x in P)<=(((x in Q) and (not(x in A)))<=(not(x in P)))) == 0: # Идём от обратного чтобы не считать сколько раз должно быть 1
            A.append(x) # Я не объясню, это просто надо запомнить
    print(A)
# Если требуют наименьшую возвожную длину - добавляем, если требуют наибольшую - убираем
# Ответом всегда будет разность между какими-то числами отрезков


# 16
if NUM16 == True:
    import functools
    from functools import *

    @cache

    def G(n):
        if n < 10:
            return 2*n
        if n >= 10:
            return G(n-2)+1
    
    def F(n):
        return 2*(G(n-3)+8)
    
    for i in range(16000):
        F(i)

    print(F(15548))

# 17
if NUM17 == True:
    f=open("17_23757.txt") # Открываем данный файл

    B=[] # Просто массив для хранения чисел с файла
    dv_ch=[] # Массив двузначных чисел
    for i in f:
        B.append(int(i)) # Добавляем числа из файла в массив B
    
    for i in B:
        if len(str(i))==2: # Проверка является ли число двузначным
            dv_ch.append(int(i)) 
    
    min_dv_ch=min(dv_ch) # Минимальное двузначное число

    OTV=[] # Массив с подходящими условию суммами чисел
    for i in range(len(B)-1): # Берём числа от 0 и до кол-ва чисел в массиве B (-1 для того чтобы пары нормально работали)
        a=B[i] # Число из массива B с индексом i
        b=B[i+1] # Пара к числу a
        
        if ((len(str(a))==2) + (len(str(b))==2)) == 1: # Условие 1
            if (a+b)%min_dv_ch==0: # Условие 2
                OTV.append(a+b)
    print(len(OTV),max(OTV)) # len(OTV) - длина массива, т.е. кол-во пар подходящих условию. max(OTV) - наибольшая сумма пар 


# 23
if NUM23 == True:
    def F(x,y): # x - число от которого идём, y - число к которому мы идём
        if x==y:
            return 1
        if x<y or x==7: # x<y - если мы перешагнули, т.е. не туда пошёл алгоритм, x==7 - по условию не содержит число 7
            return 0
        
        k=0
        k+=F(x-1,y)
        k+=F(x-4,y)
        k+=F(x//3,y)
        return k
    
    print(F(19,13)*F(13,2)) # Сколько существует алгоритмов идущих от 19 до 13 (должны пройти через 13 по условию) и от 13 до конечного числа 2 (умножение можно объяснить графом, но я его тут чертить не собираюсь)


# 25.1
if NUM25_1 == True:
    import math
    from math import *

    LIST=list(range(800000,800000+5000)) # Числа большие 800000
    k=0
    for x in LIST:
        A=set() # Почему не list()? Всё просто, чтобы делители не повторялись
        for i in range(2, int(sqrt(x)+1)): # Идём от 2 (т.к. нужны делители не считая 1 и самого числа) до корня из числа (т.е. ровно до середины) 
            if x%i==0: # Действительно ли i является делителем числа x?
                A.add(i) # Добавляем делитель
                A.add(x//i) # Добавляем парный делитель (возьмём к примеру делители числа 20: 1 2 4 5 10 20. Парный к делителю 1 - 20, к делителю 2 - 10 и т.д.)
        A=sorted(A) # Превращаем сложный массив в простой просто отсортировав его
        if len(A)!=0: # Если список натуральных делителей не пуст
            M=max(A)+min(A) # M – сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа.
            if str(M)[-1]=="4": # Если M оканчивается на 4
                print(x,M)
                k+=1 # Эти 3 строки чтобы просто вывести первые 10 чисел подходящих по всем условиям
                if k==10:
                    break
# Если в 25.1 просят найти простые делители числа, то это конечно жопа, но решаемо. Проще всего будет вынести проверку на делители в функцию и работать с ней, ибо иначе будет овердохрена строк кода в которых запутаться проще простого


# 25.2
if NUM25_2 == True:
    import fnmatch
    from fnmatch import *

    for x in range(0,10**10,1917): # Идём от 0 до данного нам по условию лимита 10**10 с шагом равным нашему делителю чтобы обработка шла быстрее
        if fnmatch(str(x),"3?12?14*5"): # Подходит ли число x (обязательно строковое) 
            if x%1917==0: # Повторная проверка делится ли
                print(x,x//1917)
# Если в 25.2 в маске просят четную или нечётную, беги

# 27

if NUM27 == True:
    f = open('27_B_18314.txt')
    f.readline() # Отсекаем 1 строку т.к. в ней просто прописаны буквы x и y

    cl_1 = [] # Кластер 1
    cl_2 = [] # Кластер 2
    cl_3 = [] # Кластер 3

    for i in f:
        x,y = map(float,i.replace(',','.').split()) # Записываем координаты в переменные x,y делая из них значения float функцией map (применяет заданную функцию ко всем аргументам) и при этом заменяем запятые на точки ибо питон с запятыми работать не умеет
        if x < -10: # Отсекаем кластеры друг от друга
            cl_1.append([x,y]) # Добавляем в массив кластеров звёзды к нему относящиеся
        if x > 16:
            cl_2.append([x,y])
        if (x>-10)and(x<16):
            cl_3.append([x,y])

    def centroid(cl): # Функция которая ищет центроид кластера (бывают и минимальное и максимальное расстояние, читай условие)
        min_sum = 10 ** 10 # Берём наибольшее чтобы найти наименьшее
        for i in cl: # i - координаты 1 звезды
            summ_dlin = 0
            for j in cl: # j - координаты 2 звезды
                dlina = abs(j[0]-i[0])+abs(j[1]-i[1]) # Формула Манхэттенского расстояния (бывает и другое, читай условие)
                summ_dlin += dlina
            if summ_dlin < min_sum: # Если сумма длин от 1 звезды до остальных меньше чем текущая минимальная сумма, то перезаписываем
                min_sum = summ_dlin
                centr_cl = i 
        return centr_cl

    centr_1 = centroid(cl_1)
    centr_2 = centroid(cl_2)
    centr_3 = centroid(cl_3)

    Px = int((centr_1[0] + centr_2[0] + centr_3[0]) / 3 * 1000) # По условию ср. ариф координаты x центроидов умноженное на 1000
    Py = int((centr_1[1] + centr_2[1] + centr_3[1]) / 3 * 1000) # По условию ср. ариф координаты y центроидов умноженное на 1000

    print(Px,Py)



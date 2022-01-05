from random import *
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=[]
    neg=[]
    null=[]
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")    
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """
    Меняет местами mini и maxi если mini больше maxi
    :param a :вводимое пользавателем неправельное минимальное число диапазона
    :param b :вводимое пользавателем неправельное максимальное число диапазона
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    Выдает n случайных чисел от а до b 
    :param int n : сколко раз нужно повторить цкал
    :param int a : какое минимальное число диапазона будет выведен
    :param int b : какое максимальное число диапазона будет выведен
    :param list loend : хранит даные выведенных чисел
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:int,n:int,nol:int):
    """
    Проверяет и запоменает в списки pos, neg, null 
    из списка loend сколько позитивных,негативных и нулей 
    :param int p :
    :param int n :
    :param int nol :
    :list loend : хранит даные проверенных чисел
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    loend.append(el)
    loend.sort()
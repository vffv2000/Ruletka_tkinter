#auto-py-to-exe
from tkinter import *
import random
ball = 0
number = 0
money = 100
stavka = 1
win = 0
koef=1
numbers = []

def change():
    print(spinbox.get())
    Label(text=str(spinbox.get())) \
        .grid(row=0, column=10, columnspan=3, rowspan=2, sticky=N + S + W + E)

def start():
    window1 = Tk()
    window1.title("Правила")
    window1.geometry("250x200")
    label = Label(window1, text="Тут типо правила должны быть"
                                " но их тут нет")
    label.pack(anchor=CENTER, expand=1)

def num_start():
    global money
    global number
    ball = random.randint(0, 36)
    print("выпало - ",ball,"Ваше число - ", number)
    stavka = spinbox.get()
    stavka = int(stavka)
    s = stavka * 35
    if number == ball:

        money = money +s
        Label(text=str(s)) \
            .grid(row=0, column=16, columnspan=3, rowspan=2, sticky=N + S + W + E)
        zapisb="Выпало - "+str(ball)+" Вы победили. Ваш выйгрыш - "+str(s)

        box.insert(0,zapisb )
        box.itemconfig(0, {'bg': '#92e1a9'})
    else:
        Label(text=str(0)) \
            .grid(row=0, column=16, columnspan=3, rowspan=2, sticky=N + S + W + E)
        zapisb = "Выпало - " +str(ball) + " Вы Проиграли."
        box.insert(0, zapisb)
        box.itemconfig(0, {'bg': '#f83b3b'})
    money = money - stavka
    Label(text=money).grid(row=0, column=4, columnspan=3, rowspan=2, sticky=N + S + W + E)
    Label(text="Выпало - " + str(ball)).grid(row=13, column=20, sticky=N + S + W + E)

    print(stavka, money)

def nums_2x():
    global numbers
    global money
    global koef
    ball = random.randint(0, 36)
    print("выпало - ", ball, "Ваше число - ", number)
    stavka = spinbox.get()
    stavka = int(stavka)
    if ball in numbers:
        money = money + (stavka * koef)
        Label(text=str(stavka * koef - stavka)) \
            .grid(row=0, column=16, columnspan=3, rowspan=2, sticky=N + S + W + E)
        zapisb = "Выпало - " + str(ball) + " Вы победили. Ваш выйгрыш - " + str(stavka * koef-stavka)
        box.insert(0, zapisb)
        box.itemconfig(0, {'bg': '#92e1a9'})
    else:
        Label(text=str(0)) \
            .grid(row=0, column=16, columnspan=3, rowspan=2, sticky=N + S + W + E)
        zapisb = "Выпало - " + str(ball) + " Вы Проиграли."
        box.insert(0, zapisb)
        box.itemconfig(0, {'bg': '#f83b3b'})
    money = money - stavka
    Label(text=money).grid(row=0, column=4, columnspan=3, rowspan=2, sticky=N + S + W + E)
    Label(text="Выпало - " + str(ball)).grid(row=13, column=20, sticky=N + S + W + E)



window = Tk()
for c in range(39): window.columnconfigure(index=c, weight=1)
for r in range(23): window.rowconfigure(index=r, weight=1)
window.title("Игра в РУЛЕТКУ") # ТИТЛ
window.resizable(width= False,height=False)# запрет на изменение окна
window.geometry('1000x600') # Размеры окна

Label(text="Счёт:")\
    .grid(row=0, column=1,columnspan=3,rowspan=2,sticky=N+S+W+E)
money_label=Label(text=str(money))
money_label.grid(row=0, column=4,columnspan=3,rowspan=2,sticky=N+S+W+E)

Label(text="Ставка:")\
    .grid(row=0, column=7,columnspan=3,rowspan=2,sticky=N+S+W+E)
stavka_label=Label(text=str(stavka))\
    .grid(row=0, column=10,columnspan=3,rowspan=2,sticky=N+S+W+E)

Label(text="Выйрыш:")\
    .grid(row=0, column=13,columnspan=3,rowspan=2,sticky=N+S+W+E)
win_label=Label(text=str(win))\
    .grid(row=0, column=16,columnspan=3,rowspan=2,sticky=N+S+W+E)

def num0():
    global number
    number=0
    num_start()
Button(text="0",command=num0,background='#92e1a9').grid(row=2, column=25,rowspan=6,sticky=N+S+W+E)
def num1():
    global number
    number=1
    num_start()
Button(text="1 ",command=num1,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=26,rowspan=2,sticky=N+S+W+E)
def num2():
    global number
    number=2
    num_start()
Button(text="2 ",command=num2,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=26,rowspan=2,sticky=N+S+W+E)
def num3():
    global number
    number=3
    num_start()
Button(text="3 ",command=num3,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=26,rowspan=2,sticky=N+S+W+E)
def num4():
    global number
    number=4
    num_start()
Button(text="4 ",command=num4,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=27,rowspan=2,sticky=N+S+W+E)
def num5():
    global number
    number=5
    num_start()
Button(text="5 ",command=num5,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=4, column=27,rowspan=2,sticky=N+S+W+E)
def num6():
    global number
    number=6
    num_start()
Button(text="6 ",command=num6,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=2, column=27,rowspan=2,sticky=N+S+W+E)
def num7():
    global number
    number=7
    num_start()
Button(text="7 ",command=num7,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=28,rowspan=2,sticky=N+S+W+E)
def num8():
    global number
    number=8
    num_start()
Button(text="8 ",command=num8,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=28,rowspan=2,sticky=N+S+W+E)
def num9():
    global number
    number=9
    num_start()
Button(text="9 ",command=num9,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=28,rowspan=2,sticky=N+S+W+E)
def num10():
    global number
    number=10
    num_start()
Button(text="10",command=num10,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=29,rowspan=2,sticky=N+S+W+E)
def num11():
    global number
    number=11
    num_start()
Button(text="11",command=num11,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=29,rowspan=2,sticky=N+S+W+E)
def num12():
    global number
    number=12
    num_start()
Button(text="12",command=num12,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=29,rowspan=2,sticky=N+S+W+E)
def num13():
    global number
    number=13
    num_start()
Button(text="13",command=num13,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=30,rowspan=2,sticky=N+S+W+E)
def num14():
    global number
    number=14
    num_start()
Button(text="14",command=num14,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=4, column=30,rowspan=2,sticky=N+S+W+E)
def num15():
    global number
    number=15
    num_start()
Button(text="15",command=num15,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=2, column=30,rowspan=2,sticky=N+S+W+E)
def num16():
    global number
    number=16
    num_start()
Button(text="16",command=num16,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=31,rowspan=2,sticky=N+S+W+E)
def num17():
    global number
    number=17
    num_start()
Button(text="17",command=num17,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=31,rowspan=2,sticky=N+S+W+E)
def num18():
    global number
    number=18
    num_start()
Button(text="18",command=num18,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=31,rowspan=2,sticky=N+S+W+E)
def num19():
    global number
    number=19
    num_start()
Button(text="19",command=num19,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=32,rowspan=2,sticky=N+S+W+E)
def num20():
    global number
    number=20
    num_start()
Button(text="20",command=num20,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=32,rowspan=2,sticky=N+S+W+E)
def num21():
    global number
    number=21
    num_start()
Button(text="21",command=num21,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=32,rowspan=2,sticky=N+S+W+E)
def num22():
    global number
    number=22
    num_start()
Button(text="22",command=num22,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=33,rowspan=2,sticky=N+S+W+E)
def num23():
    global number
    number=23
    num_start()
Button(text="23",command=num23,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=4, column=33,rowspan=2,sticky=N+S+W+E)
def num24():
    global number
    number=24
    num_start()
Button(text="24",command=num24,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=2, column=33,rowspan=2,sticky=N+S+W+E)
def num25():
    global number
    number=25
    num_start()
Button(text="25",command=num25,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=34,rowspan=2,sticky=N+S+W+E)
def num26():
    global number
    number=26
    num_start()
Button(text="26",command=num26,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=34,rowspan=2,sticky=N+S+W+E)
def num27():
    global number
    number=27
    num_start()
Button(text="27",command=num27,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=34,rowspan=2,sticky=N+S+W+E)
def num28():
    global number
    number=28
    num_start()
Button(text="28",command=num28,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=35,rowspan=2,sticky=N+S+W+E)
def num29():
    global number
    number=29
    num_start()
Button(text="29",command=num29,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=35,rowspan=2,sticky=N+S+W+E)
def num30():
    global number
    number=30
    num_start()
Button(text="30",command=num30,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=35,rowspan=2,sticky=N+S+W+E)
def num31():
    global number
    number=31
    num_start()
Button(text="31",command=num31,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=6, column=36,rowspan=2,sticky=N+S+W+E)
def num32():
    global number
    number=32
    num_start()
Button(text="32",command=num32,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=4, column=36,rowspan=2,sticky=N+S+W+E)
def num33():
    global number
    number=33
    num_start()
Button(text="33",command=num33,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=2, column=36,rowspan=2,sticky=N+S+W+E)
def num34():
    global number
    number=34
    num_start()
Button(text="34",command=num34,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=6, column=37,rowspan=2,sticky=N+S+W+E)
def num35():
    global number
    number=35
    num_start()
Button(text="35",command=num35,background='#635c5c',relief =RIDGE ,activebackground ='#262626').grid(row=4, column=37,rowspan=2,sticky=N+S+W+E)
def num36():
    global number
    number=36
    num_start()
Button(text="36",command=num36,background='#f83b3b',relief =RIDGE ,activebackground ='#A52A2A').grid(row=2, column=37,rowspan=2,sticky=N+S+W+E)

def k1_1():
    global numbers
    global koef
    koef=3
    numbers = [3,6,9,12,15,18,21,24,27,30,33,36]
    nums_2x()
def k1_2():
    global numbers
    global koef
    koef=3
    numbers = [2,5,8,11,14,17,20,23,26,29,32,35]
    nums_2x()
def k1_3():
    global numbers
    global koef
    koef=3
    numbers = [1,4,7,10,13,16,19,22,25,28,31,34]
    nums_2x()
def num1_12():
    global numbers
    global koef
    koef=3
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    nums_2x()
def num13_24():
    global numbers
    global koef
    koef=3
    numbers = [13,14,15,16,17,18,19,20,21,22,23,24]
    nums_2x()
def num25_36():
    global numbers
    global koef
    koef=3
    numbers = [25,26,27,28,29,30,31,32,33,34,35,36]
    nums_2x()

Button(text="2k1",command=k1_3).grid(row=6, column=38,rowspan=2,sticky=N+S+W+E)
Button(text="2k1",command=k1_2).grid(row=4, column=38,rowspan=2,sticky=N+S+W+E)
Button(text="2k1",command=k1_1).grid(row=2, column=38,rowspan=2,sticky=N+S+W+E)

Button(text="   1й сектор   ",command=num1_12).grid(row=8, column=26,columnspan=4,rowspan=2,sticky=N+S+W+E)
Button(text="    2й сектор    ",command=num13_24).grid(row=8, column=30,columnspan=4,rowspan=2,sticky=N+S+W+E)
Button(text="    3й сектор     ",command=num25_36).grid(row=8, column=34,columnspan=4,rowspan=2,sticky=N+S+W+E)

def num_red():
    global numbers
    global koef
    koef=2
    numbers = [1,3,5,7,9,12,14,18,16,21,19,23,27,25,30,32,34,36]
    nums_2x()
def num_black():
    global numbers
    global koef
    koef = 2
    numbers = [2,6,4,8,11,10,13,15,17,20,24,22,26,29,28,33,31,35]
    nums_2x()
def num19_36():
    global numbers
    global koef
    koef = 2
    numbers = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    nums_2x()
def num1_18():
    global numbers
    global koef
    koef = 2
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    nums_2x()
def even():
    global numbers
    global koef
    koef = 2
    numbers = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    nums_2x()
def odd():
    global numbers
    global koef
    koef = 2
    numbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    nums_2x()
Button(text="   1-18  ",command=num1_18,bd =1,relief =RIDGE ,activebackground ='#808080').grid(row=10, column=26,columnspan=2,rowspan=2,sticky=N+S+W+E)
Button(text="   Чётные  ",command=even).grid(row=10, column=28,columnspan=2,rowspan=2,sticky=N+S+W+E)
Button(text="   Красное  ",command=num_red,background='#f83b3b').grid(row=10, column=30,columnspan=2,rowspan=2,sticky=N+S+W+E)
Button(text="   Чёрное  ",command=num_black,background='#635c5c').grid(row=10, column=32,columnspan=2,rowspan=2,sticky=N+S+W+E)
Button(text="   19-36  ",command=num19_36).grid(row=10, column=34,columnspan=2,rowspan=2,sticky=N+S+W+E)
Button(text="   Нечётные  ",command=odd).grid(row=10, column=36,columnspan=2,rowspan=2,sticky=N+S+W+E)

Win_number=Label(text="Выпало - "+str(ball)).grid(row=13, column=20,sticky=N+S+W+E)


Label(text="Ваша ставка").grid(row=13, column=30,columnspan=3,sticky=N+S+W+E)
spinbox=Spinbox( from_=1.0, to=1000.0, command=change)
spinbox.grid(row=14, column=31,columnspan=2,rowspan=2,sticky=N+S+W+E)



Label(text="Ваши последнии ставки").grid(row=3, column=1,columnspan=15,sticky=N+S+W+E)
box = Listbox(selectmode=EXTENDED,yscrollcommand='True')
box.grid(row=4, column=1,columnspan=15,rowspan=18,sticky=N+S+W+E)
scroll=Scrollbar(command=box.yview)

Button(text="Правила ",command=start).grid(row=20, column=25,columnspan=13,rowspan=2,sticky=N+S+W+E)
Label(text="").grid(row=23, column=39)
box.insert(0,"Сделай первую ставку)")
window.mainloop()


from tkinter import *
import random
#game_run в эту переменную будем записывать False при завершении игры, чтобы запретить делать ходы когда
#уже выявлен победитель.
#field это будет двумерный список, в котором будут храниться кнопки игрового поля. Ходом будет изменение кнопки
# на 'X' или 'O'.
#cross_count в этой переменной мы будем отслеживать количество крестиков на поле.
root = Tk()
root.title('Крестики-нолики')
game_run = True
field = []
cross_count = 0

def new_game():
    """Будет вызываться при нажатии кнопки начала новой игры. На поле убираются все нолики и крестики
    """
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'skyblue'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    """Вызывается после нажатия на поле, при попытке поставить крестик. Если игра не завершена
       то крестик ставится.
    """
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')
#coz переменная крестик или нолик
def check_win(coz):
    """Осуществляет проверку выйгрыша. Перебирает все возможные комбинации полей, образующих линию.
       Если зафиксирована победа то меняем цвет кнопок на синий и присваеваем game_run False.
    """
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], coz)
        check_line(field[0][n], field[1][n], field[2][n], coz)
    #проверяем диагонали
    check_line(field[0][0], field[1][1], field[2][2], coz)
    check_line(field[2][0], field[1][1], field[0][2], coz)

def check_line(a1, a2, a3, coz):
    if a1['text'] == coz and a2['text'] == coz and a3['text'] == coz:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

#Действия компьютера:
# 1. Если компьютеру представился шанс победы он не должен его упустить.
# 2. Если игрок выставил два крестика в ряд, компьюте пытается предотвратить победу игрока.
# 3. Случайный ход если первые два пункта не выполняются.

def can_win(a1, a2, a3, coz):
    """Проверяет возможность победы
    """
    res = False
    if a1['text'] == coz and a2['text'] == coz and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == coz and a2['text'] == ' ' and a3['text'] == coz:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == coz and a3['text'] == coz:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

# Графический интерфейс

for row in range(3):
    line = []
    for col in range(3):
        button  = Button(root, text=' ', width=6, height=3,
                         font=('Arial', 20, 'bold'),
                         background='skyblue',
                         command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col)
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
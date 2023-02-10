# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

#[[Спартак,games,wins.nichya.loses,score]]


score_table = []


def AddResult(result):
    for i in result[0],result[2]:
        isnew = True
        for j in score_table:      
            if i in j:
                isnew = False
        if  isnew == True:
            score_table.append([i,0,0,0,0,0])  #Добавление новой команды
    for i in score_table:
        if i[0] == result[0]:
            i[1] +=1
            if result[1] > result[3]:
                i[2] +=1
                i[5] +=3
            elif result[1] == result[3]:
                i[3] +=1
                i[5] +=1
            else:
                i[4] +=1
        if i[0] == result[2]:
            i[1] +=1
            if result[1] < result[3]:
                i[2] +=1
                i[5] +=3
            elif result[1] == result[3]:
                i[3] +=1
                i[5] +=1
            else:
                i[4] +=1
    return

def PrintScores():
    for i in score_table:
        print(f"{i[0]}: {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")


games = int(input('Введите количество игр : '))
for i in range(games):
    result = input(f'Введите результат {i} игры :')
    result = result.split(";")
    AddResult(result)
PrintScores()
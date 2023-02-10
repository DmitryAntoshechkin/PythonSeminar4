# задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование


def Rle_decode(code):
    decode = []
    count = 0
    for i in code:
        if i.isdigit():
            count = count * 10 + int(i)
        else:
            if count == 0:
                count +=1
            for j in range(count):
                decode.append(i)
            count = 0
    decode = ''.join(decode)
    return (decode)

def Rle_code(text):
    code = []
    count = 1
    symbol = text[0]
    for i in range(1,len(text)):
        if text[i] == symbol:
            count +=1
        else:
            if count == 1:
                code.append(symbol)
            else:
                code.append(str(count)+symbol)
            count = 1
            symbol = text[i]
        if i == len(text)-1:
            if count == 1:
                code.append(symbol)
            else:
                code.append(str(count)+symbol)              
    code = ''.join(code)
    return(code)

text = list(input('Введите текстовую строку: '))
code = Rle_code(text)
print("Кодированный текст: "+code)
decode = Rle_decode(code)
print("Декодированный текст: "+decode)
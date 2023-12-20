# *********************************************************************************************************************
# Шифр Цезаря
# Код для шифровки/дешифровки шифра Цезаря
# На вход: язык, вариант что сделать, текст, шаг
# Логаритм шифровки:
# индекс символа в списке + шаг, если число выходит за границу, то модуль разницы длины списка и суммы индекса символа в списке и шага
# Логаритм дешифровки:
# Индекс символа - шаг, если индекс выходит за границы списка: разница длины списка и модуль разницы индекса символа в списке и шага
# Если при дешифровке неизвестен шаг шифровки, то он не указывается и выводятся все варианты дешифровки
# Есть валидаторы для проверки правильности ввода
# └Правильность ввода языка (en/ru)
# └Правильность выбора варианты (Шифровка/дешифровка)
# └Правильность ввода текста (Состоит ли текст только из ru/en букв
# └Правильность на ввод шага (Вводится буква, пустая строка или цифра)
# *********************************************************************************************************************


# Генератор прописных русских букв
def is_ru_up():
    return [chr(i) for i in range(1040, 1072)]


# Генератор строчных русских букв
def is_ru_low():
    return [chr(i) for i in range(1072, 1104)]


# Генератор прописных английских букв
def is_en_up():
    return [chr(i) for i in range(65, 91)]


# Генератор строчных английских букв
def is_en_low():
    return [chr(i) for i in range(97, 123)]


# Воллидатор ввода языка
def is_valid_lang(lang):
    if lang in 'ru, en':
        return lang
    return is_valid_lang(input('Не тот язык, введите язык еще раз (en/ru\n<<'))


# Валидатор выбора шифрока/дешифровка
def is_valid_decode_code(choise):
    if choise in '1, 2':
        return choise
    return is_valid_decode_code('Что-то пошло не так, выберите вариант снова:\n1)Зашифровать\nДешифровать\n<< ')


# Валидатор ввода цифры
def is_valid_digit(num, cd):
    if num.isdigit():
        return int(num)
    elif num == '' and cd != '1':
        return ''
    return is_valid_digit(input('Введите сдвиг еще раз\n<< '), cd)


# Валидатор ввода текста
def is_valid_text(text, lang):
    if lang == 'en':
        list_text = list(text)
        for i in list_text:
            if i in is_ru_up() or i in is_ru_low():
                return is_valid_text(input('Вы ввели текст с русскими буквами\nПовторите попытку ввода\n<< '), lang)
        return text
    elif lang == 'ru':
        list_text = list(text)
        for i in list_text:
            if i in is_en_up() or i in is_en_low():
                return is_valid_text(input('Вы ввели текст с английскими буквами\nПовторите попытку ввода\n<< '), lang)
        return text


# Шифровка русского прописного символа
def is_code_ru_up(n, shift):
    if is_ru_up().index(n) + shift > len(is_ru_up()):
        return is_ru_up()[abs(len(is_ru_up()) - (is_ru_up().index(n) + shift))]
    return is_ru_up()[is_ru_up().index(n) + shift]


# Шифровка русского строчного символа
def is_code_ru_low(n, shift):
    if is_ru_low().index(n) + shift > len(is_ru_low()):
        return is_ru_low()[abs(len(is_ru_low()) - (is_ru_low().index(n) + shift))]
    return is_ru_low()[is_ru_low().index(n) + shift]


# Шифровка русского прописного символа
def is_code_en_up(n, shift):
    if is_en_up().index(n) + shift > len(is_en_up()):
        return is_en_up()[abs(len(is_en_up()) - (is_en_up().index(n) + shift))]
    return is_en_up()[is_en_up().index(n) + shift]


# Шифровка русского строчного символа
def is_code_en_low(n, shift):
    if is_en_low().index(n) + shift > len(is_en_low()):
        return is_en_low()[abs(len(is_en_low()) - (is_en_low().index(n) + shift))]
    return is_en_low()[is_en_low().index(n) + shift]


# Шифрование текста
def is_coding(lang, shift, text):
    text_list = list(text)
    if lang == 'ru':
        for i in range(len(text_list)):
            if text_list[i] in is_ru_up():
                text_list[i] = is_code_ru_up(text_list[i], shift)
            elif text_list[i] in is_ru_low():
                text_list[i] = is_code_ru_low(text_list[i], shift)
        return ''.join(text_list)
    elif lang == 'en':
        for i in range(len(text_list)):
            for i in range(len(text_list)):
                if text_list[i] in is_en_up():
                    text_list[i] = is_code_en_up(text_list[i], shift)
                elif text_list[i] in is_en_low():
                    text_list[i] = is_code_en_low(text_list[i], shift)
            return ''.join(text_list)


# Дешифровка русского прописного символа
def is_decode_ru_up(n, shift):
    if is_ru_up().index(n) - shift < 0:
        return is_ru_up()[len(is_ru_up())-abs(is_ru_up().index(n)-shift)]
    return is_ru_up()[is_ru_up().index(n) - shift]



# Дешифровка русского строчного символа
def is_decode_ru_low(n, shift):
    if is_ru_low().index(n) - shift < 0:
        return is_ru_low()[len(is_ru_low())-abs(is_ru_low().index(n)-shift)]
    return is_ru_low()[is_ru_low().index(n) - shift]

# Дешифровка русского прописного символа
def is_decode_en_up(n, shift):
    if is_en_up().index(n) - shift < 0:
        return is_en_up()[len(is_en_up())-abs(is_en_up().index(n)-shift)]
    return is_en_up()[is_en_up().index(n) - shift]


# Дешифровка русского строчного символа
def is_decode_en_low(n, shift):
    if is_en_low().index(n) - shift < 0:
        return is_en_low()[len(is_en_low())-abs(is_en_low().index(n)-shift)]
    return is_en_low()[is_en_low().index(n) - shift]


# Дешифровка текста
def is_decoding(lang, shift, text):
    text_list = list(text)
    if lang == 'ru':
        for i in range(len(text_list)):
            if text_list[i] in is_ru_up():
                text_list[i] = is_decode_ru_up(text_list[i], shift)
            elif text_list[i] in is_ru_low():
                text_list[i] = is_decode_ru_low(text_list[i], shift)
        return ''.join(text_list)
    if lang == 'en':
        for i in range(len(text_list)):
            if text_list[i] in is_en_up():
                text_list[i] = is_decode_en_up(text_list[i], shift)
            elif text_list[i] in is_en_low():
                text_list[i] = is_decode_en_low(text_list[i], shift)
        return ''.join(text_list)

language = is_valid_lang(input('Выберите язык для кодирования/декодирования (en/ru)\n<< '))
code_decode = is_valid_decode_code(input('Выберите что нужно сделать (укажите цифру)\n1) Зашифровать\n2) Дешифровать\n<< '))
text = is_valid_text(input('Введите текст\n<< '), language)
shift = is_valid_digit(input('Введите сдвиг\n<< '), code_decode)
if code_decode == '1':
    print(is_coding(language, shift, text))
elif code_decode == '2':
    if shift == '':
        if language == 'ru':
            for i in range(1, 33):
                print(is_decoding(language, i, text))
        elif language == 'en':
            for i in range(1, 26):
                print(is_decoding(language, i, text))
    else:
        print(is_decoding(language, shift, text))

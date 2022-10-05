# наивный алгоритм: пробежаться циклом for по каждому символу в строке
# (все в нижнем регистре), ретернуть символ if индекс 1 вхождения==последнего
# for symb in string:
#   if string.lower().find(symb.lower()) == string.lower().rfind(symb.lower()):
#       return symb
# return ''

def first_non_repeating_letter(string: str) -> str:
    """Function which takes a string as input and returns the first symbol
    that is not repeated anywhere in the string.
    :param string: original string
    :type string: str
    :rtype: str
    :return: first nonrepeated symbol
    """
    # через listcomprehension сгенерировать список всех символов входящих 1 раз
    # и вернуть 1 элемент или пустую строку:
    return ([symb for symb in string
            if string.lower().count(symb.lower()) == 1] or [''])[0]


if __name__ == '__main__':
    # сначала обернем все в тесты, для удобства проверки
    assert first_non_repeating_letter('a') == 'a'  # a
    assert first_non_repeating_letter('stress') == 't'  # t
    assert first_non_repeating_letter('moonmen') == 'e'  # e
    assert first_non_repeating_letter('') == ''  # (пустая строка)
    assert first_non_repeating_letter('abba') == ''  # (пустая строка)
    assert first_non_repeating_letter('hello world, eh?') == 'w'  # w
    assert first_non_repeating_letter('sTreSS') == 'T'  # T
    assert first_non_repeating_letter(
        'Go hang a salami, I\'m a lasagna hog!') == ','  # ,

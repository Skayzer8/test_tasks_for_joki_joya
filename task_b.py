def make_looper(string: str):
    """Function take argument a string (non-zero length) and return function.
    The returned function return consecutive symbols of the string.
    :param string: original string (non-zero length)
    :type string: str
    :rtype: str
    :return: next symbol
    """
    # cбрасываем флаг в -1 позицию, чтобы флаг не сбился на 1 итерации
    flag = -1

    def looper_generator():
        # заведем флаг состояния в глобальной области, для хранения индекса
        nonlocal flag
        flag += 1
        # обнуляем флаг состояния если дошли до конца строки
        if flag == len(string):
            flag = 0
        return string[flag]

    return looper_generator


if __name__ == '__main__':
    abc = make_looper('abc')
    # сначала обернем ожидаемые результаты в assert
    assert abc() == 'a'  # возвращает 'a'
    assert abc() == 'b'  # возвращает 'b'
    assert abc() == 'c'  # возвращает 'c'
    assert abc() == 'a'  # снова возвращает 'a'

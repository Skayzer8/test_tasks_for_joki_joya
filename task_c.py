# решение в лоб: посимвольно сравнить s сначала с part1, затем с part2,
#  совпадающие символы отбрасывать на каждом шагу.
def is_merge(string: str, part1: str, part2: str) -> bool:
    """Function checks if the given string can be formed from
    two other strings(part 1+part 2).
    :param string: original string
    :type string: str
    :rtype: bool
    :return: true or false verdict
    """
    #  опишем базовый случай рекурсии, в нашем случае это пустые строки
    if not (string and part1 and part2):
        return (string == part1 + part2)
    else:
        # если первые символы ==, отбрасываем и рекурсивно вызываем функцию,
        # если в 1 условии получаем False, уходим искать нужный символ в part2
        return (
            string[0] == part1[0] and is_merge(string[1:], part1[1:], part2) or
            string[0] == part2[0] and is_merge(string[1:], part1, part2[1:])
        )


if __name__ == '__main__':
    # готовим тесты
    assert is_merge('helloworld', 'hello', 'world') is True  # True
    assert is_merge('helloworld', 'how', 'ellorld') is True  # True
    assert is_merge('helloworld', 'hell', 'world') is False  # False
    assert is_merge('helloworld', 'ehll', 'world') is False  # False

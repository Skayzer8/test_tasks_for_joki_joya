# напомнило задачку о рюкзаке
# решение "в лоб": воспользоваться рекурсией,
# каждый раз уменьшая доступный номинал монет
from typing import List


def count_change(money: int, nominals: List[int]) -> int:
    """Function which counts available ways change a given amount of money,
    used only given nominals.
    :param money: amount of money
    :type money: int
    :rtype: int
    :return: available ways change money
    """
    # описываем базовые случаи рекурсии:
    # если получили сумму < 0 или монеток считаем, что способа размена нет
    if money < 0 or not nominals:
        return 0
    # если получили сумму = 0, считаем +1 возможный способ размена
    if money == 0:
        return 1
    # если осталась монетка одним номиналом проверям можно ли разменять сумму:
    if len(nominals) == 1:
        return money % nominals[0] == 0
    # запускаем рекурсию убирая, проверенный номинал
    return (count_change(money - nominals[0], nominals)
            + count_change(money, nominals[1:]))


if __name__ == '__main__':
    # готовим тесты
    assert count_change(4, [1, 2]) == 3  # 3 (1+1+1+1, 1+1+2, 2+2)
    assert count_change(10, [5, 2, 3]) == 4  # 4 (5+5, 5+2+3, 2+3+2+3, 3+3+2+2)
    assert count_change(11, [5, 7]) == 0  # 0

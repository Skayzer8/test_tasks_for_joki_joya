def first_non_repeating_letter(string: str) -> str:
    """Function which takes a string as input and returns the first symbol
    that is not repeated anywhere in the string.
    :param string: original string  
    :type data: str
    :rtype: strы
    :return: first nonrepeated symbol 
    """ 
    for symb in string:
        if string.lower().find(symb.lower()) == string.lower().rfind(symb.lower()):
            return symb
    return ''


if __name__ == '__main__':
    # сначала обернем все в тесты, для удобства проверки
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'
    assert first_non_repeating_letter('') == ''
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('hello world, eh?') == 'w'
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter(
        'Go hang a salami, I\'m a lasagna hog!') == ','

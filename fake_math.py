def divide(first, second):
    res = 1
    if isinstance(first, (int, float)) and isinstance(second, (int, float)):
        if second == 0:
            res = 'ошибка'
        else:
            res = first / second
    return res
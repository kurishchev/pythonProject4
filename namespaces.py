def test_function():
    def inner_function():
        print('Я')

    print('inner_function внутри функции test_function, ау?')
    inner_function()
test_function()
# print('inner_function вне функции test_function, ау?')   # -отсюда не вызывается
# inner_function()

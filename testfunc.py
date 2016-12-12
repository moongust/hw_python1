

def test(text,got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Тест: {1} | Получено: {2} | Ожидалось: {3}".format(prefix, text, repr(got), repr(expected)))
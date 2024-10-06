calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False


print(string_info('Шокированный'))
print(string_info('пАДАЮЩИЙ'))
print(string_info('Абракадабра'))
print(string_info('бАРАБУШКА'))
print(is_contains('кружок', ['Кружище', 'Кружево']))
print(is_contains('еГОТ', ['Его', 'ГОТ', 'ЕГот']))
print(is_contains('ПРИВЕТ', ['приВЕТО', 'приВЕТ']))
print(is_contains('зДРАСТЕ', ['зДРАВИя', 'зДРАВО', 'зДОРОВвье']))
print(calls)

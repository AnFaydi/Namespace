calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(str):
    count_calls()
    tuple_ = tuple()
    tuple_ = (len(str), str.upper(), str.lower())
    return tuple_
def is_contains(str, list_):
    count_calls()
    str = str.upper()
    for i in range(0,len(list_)):
        list_[i] = list_[i].upper()
    if str in list_:
        return True
    else:
        return False

print(string_info('Коллаж'))
print(string_info('Осьминог'))
print(string_info('Дом'))
print(is_contains('Дом',['дОм','Дома', 'Дима']))
print(is_contains('Энциклопедия',['Медицина','энциклапидия', 'энци', 'клоп']))
print(calls)
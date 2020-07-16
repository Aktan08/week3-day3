# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Foo”
# b) Если значение делиться на 5, то записываем строку “Bar”
# Пример:
# {'a': 5, 'b': 3, 'c': 8, 'd': 14} до
# {'a': 'Foo', 'b': 'Bar'} после
# Требование:
# Использовать dict comprehension

# my_dict = {'a': 6, 'b': 3, 'c': 10, 'd': 14}
# my_dict2 = {key :'foo'if value%3==0 else  'bar' if value%5==0 else "none" for key , value  in my_dict.items()}
# print(my_dict2)

my_dict = {'a': 6, 'b': 3, 'c': 10, 'd': 14}
my_dict2 = {key:'Foo'if value%3==0 else  'Bar' if value%5==0 else "none"  for key,value in my_dict.items()if value%3==0 or value%5==0}
print(my_dict2)

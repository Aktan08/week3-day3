# Написать генератор списка, который итерируется по функции range от 1 до 100
# и фильтрует по четным числам.
my_list = range(1,101)
my_list2 = [ num for num in my_list if num % 2 ==0]
print(my_list2)


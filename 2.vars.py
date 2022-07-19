# Типы данных
my_int = 1000

# числа с плавающей точкой (вещественные) (float)
my_float = 3.14

# строковые данные (текстовые строки, слова, символы) (str, string)
my_str_1 = 'pizdayton'
my_str_2 = "arbayton"
my_char_1 = 'X'
my_char_2 = 'Y'
my_char_3 = 'Й'
my_text = '''
осенью
птицы
летят
на
'''
three = 300
# print(my_text)


# Способы форматирования строк
# 1. Конкатенация строк
# result = my_char_3 + my_char_2 + my_char_1 + ' ' + str(three)
# print(result)

# 2. F-строка
# result = f'{my_str_1}{three}{ my_str_2}'
# result = f'Число 1: {three}'

num_1 = 100
num_2 = 16.66123232434534

# result = f'Число 1: {num_1}, Число 2: {num_2:.2f}%'

a = 10
b = 3

# обычное деление 

# res = a / b

# целочисленное деление
# res = a // b

# деление по остатку
b = 4
res = a % b

print(res)
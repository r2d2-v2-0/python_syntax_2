x = 3
y = 2

# операции равенства
# res = x == y

# операция неравенства
res = x != y

# операция сравнения 1
res = x < y

# операция сравнения 2
res = x > y

# логические операции

var_1 = True
var_2 = False

# оператор "НЕ" (NOT, инверсия)
res = not var_1 

# оператор "И" (AND, конъюкция)
res = var_1 and var_2

# оператор "ИЛИ" (OR, дезъюкция)
res = var_1 or var_2

# условные операции

a = -5
res = None

# оператор if (если)
a = 0
condition = a > 5

a = 2
b = 3

# if (a == 2) and not (b < 3):
#     res = "Hello!"

# оператор else (иначе)
a = 100

# if a < 50:
#     res = "меньше 50"
# else:
#     res = "больше либо равно 50"

# оператор elif 
a = 0

# if a > 0:
#     res = "больше нуля"
# elif a < 0:
#     res = "меньше нуля"
# else:
#     res = "равно нулю"

char = 'c'

if char == 'a':
    res = "буква a"
elif char == 'b':
    res = "буква b"
elif char == 'c':
    res = "буква c"
else:
    res = "другой символ"


print(res)
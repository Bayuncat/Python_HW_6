# БЫЛО

# import math

# x = int(input("Введите целое число для вывода списка факториалов: "))
# y = []
# for i in range(1,x+1): y.append(math.factorial(i))
# print(y)



# СТАЛО
import math

x = int(input("Введите целое число для вывода списка факториалов: "))
res = list(map(lambda x: math.factorial(x), [i for i in range(1,x+1)]))
print(res)
#----------------------------------------------------------
# Задача 1: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)



# num = int(input("Введите число: "))
# sum = 0

# while num > 0:
#     sum += num % 10
#     num //= 10
# print(f"Сумма трёхзначного числа равна: {sum}")




#----------------------------------------------------------
# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10



# s = int(input("Введите количество журавликов: "))
# kate = s // 6 * 4
# petr = s // 6
# sergey = petr
# print(f"Катя сделала {kate} журавлей\nПетя сделал {petr} журавлей\nСерёжа сделал {sergey} журавлей")



#----------------------------------------------------------
# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр 
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no



# num = int(input("Введите номер билета и узнайте счастливый ли он: "))
# first_hulf_sum = 0
# second_hulf_sum = 0

# while num > 0:
#     if num > 999:
#         first_hulf_sum = first_hulf_sum + num % 10 
#     if num < 1000:
#         second_hulf_sum = second_hulf_sum + num % 10
#     num = num // 10
    
# if second_hulf_sum == first_hulf_sum:
#     print("Да")
# else:
#     print("Нет")
    
    
    
#----------------------------------------------------------
# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


# n = int(input("Введите число n:")) 
# m = int(input("Введите число m:")) 
# k = int(input("Введите число k:")) 
# if k % n == 0 or k % m == 0:
#     print("yes")
# else:
#     print("no")


#----------------------------------------------------------
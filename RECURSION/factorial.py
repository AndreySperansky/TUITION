def factorial(n):
  if n == 0 or n==1:
      return 1
  else:
      return n * factorial(n-1)

num = abs(int(input("Введите целое число: ")))
print("Факториал числа %d равен: " % num, factorial(num))


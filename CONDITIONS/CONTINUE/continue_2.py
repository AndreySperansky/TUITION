"""СONTINUE  служит для пропуска итерации в которой оно возникло"""

"""Вариант 1"""
for letter in "Python":
    if letter == "h":
        continue                            # Тупо пропускает один цикл выполнения кода
    print ("Carrent letter:  ", letter)

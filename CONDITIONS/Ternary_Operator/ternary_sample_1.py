"""Common Pattern for ternary operator"""
"""condition_if_true if condition else condition_if_false"""

is_checked = True
mode = "checked" if is_checked else "not checked"
print(mode + '\n')

"""Другой вариант с кортежами
(if_check_is_false, if_check_is_true)[param_to_check]"""

checked = True
personality = ("проверено", "не проверено")[checked]
print(personality + '\n')

""" Существует более лаконичная версия данного оператора """

print(True or "Some")
print(False or "Some")

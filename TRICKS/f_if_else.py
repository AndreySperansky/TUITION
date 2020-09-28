"""
8. Назначение переменных и функций по условию

A = Y if X else Z
"""


def product(a, b):
    return a * b

def summarize(a, b):
    return a + b

c = True

print((product if c else summarize)(3, 4))
# 12

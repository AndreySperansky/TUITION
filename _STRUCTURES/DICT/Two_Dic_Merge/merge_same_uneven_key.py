foo = [
    {'a': 'x', 'b': 'y', 'c': 'z'},
    {'a': 'j', 'c': 'z'}
]

dic = {
    k: [d.get(k) for d in foo]
    for k in set().union(*foo)
}

print(dic)
# {'b': ['y', None], 'c': ['z', 'z'], 'a': ['x', 'j']}


# Вариант2
import operator
from functools import reduce

all_keys = reduce(operator.or_, (d.keys() for d in foo))
print(all_keys)
# {'a', 'b', 'c'}

adic = {key: [d.get(key) for d in foo] for key in all_keys}
print(adic)
# {'a': ['x', 'j'], 'b': ['y', None], 'c': ['z', 'z']}
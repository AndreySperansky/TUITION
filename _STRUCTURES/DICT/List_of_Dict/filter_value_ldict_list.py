# Отфильтровать словари по нескольким значениям
lst = [{'A':'BBB', 'C':'DDD', 'D':'EEE'},
       {'A':'BBB', 'C':'DDD', 'D':'ESS'},
       {'A':'BBB', 'C':'ASD', 'D':'EEE'},
       {'C':'ASD', 'D':'EEE'}]

# list of filters
flt = [('A', 'BBB'), ('D', 'EEE')]

# a list comprehension + all() will do the trick
res = [x for x in lst if all(x.get(k, None) == v for k, v in flt)]

print(res)
#[{'A': 'BBB', 'C': 'DDD', 'D': 'EEE'}, {'A': 'BBB', 'C': 'ASD', 'D': 'EEE'}]
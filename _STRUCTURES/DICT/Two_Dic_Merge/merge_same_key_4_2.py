data = [ {"A": "value1", "B": "value2", "C": "value3"},
         {"A": "value4", "B": "value5", "C": "value3"},
         {"A": "value1", "B": "value8", "C": "value3"} ]


from collections import defaultdict

temp_dict = defaultdict(set)
for item in data:
   for key, value in item.items():
       temp_dict[key].add(value)
# print(temp_dict)

my_dict = {}
for key, value in temp_dict.items():
    my_dict[key] = ", ".join(value)
print(my_dict)

# {'A': 'value1, value4', 'B': 'value5, value8, value2', 'C': 'value3'}
# Trick - использовать dict.setdefault, чтобы начать список и добавить к нему:

input = [{1: 2}, {2: 2}, {1: 3}, {2: 1}, {1: 3}]
output = {}
for d in input:
    for k,v in d.items():
        output.setdefault(k, []).append(v)

print(output)
# output contains {1: [2, 3, 3], 2: [2, 1]}

output=[{k:v} for k,v in output.items()]

print(output)
# output contains [{1: [2, 3, 3]}, {2: [2, 1]}]
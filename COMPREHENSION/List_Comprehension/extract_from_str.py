

s = "gsjglk235235erewrt23452345wetw3535wertGJH"

b = [int(i) for i in s if i.isdigit()]
print(b)

# [2, 3, 5, 2, 3, 5, 2, 3, 4, 5, 2, 3, 4, 5, 3, 5, 3, 5]


a = [i for i in s if i.isalpha()]
print(a)
# ['g', 's', 'j', 'g', 'l', 'k', 'e', 'r', 'e', 'w', 'r', 't', 'w', 'e', 't', 'w', 'w', 'e', 'r', 't', 'G', 'J', 'H']
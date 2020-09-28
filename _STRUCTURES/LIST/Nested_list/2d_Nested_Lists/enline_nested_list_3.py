"""" Распаковка с помощью генераторов """""

data = [[1, 2, 3], [4, 5, 6]]
nova = [y for x in data for y in x]
print(nova)

# [1, 2, 3, 4, 5, 6]
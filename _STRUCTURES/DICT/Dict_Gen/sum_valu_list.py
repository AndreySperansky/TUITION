d = {'alfa': [3, 7, 2],
	 "betta": [22, -16],
	 "gamma": [10, 20],
	 'delta': [0, 10.0, 15.0, -3.0],
	  }

print(sum(d.values(), []))
# [3, 7, 2, 22, -16, 10, 20, 0, 10.0, 15.0, -3.0]

print(sum(sum(d.values(), [])))
# 70.0

d = {
    1: [1,2,3],
    2: [2,5,6]
}

values_sum = [sum(values_list) for values_list in d.values()]
print(values_sum)
# [6, 13]

values_sum_ = sum([sum(values_list) for values_list in d.values()])
print(values_sum_)
# 19

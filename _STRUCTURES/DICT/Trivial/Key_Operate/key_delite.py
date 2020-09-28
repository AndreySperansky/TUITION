prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):  # Use a list instead of a view
	if key == 'orange':
		del prices[key]  # Delete a key from prices

print(prices)
#{'apple': 0.4, 'banana': 0.25}


"""если вы попытаетесь удалить ключ из prices, используя напрямую .keys(), тогда Python вызовет RuntimeError, 
сообщающую, что размер словаря изменился во время итерации:"""

# Python 3. dict.keys() returns a view object, not a list

# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key in prices.keys():
# 	if key == 'orange':
# 		del prices[key]


"""Traceback (most recent call last):
	File "<input>", line 1, in <module>
		for key in prices.keys():
RuntimeError: dictionary changed size during iteration"""
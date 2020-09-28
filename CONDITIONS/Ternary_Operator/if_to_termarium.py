# слово -> СлОвО

word = 'слово'

result = []

for i in range(len(word)):
	# if i % 2 != 0:
	# 	letter = word[i].lower()
	# else:
	# 	letter = word[i].upper()

# тернарный вариант
	letter = word[i]
	letter = letter.lower() if i % 2 != 0 else letter.upper()

	result.append(letter)
result = ''.join(result)
print(result)


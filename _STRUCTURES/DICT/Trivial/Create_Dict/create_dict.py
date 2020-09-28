person = {}

s = 'IVANOV IVAN Samara SGU 5 4 5 5 4 3 5'

s = s.split()
person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
	person['marks'].append(int(i))
print(s, '\n')
# ['IVANOV', 'IVAN', 'Samara', 'SGU', '5', '4', '5', '5', '4', '3', '5']

print(person)

# {'lastName': 'IVANOV', 'firstName': 'IVAN', 'city': 'Samara', 'university': 'SGU', 'marks': [5, 4, 5, 5, 4, 3, 5]}

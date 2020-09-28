# Загадать случайное число
import random

number = random.randint(1, 100)
print(number)


user_number = None

count = 0

# Определяем уровень сложности:
levels = {1: 10, 2: 5, 3: 3}
level = int(input("Введите уровень сложности 1-2-3: \n"))
max_count = levels[level]

# Объявляем количесво игроков:

user_count = int(input("Введите количество игроков: \n"))
users = []
for name in range(user_count):
	user_name = input(f"Введите имя игрока {name}: ")
	users.append(user_name)

print(users)

is_winner = False
winner_name = None

# while number != user_number:
while not is_winner:

	count += 1
	if count > max_count:
		print("Лимит попыток исчерпан, Все пользователи проиграли :-( !")
		break

	print(f"Попытка № {count} из {max_count}")

	for user in users:
		print(f"Ход игрока {user}")
		# Шаг 2: Предложить пользователю ввести число
		user_number = int(input('Введите число: \n'))
		if user_number == number:
			is_winner = True
			winner_name = user
			break
		# Шаг 3: Срвнение чисел, вывод результата
		elif number < user_number:
			print("Ваше число больше загаданного \n")
		else:
			print("Ваше число меньше загаданного \n")

else:
	print(f"Победитель {winner_name}!!!")

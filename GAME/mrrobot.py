import sys
import os
import shutil
import psutil

def duplicate_file(filename):
	if os.path.isfile(filename):
		newfile = filename + '.dupl'
		shutil.copy(filename, newfile)  # копируй
		if os.path.exists(newfile):
			print("файл", newfile, " был успешно создан")
			return True
		else:
			print("Возникли проблемы при копировании")
			return False

def sys_info():
	print("Вот что я знаю о системе: \n")
	print("Текущая дериктория: ", os.getcwd())
	print("Платформа (ОС): ", sys.platform)
	print("Кодировка файловой системы : ", sys.getfilesystemencoding())
	print("Текущий пользователь системы: ", os.getlogin())
	print("Количество CPU: ", str(os.cpu_count()))
	print("Количество CPU: ", psutil.cpu_count())
	print("Текущий пользователь: ", os.getlogin())


def del_duplicates(dirname):
	file_list = os.listdir(dirname)
	doubl_count = 0

	for f in file_list:
		fullname = os.path.join(dirname, f)
		if fullname.endswith('.dupl'):
			os.remove(fullname)
			if not os.path.exists(fullname):
				doubl_count += 1
				print("файл", fullname, " был успешно удален")
	return doubl_count


answer = ''
while answer != 'q':
	answer = input("Давайте поработаем? (y/n/q) \n")

	if answer == 'y':
		print("Отлично, ")
		print("Я умею:")
		print(" [1] - выведу список файлов")
		print(" [2] - выведу информацию о системе")
		print(" [3] - выведу список процессов")
		print(" [4] - продублирую файлы в дериктории")
		print(" [5] - продублирую указанный файл")
		print(" [6] - продублирую файлы в дериктории")
		do = int(input("Укажите номер действия: \n"))

		if do == 1:
			print(os.listdir())
		elif do == 2:
			sys_info()


		elif do == 3:
			print(psutil.pids())

		elif do == 4:
			print("=Дублирование файлов в текущей директории= \n")
			dirname = input("Укажите имя директории : \n для текущей введите знак '.' \n")
			file_list = os.listdir(dirname)
			i = 0
			while i < len(file_list):
				duplicate_file(file_list[i])
				i += 1
		elif do == 5:
			print("Дублирвание указанного файла : \n")
			filename = input("Укажите имя файла: \n")
			duplicate_file(filename)


		elif do == 6:
			print("Удаление дубликатов в директориии \n")
			dirname = input("Укажите имя директории : \n")
			count = del_duplicates(dirname)
			print("--Удалено файлов: ", count)


		else:
			pass

	elif answer == 'n':
		print("До свидания!")
	else:
		print("Неизвестный ответ")
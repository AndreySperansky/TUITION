def is_date_valid(date_as_string):
	day, month, year = map(int, date_as_string.split('-'))
	try:
		assert 0 <= day <= 31
		assert 0 <= month <= 12
		assert 0 <= year <= 3999
	except AssertionError:
		return False
	return True
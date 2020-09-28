class Counter:
	def __init__(self, low, high, step):
		self.current = low
		self.high = high
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.high:
			raise StopIteration
		else:
			result = self.current
			self.current += self.step
			return result

for c in Counter(3, 9, 2):
	print(c, end = ' ' )
# 3 5 7 9
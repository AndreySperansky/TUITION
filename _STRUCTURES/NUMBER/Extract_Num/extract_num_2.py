any_text = "hello3 bu 34 5kdf45"

#print(" ".join(filter(lambda s: s.isnumeric(),input().split())))
print(" ".join(filter(lambda s: s.isnumeric(), any_text.split())))
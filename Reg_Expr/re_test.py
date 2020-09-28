import re

string = "This is a simple test message for test"
found = re.findall(r'test', string)
print(found)
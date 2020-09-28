table = {'Python': 'Guido van Rossum',
        'Perl': 'Larry Wall',
        'Tcl': 'John Ousterhout' }

language = 'Python'                         # key
creator = table[language]                   # value
print(creator)

for anyword in table:                      # То же, что и: for lang in table.keys()
        print(anyword, '\t', table[anyword])

# Guido van Rossum
# Python 	 Guido van Rossum
# Perl 	 Larry Wall
# Tcl 	 John Ousterhout
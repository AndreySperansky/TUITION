dict_filter_test = {'one_key': {'one_value': ['r_one',
                                 'r_two',
                                 'r_three',
                                 'r_four',
                                 'r_five',
                                 'r_six']},
					'two_key': {'two_value': ['r_one',
                                 'r_two',
                                 'r_three',
                                 'r_four',
                                 'r_five',
                                 'r_six']}}

filt = ['six', 'two']  # you don't need a set here
for v in dict_filter_test.values():
    for v2 in v.values():
        v2[:] = [x for x in v2 if all(f not in x for f in filt)]

        print(v2)
# ['r_one', 'r_three', 'r_four', 'r_five']
# ['r_one', 'r_three', 'r_four', 'r_five']


dict_filter_test = { k:{k2:[x for x in v2 if all(f not in x for f in filt)]\
                        for k2,v2 in v.items()} for k,v in dict_filter_test.items()}

print(dict_filter_test)

# {'one_key': {'one_value': ['r_one', 'r_three', 'r_four', 'r_five']}, \
# 'two_key': {'two_value': ['r_one', 'r_three', 'r_four', 'r_five']}}
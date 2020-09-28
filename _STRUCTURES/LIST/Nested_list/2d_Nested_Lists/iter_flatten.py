def stringify(a):
    a = a[:]                           # Make copy of what was passed in.
    res = []                           # Initialize result list.
    my_stack = []                      # Initialize our own LIFO stack.
    while (a or my_stack):                            # While a or my_stack is non-empty
        if (a):
            elem = a.pop(0)
            if (not isinstance(elem, list)):          # If popped elem is not a list
                res.append(str(elem))                 # Append stringified elem to res
            else:
                my_stack.append((a, res))           # Push some stuff, to resume working upon later.
                a = elem                            # Let's start iterating on this inner list
                res = []                            # This inner list needs a clean res, to start with.
        else:                                       # my_stack is non-empty
            a, res_prev = my_stack.pop()   # Pop some stuff, to resume, work on outer list
            res_prev.append(res)           # First, append our just-completed inner list.
            res = res_prev
    return res
a = [[1, 2, 3], [4, 5, 6]]
#a = [1, [2, [3, 4], 5]]
print(stringify(a))
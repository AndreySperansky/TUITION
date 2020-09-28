"""!"""
"""Следующий фрагмент распечатывает прошедшее время выполнения кода в удобном для человека формате <HH:MM:SS>"""

import time
from datetime import timedelta

start_time = time.time()

#
# Perform lots of computations.
#

elapsed_time_secs = time.time() - start_time

msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))

print(msg)



# import timeit
#
# start = timeit.default_timer()
# #ALL THE PROGRAM STATEMETNS
# stop = timeit.default_timer()
# execution_time = stop - start
#
# print("Program Executed in "+execution_time) #It returns time in sec

"""Ipython "timeit" любой script:"""

# def foo():
#     %run bar.py
# timeit foo()
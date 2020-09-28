import threading
import time


def my_timer(print_interval):
    data = threading.local()
    data.counter = 1
    while data.counter <= 3:
        time.sleep(print_interval)
        print("I am alive %d times!" % data.counter)
        data.counter += 1

my_timer(2)


# import time
# import threading as th
#
# def target(form):
#     while True:
#         print(form) #нажмите кнопку тут
#         time.sleep(10)
#
# form = 1 #некая кнопка
# t = th.Thread(target=target, args=(form,), daemon=True)
# t.start()
#сохраните куда-то переменную t
#del t если вам надо убить поток


# import threading
# import time
#
#
# def my_timer(print_interval):
#     data = threading.local()
#     data.counter = 1
#     while True:
#         time.sleep(print_interval)
#         print("I am alive %d times!" % data.counter, threading.current_thread().name)
#         data.counter += 1
#
# t = threading.Thread(target=my_timer, name="My time thread", args=(5, ), daemon=True)
# t.start()
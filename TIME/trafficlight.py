import time

TrafficLightRunOrder = {"RED": 7, "YELLOW": 2, "GREEN": 7}
counter = 1
while counter <= 3:

	for k, w in TrafficLightRunOrder.items():
		print(f"{k}   \n следующий сигнал чере {w} сек.")
		time.sleep(w)

	counter += 1
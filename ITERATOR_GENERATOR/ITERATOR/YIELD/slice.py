def get_slice(packet):
    i = 0
    step = 4
    ln = len(packet)
    while i < ln:
        yield packet[i:i + step]
        i += step


for i in get_slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i)

# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10]
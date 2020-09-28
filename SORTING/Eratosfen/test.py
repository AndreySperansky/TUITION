import sys

l1 = [i for i in range(1)]
l2 = [i for i in range(17)]

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

# def gcd(m, n):
#     return (m / gcd(m, n)) * n

def gcd(m, n):
    while n!=0:
        m, n = n, m % n
        return m


print(gcd(5, 25))
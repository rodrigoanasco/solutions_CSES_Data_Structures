import time

temp = []
n = pow(10, 5)
start = time.time()
for i in range(1, n+1, +1):
    temp.append(i)
end = time.time()

print(end - start)


start = time.time()
for i in range(1, n+1, +1):
    temp.pop(0)
end = time.time()

print(end - start)

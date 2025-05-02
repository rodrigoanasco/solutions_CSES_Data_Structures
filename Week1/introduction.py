'''
Starting with the "count even" example
'''

def count_even(list):
    count = 0
    for element in list:
        if (element % 2) == 0:
            count = count + 1
    
    return count

print(count_even([1, 2, 3, 4, 4, 5, 6, 6, 7, 7]))
print(count_even([1, 1, 1, 1, 2]))
print(count_even([2, 2]))


'''
Measuring the efficiency of the algorithm
'''
import random
import time

#This function is meant to return max - min
def max_diff1(numbers):
    if numbers == []:
        return
    max_num = numbers[0];
    min_num = numbers[0];
    for element in numbers:
        if max_num < element:
            max_num = element
        elif min_num > element:
            min_num = element
    return max_num - min_num


#This function is meant to return max - min
def max_diff2(numbers):
    return max(numbers) - min(numbers)


n = 1000000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]
start_time = time.time()
result = max_diff1(numbers)
end_time = time.time()
print("result:", result)
print("time:", end_time - start_time, "s")

start_time = time.time()
result = max_diff2(numbers)
end_time = time.time()
print("result:", result)
print("time:", end_time - start_time, "s")
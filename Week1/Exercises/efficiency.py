import time
import random

# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

#implementation 2
#def count_even(numbers):
#    return sum(x % 2 == 0 for x in numbers)

def main():
    random.seed(100)
    list1 = [random.randint(1, 10000000) for _ in range(100000)]
    list2 = [random.randint(1, 10000000) for _ in range(1000000)]
    list3 = [random.randint(1, 10000000) for _ in range(10000000)]

    start = time.time()
    print(count_even(list1))
    end = time.time()
    print("Execition 1:", end - start)

    start = time.time()
    print(count_even(list2))
    end = time.time()
    print("Execition 2:", end - start)

    start = time.time()
    print(count_even(list3))
    end = time.time()
    print("Execition 3:", end - start)

    
if __name__ == "__main__":
    main()
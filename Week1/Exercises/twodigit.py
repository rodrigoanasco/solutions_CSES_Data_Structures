import time

def permutation_repetition(options, len, final, current, temp):
    
    if current >= len:
        final.append(temp)
        return

    #Base Case:
    temp = (temp * 10) + options[0]
    permutation_repetition(options, len, final, current + 1, temp)
    temp = int(temp / 10)
    
    temp = (temp * 10) + options[1]
    permutation_repetition(options, len, final, current + 1, temp)
    temp = int(temp / 10)

def count_permutation_repetition(num):
    return pow(2, num)

def not_equal(a, b):
    options = [2, 5]
    len_a = len(str(a))
    len_b = len(str(b))
    final_a = []
    final_b = []
    current = 0
    temp = 0

    permutation_repetition(options, len_a, final_a, current, temp)
    current = 0
    temp = 0
    permutation_repetition(options, len_b, final_b, current, temp)
    
    count = 0
    for j in range(len(final_a)):
        if final_a[j] >= a:
            count = count + 1

    for j in range(len(final_b)):
        if final_b[j] <= b:
            count = count + 1
    
    for i in range(len_a + 1, len_b):
        count = count + count_permutation_repetition(i)
    
    return count
    
def isEqual(a, b):
    count = 0
    final = []
    permutation_repetition([2, 5], len(str(a)), final, 0, 0)

    for i in range(len(final)):
        if final[i] >= a and final[i] <= b:
            count = count + 1
    
    return count
    

def count_numbers(a, b):
    # TODO
    count = 0
    if len(str(a)) != len(str(b)):
        count = not_equal(a, b)
    elif len(str(a)) == len(str(b)):
        count = isEqual(a, b)

    return count            


if __name__ == "__main__":
    start = time.time()

    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512

    end = time.time()

    print(end - start)
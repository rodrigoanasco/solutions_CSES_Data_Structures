def find_sums(numbers, size):
    # Edge case for faster return:
    if size == 1:
        return numbers
    
    # Next case:
    sum = []
    
    #First sum:
    n = 0
    k = size
    for i in range(size):
        n = n + numbers[i]
    sum.append(n)

    #Next sums
    for i in range(len(numbers)):
        
        if k == (len(numbers)):
            break
        sum.append(sum[i] - numbers[i] + numbers[k])
        k = k + 1


    return sum


if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]


    
    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000
    
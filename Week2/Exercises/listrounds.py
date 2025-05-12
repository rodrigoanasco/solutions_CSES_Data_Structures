import time

def find_rounds(numbers):
    # TODO
    final = []
    start = 1
    count = len(numbers)
    n = len(numbers)
    while(count > 0):
        temp = []
        for i in range(n):
            if numbers[i] == start:
                start = start + 1
                temp.append(numbers[i])
                count = count - 1
        final.append(temp)

    return final




if __name__ == "__main__":
    start = time.time()
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]

    end = time.time()

    print(end - start)
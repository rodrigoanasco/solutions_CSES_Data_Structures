def count_rounds(numbers):
    # Build a map from number to its position
    n = len(numbers)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[numbers[i]] = i

    rounds = 0
    current = 1

    while current <= n:
        rounds += 1
        # Proceed in this round as long as the next number comes later
        while current < n and pos[current + 1] > pos[current]:
            current += 1
        current += 1

    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000

def create_list(n):
    final = []
    for i in range(n):
        final.append(i + 1)
    return final

def find_order(n):
    # TODO
    #Edge case 1: When n is 1
    if n == 1:
        return [1]
    else:
        current = create_list(n)
        final = []
        i = 0
        while(True):
            if len(final) == n:
                break

            k = len(current)
            while i < k:
                if i % 2 == 0:
                    current.append(current[i])
                    i += 1
                else:
                    final.append(current[i])
                    i += 1
        
        return final
if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]

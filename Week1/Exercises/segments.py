def find_segments(data):
    list = []
    if (len(data) <= 0):
        return list
    
    str = data[0]
    count = 0
    temp = 0
    for i in range(len(data)):
        temp = temp + 1
        if (str == data[i]):
            count = count + 1
            
        else:
            list.append(tuple((count, (data)[i-1])))
            str = data[i]
            count = 1

        if(temp == len(data)):
            list.append(tuple((count, data[i])))
    return list

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
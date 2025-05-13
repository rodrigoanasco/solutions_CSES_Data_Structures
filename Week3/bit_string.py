'''
You are given a bit string consisting of the characters 0 and 1. 
How many ways can you select two positions in the bit string so 
that the left position contains the bit 0 and the right position 
contains the bit 1?
'''


def pair_maker(bits):
    if len(bits) < 1:
        return 0
    
    sum = 0
    count = 0
    temp = bits[0]

    for i in range(0, len(bits)):
        temp = bits[i]
        if temp == "0":
            sum += 1
        if temp == "1":
            count = count + sum

    return count

if __name__ == "__main__":
    #There should be 12 pairs in here
    bits = "01001011"
    print(pair_maker(bits))

    
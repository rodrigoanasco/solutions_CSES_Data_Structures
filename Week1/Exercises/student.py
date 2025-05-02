def check_number(number):
    if len(number) != 9:
        return False
    elif int(str(number)[0]) != 0:
        return False
    
    elif (100 - (int(str(number)[0]) * 3 + int(str(number)[1]) * 7 + int(str(number)[2]) * 1 
        + int(str(number)[3]) * 3 + int(str(number)[4]) * 7 + int(str(number)[5]) * 1 
        + int(str(number)[6]) * 3 + int(str(number)[7]) * 7)) % 10 != int(str(number)[8]):
        return False
    
    
    return True

    


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
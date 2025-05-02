def check_year(year):
    first = year % 100
    second = int(year / 100) % 100
    
    '''
    You can also do:
     left = int(str(year)[:2])
     right = int(str(year)[-2:])
    '''
    
    if (first + second) ** 2 == year:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False
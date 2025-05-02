def min_count(product_count, box_size):
    if (product_count % box_size) == 0:
        return product_count // box_size
    else:
        return product_count // box_size + 1
   

if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1
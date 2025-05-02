import time

def clear_reps(array_holder):
    final = []
    for i in range(0, len(array_holder), +1):
        temp = array_holder[i][1]
        isin = False
        for j in range(len(final)):
            if temp == final[j]:
                isin = True
                break
        if isin == False:
            final.append(array_holder[i][1])

    return final

def final_clear(array1, array2):
    final = []

    for i in range(len(array1)):
        final.append(array1[i])
    
    for j in range(len(array2)):
        isin = False
        for i in range(len(final)):
            if array2[j] == final[i]:
                isin = True
        
        if isin == False:
            final.append(array2[j])
    
    return final

def non_diagonal(grid, input):
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    array_holder = []

    #Left to right
    for i in range(num_rows):
        for j in range(num_cols):
            temp = ""
            index_holder_array = []
            rows = i
            cols = j
            while(cols < num_cols):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if temp == input:
                    array_holder.append((temp, index_holder_array))
                    break
                cols = cols + 1
    
    #Up and down
    for i in range(num_cols):
        for j in range(num_rows):
            temp = ""
            index_holder_array = []
            rows = j
            cols = i
            while(rows < num_rows):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if temp == input:
                    array_holder.append((temp, index_holder_array))
                    break
                rows = rows + 1

    #Left to right
    for i in range(num_rows):
        for j in range(num_cols - 1, -1, -1):
            temp = ""
            index_holder_array = []
            rows = i
            cols = j
            while(cols > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if temp == input:
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    break
                cols = cols - 1
            

    #Down to up
    for j in range(num_cols):
        for i in range(num_rows - 1, -1, -1):
            temp = ""
            index_holder_array = []
            rows = i
            cols = j
            while(rows > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if(temp == input):
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    break
                rows = rows - 1

    return clear_reps(array_holder)

def diagonals(grid, input):
    grid_rows = len(grid)
    grid_cols = len(grid[0])

    array_holder = []
    count = 0
    #Diagonal top left to down right rows
    for i in range(grid_rows):
        j = 0
        while(i < grid_rows and j < grid_cols):
            rows = i
            cols = j
            temp = ""
            index_holder_array = []
            while(rows < grid_rows and cols < grid_cols):  
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, index_holder_array))
                    count = count + 1
                    break
                rows = rows + 1
                cols = cols + 1
            i = i + 1
            j = j + 1
    
    #Diagonal reversed
    for j in range(grid_cols - 1, -1, -1):
        i = grid_rows - 1
        while(i > -1 and j > -1):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while(rows > -1 and cols > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    count = count + 1
                    break
                rows = rows - 1
                cols = cols - 1
            i = i - 1
            j = j - 1
        

    #Diagonal top left to down right col (ommiting shared diagonal which would be starting from index 0, 0)
    for j in range(0, grid_cols, +1):
        i = 0
        while(i < grid_rows and j < grid_cols):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while (rows < grid_rows and cols < grid_cols):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, index_holder_array))
                    count = count + 1
                    break
                rows = rows + 1
                cols = cols + 1
            i = i + 1
            j = j + 1

    #Diagonal reversed
    for i in range(grid_rows - 1, -1, -1):
        j = grid_cols - 1
        while(i > -1 and j > -1):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while(rows > -1 and cols > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    count = count + 1
                    break
                rows = rows - 1
                cols = cols - 1
            i = i - 1
            j = j - 1
        




    #Oposite as the other
    #Diagonal botton left to top right (without skipping)
    for i in range(grid_rows - 1, -1, -1):
        j = 0
        while (i > -1 and j < grid_cols):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while (rows > -1 and cols < grid_cols):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, index_holder_array))
                    count = count + 1
                    break
                rows = rows - 1
                cols = cols + 1
            i = i - 1
            j = j + 1
    
    #Diagonal Reversed
    for j in range(grid_cols - 1, -1, -1):
        i = 0
        while(i < grid_rows and j > -1):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while (rows < grid_rows and cols > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    count = count + 1
                    break
                rows = rows + 1
                cols = cols - 1
            i = i + 1
            j = j - 1


    #Diagonal botton left to top right (Skipping)
    for j in range(0, grid_cols, +1):
        i = grid_rows - 1
        while(i > -1 and j < grid_cols):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while (rows > -1 and cols < grid_cols):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, index_holder_array))
                    count = count + 1
                    break
                rows = rows - 1
                cols = cols + 1
            j = j + 1
            i = i - 1
        
    #Diagonal Reversed
    for i in range(0, grid_rows, +1):
        j = grid_cols - 1
        while(i < grid_rows and j > -1):
            temp = ""
            rows = i
            cols = j
            index_holder_array = []
            while (rows < grid_rows and cols > -1):
                temp = temp + grid[rows][cols]
                index_holder_array.append((rows, cols))
                if (temp == input):
                    array_holder.append((temp, list(reversed(index_holder_array))))
                    count = count + 1
                    break
                rows = rows + 1
                cols = cols - 1
            i = i + 1
            j = j - 1

    return clear_reps(array_holder)


class WordFinder:
    def set_grid(self, grid):
        self.grid = grid

    def count(self, word):
        # TODO
        temp1 = diagonals(self.grid, word)
        temp2 = non_diagonal(self.grid, word)
        count = len(final_clear(temp1, temp2))
        return count

'''    
if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0     
 '''

if __name__ == "__main__":
    start = time.time()
    

    
    grid = ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("A")) #17
    print(finder.count("BAAB")) # 3
    print(finder.count("ABB")) # 16
    print(finder.count("AB")) # 46
    print(finder.count("BAA")) # 15

    end = time.time()
    print(end - start)

#automate the boring stuff
#chapter 4 - lists
#character picture guide

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#defines printing function
def grid_print(entry):
    for y in range(len(entry[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print('')

            
#calls grid_print function on entry
grid_print(grid)

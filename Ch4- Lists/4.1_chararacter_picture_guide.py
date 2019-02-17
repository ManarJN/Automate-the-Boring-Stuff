#automate the boring stuff
#chapter 4 - lists
#character picture guide - program that prints a given list of lists

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
def gridPrint(entry):
    for y in range(len(entry[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print('')

            
#calls gridPrint function on entry
gridPrint(grid)

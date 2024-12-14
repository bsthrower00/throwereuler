with open('p096_sudoku.txt', 'r') as f:
    lines = f.readlines()

sudokus = []
cur_sudoku = []

for line in lines:
    line = line.strip()
    if line.startswith('Grid'):
        if cur_sudoku:
            sudokus.append(cur_sudoku)
        cur_sudoku = []
    else:
        cur_sudoku.append([int(x) for x in line])

if cur_sudoku:
    sudokus.append(cur_sudoku)

print(len(sudokus))


def validSpot(sudoku, digit, x, y):
	if digit in sudoku[x]:
		return False
	if digit in [sudoku[X][y] for X in range(9)]:
		return False
	if x % 3 == 0:
		X = [x, x+1, x+2]
	elif x % 3 == 1:
		X = [x-1, x, x+1]
	else:
		X = [x-2, x-1, x]
	if y % 3 == 0:
		Y = [y, y+1, y+2]
	elif y % 3 == 1:
		Y = [y-1, y, y+1]
	else: 
		Y = [y-2, y-1, y]
	box = []
	for i in X:
		for j in Y:
			
			box.append(sudoku[i][j])
	if digit in box:
		return False
	return True
	
def recSudoku(sudoku, x=0, y=0):
	if y == 9:
		y=0
		x+= 1
		if x == 9: 
			return True
	if sudoku[x][y] != 0:
		return recSudoku(sudoku, x, y+1)
	
	for i in range(9):
		if validSpot(sudoku, i+1, x, y):
			sudoku[x][y] = i+1
		
			if recSudoku(sudoku,x,y+1):
				return True
			
			sudoku[x][y]=0
		
	return False
	
c = 0
for i in range(len(sudokus)):
	recSudoku(sudokus[i])
	print(i)
	for j in range(len(sudokus[i])):
		print(sudokus[i][j])
		if j == 0:
			c += 100 * int(sudokus[i][j][0]) + 10 * int(sudokus[i][j][1])+  int(sudokus[i][j][2])
print(c)
		
	










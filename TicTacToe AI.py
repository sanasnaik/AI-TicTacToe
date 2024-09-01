computer = 'x'
human = 'o'

# Checks if a win exists. Returns 1 for computer win, -1 for human win, 0 for no win
def win_exists(board):
	
	for row in range(3):
		if (board[row] == [computer, computer, computer]):
			return 1
		elif (board[row] == [human, human, human]):
			return -1

	for col in range(3):
		if (board[0][col] == board[1][col] == board[2][col]):
			if (board[0][col] == computer):
				return 1
			elif (board[0][col] == human):
				return -1

	if (board[0][0] == board[1][1] == board[2][2]):
		if (board[0][0] == computer):
			return 1
		elif (board[0][0] == human): 
			return -1

	if (board[0][2] == board[1][1] == board[2][0]):
		if (board[0][2] == computer):
			return 1
		elif (board[0][2] == human):
			return -1

	return 0

# Generates the optimal move
def get_move(board): 

	bestScore = float('-inf')
	bestMove = {-1, -1}

	for i in range(3):
		for j in range(3):

			if (board[i][j] == '_'):
				board[i][j] = computer
				moveScore = minimax(board, False) 
				board[i][j] = '_'

				if (moveScore > bestScore):				 
					bestMove = (i, j) 
					bestScore = moveScore

	if bestScore == 1:
		print("Computer Wins!")
	else:
		print("Your Move/Update Board")
	
	return bestMove 

# Recursive function that evaluates all possible moves
def minimax(board, isMax):

	score = win_exists(board) 

	if (score == 1 or score == -1): # if move ends in a win (maximize your score)
		return score

	if (moves_exist(board) == False): # if move ends in a tie (minimize your losses)
		return 0

	# If this computer's move 
	if (isMax):
		best = float('-inf')

		for i in range(3):		 
			for j in range(3): 
				if (board[i][j] == '_'):
					board[i][j] = computer 
					best = max(best, minimax(board, not isMax)) 
					board[i][j] = '_'
		return best 

	# If this human's move 
	else: 
		best = float('inf')

		for i in range(3):		 
			for j in range(3): 
				if (board[i][j] == '_'): 
					board[i][j] = human 
					best = min(best, minimax(board, not isMax)) 
					board[i][j] = '_'
		return best 

def moves_exist(board): 

	for i in range(3): 
		for j in range(3): 
			if (board[i][j] == '_') : 
				return True
			
	return False

# Main Code
board = [
	['o','x','o'],
	['o','o','x'], 
	['x','_','x'] 
] 

if not moves_exist(board):
	print("Game Over.")
else:
	win = win_exists(board)
	if win == 1:
		print("Computer Wins!")
	elif win == -1:
		print("You Win!")
	else:
		move = get_move(board) 
		board[move[0]][move[1]] = computer
	
print("Board:")
for i in range(3):
	print(board[i])
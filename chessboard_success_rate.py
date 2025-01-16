import random

# Chessboard dimensions
N = 8

# All possible moves for a knight
def get_knight_moves():
    return [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# Check if the move is valid and within bounds.
def is_valid_move(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Las vegas. Returns True for successful tour and False for failed tour
def las_vegas_tour(board, start_x, start_y, is_closed):
    knight_moves = get_knight_moves()
    x, y = start_x, start_y
    board[x][y] = 0

    for step in range(1, 64):
        valid_moves = [(x + dx, y + dy) for dx, dy in knight_moves if is_valid_move(x + dx, y + dy, board)]
        if not valid_moves:
            return False  

        x, y = random.choice(valid_moves)
        board[x][y] = step

    if is_closed:
        return any((x + dx, y + dy) == (start_x, start_y) for dx, dy in knight_moves)  #Check to return to the starting square

    return True  

# Backtracking. Returns True for successful tour and False for failed tour
def backtracking_tour(board, x, y, step, is_closed):
    if step == 64:
        if not is_closed or (x, y) == (start_x, start_y):
            return True
        return False

    knight_moves = sorted(get_knight_moves(),
                          key=lambda move: sum(1 for dx, dy in get_knight_moves() if is_valid_move(x + move[0] + dx, y + move[1] + dy, board)))

    for dx, dy in knight_moves:
        next_x, next_y = x + dx, y + dy
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = step
            if backtracking_tour(board, next_x, next_y, step + 1, is_closed):
                return True
            board[next_x][next_y] = -1

    return False

#main program begins

# initialization of variables
chessboard = [[-1 for _ in range(N)] for _ in range(N)] # using a 2D list for 8 by 8 chessboard
user_version_choice = -1
user_approach_choice = -1
is_user_version_choice_valid = False
is_user_approach_choice_valid = False
success = False

# Display the initial chessboard
print("Initial chess board state\n")
for row in chessboard:
    print(" ".join(str(row)))

#user inputs start
while(not is_user_version_choice_valid):
    user_version_choice = input("Which version?\nEnter 1 for open version.\nEnter 2 for closed version.\nversion? ")
    if(user_version_choice not in ["1", "2"]):
       print("You have entered a wrong value")
    else:
        is_user_version_choice_valid = True

while(not is_user_approach_choice_valid):
    user_approach_choice = input("Which approach?\nEnter 1 for Backtracking.\nEnter 2 for Las Vegas .\napproach? ")
    if(user_approach_choice not in ["1", "2"]):
       print("You have entered a wrong value")
    else:
        is_user_approach_choice_valid = True


start_x = int(input("Enter the starting x-coordinate (0-7): "))
start_y = int(input("Enter the starting y-coordinate (0-7): "))

#user input ends

is_closed = True if user_version_choice == 2 else False

# Run the appropriate tour and track success
success_count = 0
attempts = 10000

for _ in range(attempts):
    #selecting the right tour
    if user_approach_choice == "2":
        success = las_vegas_tour(chessboard, start_x, start_y, is_closed)
    elif user_approach_choice == "1":
        chessboard[start_x][start_y] = 0
        success = backtracking_tour(chessboard, start_x, start_y, 1, is_closed)

    if success:
        success_count += 1


success_rate = success_count/attempts

print("success rate: ", success_rate)



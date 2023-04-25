import itertools

# Initialize the game board and the player symbols
board = {i: " " for i in range(1, 10)}
players = itertools.cycle(["X", "O"])


# Define a function to display the current board
def display_board(board):
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")


# Define a function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[1] == board[5] == board[9] == player:
        return True
    if board[3] == board[5] == board[7] == player:
        return True
    return False


# Define a function to check if the game is a tie
def check_tie(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True


# Define a function to play the game
def play_game():
    # Initialize the board and the player symbols
    board = {i: " " for i in range(1, 10)}
    players = itertools.cycle(["X", "O"])

    # Loop until someone wins or there is a tie
    while True:
        # Get the current player and their move
        player = next(players)
        display_board(board)
        move = input(f"{player}'s turn. Enter a number from 1-9: ")

        # Check if the move is valid
        if move.isdigit() and int(move) in board and board[int(move)] == " ":
            board[int(move)] = player
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the game has ended
        if check_win(board, player):
            display_board(board)
            print(f"{player} wins!")
            return player
        elif check_tie(board):
            display_board(board)
            print("Cat!")
            return None


# Define a function to keep score
def update_score(scores, winner):
    if winner is None:
        scores["ties"] += 1
    else:
        scores[winner] += 1


# Define a function to display the scores
def display_scores(scores):
    print("Current scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    print()


# Initialize the scores
scores = {"X": 0, "O": 0, "ties": 0}

# Loop until the players want to stop playing
while True:
    # Play a game and update the scores
    winner = play_game()
    update_score(scores, winner)

    # Display

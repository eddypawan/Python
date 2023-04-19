import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a 2D list to represent the game board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create a function to handle player moves
def player_move(row, col):
    # Check if the square is empty
    if board[row][col] == 0:
        # Set the square to the player's symbol
        board[row][col] = player
        # Update the button text
        buttons[row][col].config(text=player)
        # Check for a win or a draw
        check_win()
        # Switch to the other player
        switch_player()

# Create a function to switch players
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
    label.config(text="Player " + player + "'s turn")

# Create a function to check for a win or a draw
def check_win():
    global board
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            label.config(text="Player " + player + " wins!")
            disable_buttons()
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            label.config(text="Player " + player + " wins!")
            disable_buttons()
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        label.config(text="Player " + player + " wins!")
        disable_buttons()
    if board[0][2] == board[1][1] == board[2][0] != 0:
        label.config(text="Player " + player + " wins!")
        disable_buttons()
    # Check for a draw
    if all([all(row) for row in board]) and not check_win():
        label.config(text="It's a draw!")
        disable_buttons()

# Create a function to disable all buttons
def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state="disabled")

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", font=("Arial", 32), width=3, height=1,
                           command=lambda row=row, col=col: player_move(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Create the label to show whose turn it is
player = "X"
label = tk.Label(root, text="Player " + player + "'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

# Run the main loop
root.mainloop()

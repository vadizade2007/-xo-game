def display_board(board):
    for row in board:
        print(row)


def make_move(board, player, row, col):
    board[row][col] = player


def check_game(board):
    for i in range(3):
        # بررسی سطرها
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return True, board[i][0]
        # بررسی ستون ها
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return True, board[0][i]
    # بررسی قطرها
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True, board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True, board[0][2]
    # بررسی تساوی
    elif all([all(row) for row in board]):
        return True, None
    else:
        return False, None


def play_game(player1=None, board=None, player2=None):
    player = player1
    while True:
        display_board(board)
        # خواندن ورودی از بازیکن
        row = int(input(f'{player}, Enter row number (0-2): '))
        col = int(input(f'{player}, Enter column number (0-2): '))
        # بررسی صحت ورودی بازیکن
        if row not in range(3) or col not in range(3):
            print('Invalid input. Try again.')
            continue
        if board[row][col] != '':
            print('This place is already filled. Try another one.')
            continue
        # اعمال حرکت بازیکن
        make_move(board, player, row, col)
        # بررسی وضعیت بازی
        game_over, winner = check_game(board)
        if game_over:
            display_board(board)
            if winner:
                print(f'{winner} wins!')
            else:
                print('It is a tie!')
            break
        # تغییر نوبت بازیکن
        player = player2 if player == player1 else player1
    play_game()

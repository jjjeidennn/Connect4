# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name: Jayden Phan
# Student Number: 48821971
# ----------------

def num_hours() -> float:
    """
    Checks number of hours spent on assignment

    Returns:
        float: number of hours in floating point numbers 
            (number w/ decimal)

    Example:
        hours_spent = 12.5
        >>> print(num_hours())
        12.5
    """
    hours_spent = 100.5
    return hours_spent


def generate_initial_board() -> list[str]:
    """
    Returns initial board state (empty board state)
    
    Returns:
        list[str]: each column is a string where first string represents
            leftmost column, & last string in list represents rightmost 
            column.  
            first character of each string represents top of associated 
            column, & last character of each string represents bottom 
            of associated column.
    Example:
        >>> generate_initial_board
        ['--------', '--------', '--------', '--------', '--------', 
        '--------', '--------', '--------']
    """
    return ['--------'] * 8

def is_column_full(column: str) -> bool:
    """
    Checks if column is full.

    Parameters:
        column(str): each character in column string represents cell in column.
        'X' or 'O' indicates specific player's piece, & '-' indicates 
        empty cell.
    
    Returns:
        bool: True if column full (has no empty spaces), False otherwise.
            
    Example:
        >>> column = "---XOXXX"
        is_column_full(column)
        False
        >>> column = "OXXOOXOO"
        is_column_empty(column)
        True
    """
    for char in range(BOARD_SIZE):
        if column[char] == BLANK_PIECE:
            return False

        return True
    
        
def is_column_empty(column: str) -> bool: 
    """
    Checks if column is empty (reverse of var is_column_full).
    
    Parameters:
        column(str): each character in column string represents cell in column.
            'X' or 'O' indicates specific player's piece, & '-' indicates 
            blank piece / empty cell.
    
    Returns:
        bool: True if column has empty spaces, false otherwise
    
    Example:
        >>> column1 = "---XOXXX"
        is_column_empty(column1)
        True
        >>> column2 = "OXXOOXOO"
        is_column_empty(column2)
        False
    """
    if column == BLANK_PIECE * 8:
        return True
    
    return False

def display_board(board: list[str]) -> None:
    """
    Prints game board with columns separared by pipe characters (--------) & 
        numbered below
    
    Parameters:
        board (list[str]): List of strings representing game board.
            Each string should have EXACTLY 8 strings. Each string represents
            column of game board
            
    Returns:
        none

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters, representing valid game board state.
    """
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
                print(COLUMN_SEPARATOR, end = "")
                print(board[column][row], end = "") 
                # prints "|-" 7 times & ensures entire row printed on same line
                # end="" needed so it doesn't print new line

        print(COLUMN_SEPARATOR) 
        # after printing all cells in row, column_separator printed to 
        #  seal the end & complete row
    print(" 1 2 3 4 5 6 7 8 ")

def check_input(command: str) -> bool:
    '''
    Checks if given command is valid based on all valid commands.

    Parameters:
        command (str): Input command to be checked.

    Returns:
        bool: True if given command is valid, False otherwise.

    Preconditions:
        Command must be a string

    Example:
        >>> command = "a1"
        >>> check_input(command)
        True
        >>> command = "r1"
        >>> check_input(command)
        True
        >>> command = "a3"
        >>> check_input(command)
        True
        >>> command = "h"
        >>> check_input(command)
        True
        >>> command = "1r"
        >>> check_input(command)
        Invalid command. Enter 'h' for valid command format
        False
        >>> command = "a3 "
        >>> check_input(command)
        Invalid command. Enter 'h' for valid command format
        False
        >>> command = "a9"
        >>> check_input(command)
        Invalid column, please enter a number between 1 and 8 inclusive
        False
        >>> command = ""
        >>> check_input(command)
        Invalid command. Enter 'h' for valid command format
        False
    '''
    board_input_letters =  "aArR"
    command_input_letters = "hHqQ"
    
    valid_numbers = "12345678"

    if command == "":
        print(INVALID_FORMAT_MESSAGE)
        return False

    if command in command_input_letters and len(command) == 1:
        return True
    
    if (command[0] in board_input_letters and command[1:] not in valid_numbers 
          and len(command) == 2):
        print(INVALID_COLUMN_MESSAGE)
        return False

    if (command[0] in board_input_letters and command[1:] in valid_numbers 
          and len(command) == 2):
        return True

    print(INVALID_FORMAT_MESSAGE)
    return False

def get_action() -> str:
    '''
    Prompt user for command until valid command is entered.

    Returns:
        str: Valid command entered by user
    
    Example:
        >>> get_action()
        Please enter action (h to see valid commands): r-1
        Invalid command. Enter 'h' for valid command format
        Please enter action (h to see valid commands): a
        Invalid command. Enter 'h' for valid command format
        Please enter action (h to see valid commands): r4
        'r4'
        >>> get_action()
        Please enter action (h to see valid commands): g
        Invalid command. Enter 'h' for valid command format
        Please enter action (h to see valid commands): help
        Invalid command. Enter 'h' for valid command format
        Please enter action (h to see valid commands): H
    '''
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if check_input(command):
            return command

def add_piece(board: list[str], piece: str, column_index: int) -> bool:
    '''
    Adds specified piece to column at given column index of board.

    Parameters:
        board (list[str]): Game board represented as list of strings
        piece (str): Piece to be added to game board. 
            Should be exactly one character in length, to fit into cell.
        column_index (int): 0-indexed column index where piece should 
            be added.

    Returns:
        bool: True if piece was successfully added to game board, 
            False otherwise

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters, representing valid game board state.
        - Specified column index must be between 0 - 7 inclusive.
        - Specified piece must be exactly one character in length.

    Example:
        >>> board = ['--------', '----OOOO', 'XXXXXXXX', '--------', '------XO',
        '--------', '---XXOXO', '--------']
        >>> add_piece(board, "X", 1)
        True
        >>> board
        ['--------', '---XOOOO', 'XXXXXXXX', '--------', '------XO', '--------',
        '---XXOXO', '--------']
        >>> add_piece(board, "O", 2)
        You can't add a piece to a full column!
        False
        >>> board
        ['--------', '---XOOOO', 'XXXXXXXX', '--------', '------XO', '--------',
        '---XXOXO', '--------']
        >>> add_piece(board, "e", 1)
        True
        >>> board
        ['--------', '--eXOOOO', 'XXXXXXXX', '--------', '------XO', '--------',
        '---XXOXO', '--------']
    '''

    if is_column_full(board[column_index]):
        print(FULL_COLUMN_MESSAGE)
        return False

    for row_index in range(BOARD_SIZE - 1, -1, -1):
        if board[column_index][row_index] == BLANK_PIECE: 
            remaining_pieces = board[column_index][row_index + 1:] 
            # saves pieces after new piece added 
            #   (ie. blank pieces)
            board[column_index] = board[column_index][:row_index] 
            # keeps right amount of existing player pieces in string before 
            #  adding new piece
            board[column_index] += piece 
            # adds new piece 
            board[column_index] += remaining_pieces 
            # adds remaining pieces to string
            #   (ie. filling rest of string with blank pieces)
            return True
      
    return False

def remove_piece(board: list[str], column_index: int) -> bool:
    '''
    Removes bottom-most piece from column at given column_index of game board

    Parameters:
        board (list[str]): Game board is represented as list of strings
        column_index (int): 0-indexed column index from which the piece should 
        be removed.
    
    Returns:
        bool: True if piece was successfully removed from game board. 
            False otherwise.

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters, representing a valid game state.
        - Specified column index must be between 0 - 7 inclusive.

    Example:
        >>> board = ['--------', '----OOOO', 'XXOOOXXX', '--------', '------XO',
        '--------', '---XXOXO', '--------']
        >>> remove_piece(board, 2)
        True
        >>> board
        ['--------', '----OOOO', '-XXOOOXX', '--------', '------XO', '--------',
        '---XXOXO', '--------']
        >>> remove_piece(board, 0)
        You can't remove a piece from an empty column!
        False
        >>> board
        ['--------', '----OOOO', '-XXOOOXX', '--------', '------XO', '--------',
        '---XXOXO', '--------']
    '''

    if is_column_empty(board[column_index]):
        print(EMPTY_COLUMN_MESSAGE)
        return False

    else:
        board[column_index] = BLANK_PIECE + board[column_index][0:7]
        # removes bottom piece by adding blank piece & integrating with
        #  substring from index 0 to 7 of original column string.

    return True

def win_horizontal(board: list[str], piece: str) -> Optional[str]:
    '''
    Checks for a horizontal win for a specific piece on the game board

    Parameters:
        board (list[str]): List of strings represent game board.
            Each string represents a row of game board.
        piece (str): Specific piece to check for a win ('X' or 'O').

    Returns:
        Optional[str]: Winning piece ('X' or 'O') if there's a horizontal win, 
            None otherwise.

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters
        - Each string in game board list must have exactly 8 characters.
        - Each character in game board must be '-', 'X', or 'O'
    '''
    for column_index in range(BOARD_SIZE):
        for row_index in range(BOARD_SIZE - (REQUIRED_WIN_LENGTH - 1)):
            # loop iterates only over rows that have enough remaining row
            #  indexes to achieve horizontal win.
            #   (ie. checking row_index 5 onwards (to 8) -> not possible 
            #    for horizontal win)
            
            win_indicator = True
            for incrementer in range(REQUIRED_WIN_LENGTH):
                if board[row_index + incrementer][column_index] != piece:
                    win_indicator = False
                    break
            if win_indicator:
                return piece
            
    return None

def win_vertical(board: list[str], piece: str) -> Optional[str]:
    '''
    Checks for a vertical win for a specific piece on the game board

    Parameters:
        board (list[str]): List of strings represent game board.
            Each string represents a row of game board.
        piece (str): Specific piece to check for a win ('X' or 'O').

    Returns:
        Optional[str]: Winning piece ('X' or 'O') if there's a vertical win, 
            None otherwise.

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters
        - Each string in game board list must have exactly 8 characters.
        - Each character in game board must be '-', 'X', or 'O'
    '''
    for row_index in range(BOARD_SIZE):
        for column_index in range(BOARD_SIZE - (REQUIRED_WIN_LENGTH - 1)):
            # loop iterates only over columns that have enough remaining column
            #  indexes to achieve vertical win.
            #   (ie. checking column_index 5 onwards (to 8) -> not possible 
            #    for vertical win)

            win_indicator = True
            for incrementer in range(REQUIRED_WIN_LENGTH):
                if board[row_index][column_index + incrementer] != piece:
                    win_indicator = False
                    break
            if win_indicator:
                return piece
            
    return None

def win_diagonal_negative(board: list[str], piece: str) -> Optional[str]:
    '''
    Checks for a diagonal win in the negative gradient for a specific piece on 
    the game board

    Parameters:
        board (list[str]): List of strings represent game board.
            Each string represents a row of game board.
        piece (str): Specific piece to check for a win ('X' or 'O').

    Returns:
        Optional[str]: Winning piece ('X' or 'O') if there's a diagonal win in
            the negative gradient direction, None otherwise.

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters
        - Each string in game board list must have exactly 8 characters.
        - Each character in game board must be '-', 'X', or 'O'
    '''
    for row_index in range(BOARD_SIZE - (REQUIRED_WIN_LENGTH - 1)):
        # loop iterates only over rows that have enough remaining row
        #  indexes to achieve diagonal win (negative gradient direction).
        #   (ie. checking row_index 5 onwards (to 8) -> not possible 
        #    for diagonal win in negative direction)
        for column_index in range(BOARD_SIZE - (REQUIRED_WIN_LENGTH - 1)):
            # loop iterates only over columns that have enough remaining column
            #  indexes to achieve diagonal win (negative gradient direction).
            #   (ie. checking column_index 5 onwards (to 8) -> not possible 
            #    for diagonal win in negative direction)
            win_indicator = True
            for incrementer in range(REQUIRED_WIN_LENGTH):
                if (board[row_index + incrementer][column_index + incrementer] 
                    != piece):
                    win_indicator = False
                    break
            if win_indicator:
                return piece
                
    return None

def win_diagonal_positive(board: list[str], piece: str) -> Optional[str]:
    '''
    Checks for a diagonal win in the positive gradient for a specific piece on 
    the game board

    Parameters:
        board (list[str]): List of strings represent game board.
            Each string represents a row of game board.
        piece (str): Specific piece to check for a win ('X' or 'O').

    Returns:
        Optional[str]: Winning piece ('X' or 'O') if there's a diagonal win in
            the positive gradient direction, None otherwise.

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters
        - Each string in game board list must have exactly 8 characters.
        - Each character in game board must be '-', 'X', or 'O'
    '''
    for row_index in range(BOARD_SIZE - (REQUIRED_WIN_LENGTH - 1)): 
        # loop iterates only over rows that have enough remaining row
        #  indexes to achieve diagonal win (positive gradient direction).
        #   (ie. checking row_index 5 onwards (to 8) -> not possible 
        #    for diagonal win in positive direction)
        for column_index in range((REQUIRED_WIN_LENGTH - 1), BOARD_SIZE):
            # loop iterates only over columns that have enough remaining column
            #  indexes to achieve diagonal win (positive gradient direction).
            #   (ie. checking column index from 0 to 2 -> not possible
            #    for diagonal win in positive direction)
            win_indicator = True
            for incrementer in range(REQUIRED_WIN_LENGTH):
                if (board[row_index + incrementer][column_index - incrementer] 
                    != piece):
                    win_indicator = False
                    break
            if win_indicator:
                return piece

    return None

def check_win(board: list[str]) -> Optional[str]:
    '''
    Checks given game board state for a win or a draw

    Parameters:
        board (list[str]): Game board is represented as list of strings.
    
    Returns:
        Optional[str]: Piece of player who won, blank piece for draw, or None
            for no winner

    Preconditions:
        - Game board must have exactly 8 strings, each with exactly 8 
            characters
        - Each character in game board must be 'X', 'O', or '-'

    Example:
        >>> board = ['------XO', '-------O', '--------', '--------', '-------O',
        '--------', '--------', '------XX']
        >>> check_win(board)
        >>> board = ['-------O', '------OX', '-----OXO', '---XOOXX', '--------',
        '--------', '--------', '--------']
        >>> check_win(board)
        'O'
        >>> board = ['-------X', '-------X', '------OX', '---OOOXX', '--------',
        '--------', '--------', '--------']
        >>> check_win(board)
        'X'
        >>> board = ['---XXXXO', '-------O', '-------O', '-------O', '--------',
        '--------', '--------', '--------']
        >>> check_win(board)
        '-'
        >>> board = ['--------', '--------', '---O----', '---O----', '---O----',
        '---O----', '--------', '--------']
        >>> check_win(board)
        'O'
    '''
    player_1_winner = False
    player_2_winner = False

    # checking horizontal spaces
    if win_horizontal(board, PLAYER_1_PIECE):
        player_1_winner = True
    if win_horizontal(board, PLAYER_2_PIECE):
        player_2_winner = True
    
    # checking vertical spaces
    if win_vertical(board, PLAYER_1_PIECE):
        player_1_winner = True
    if win_vertical(board, PLAYER_2_PIECE):
        player_2_winner = True

    # checking diagonal spaces (negative gradient) 
    if win_diagonal_negative(board, PLAYER_1_PIECE):
        player_1_winner = True
    if win_diagonal_negative(board, PLAYER_2_PIECE):
        player_2_winner = True

    # checking diagonal spaces (positive gradient)
    if win_diagonal_positive(board, PLAYER_1_PIECE):
        player_1_winner = True
    if win_diagonal_positive(board, PLAYER_2_PIECE):
        player_2_winner = True 


    if player_1_winner and player_2_winner:
        return BLANK_PIECE
    if player_1_winner:
        return PLAYER_1_PIECE
    if player_2_winner:
        return PLAYER_2_PIECE
    else:
        return None

def play_game() -> None:
    '''
    Manages gameplay of single game from start to finish

    Returns:
        None
    
    Preconditions:
        - All written functions must be implemented correctly & be available 
            for use.
    '''
    player_turn_counter = 2
    board = generate_initial_board()
    current_player = PLAYER_1_PIECE

    display_board(board)

    while True:
        if player_turn_counter % 2 == 0:
            current_player = PLAYER_1_PIECE
            print(PLAYER_1_MOVE_MESSAGE)
        if player_turn_counter % 2 == 1:
            current_player = PLAYER_2_PIECE
            print(PLAYER_2_MOVE_MESSAGE)
        # switches player after player inputs successful command
        # if turn counter is divisible by 2, then it is Player 1's turn
        # if turn counter gives remainder of 1 after being divided by 2, then
        #  it is Player 2's turn

        while True:

            player_input = get_action()

            if check_input(player_input):
                if player_input[0] == "r" or player_input[0] == "R":
                    column_input = player_input[1:] 
                    column_index = int(column_input) - 1
                    if remove_piece(board, column_index):
                        display_board(board)
                        player_turn_counter += 1
                        break

                if player_input[0] == "a" or player_input[0] == "A":
                    column_input = player_input[1:] 
                    column_index = int(column_input) - 1
                    if add_piece(board, current_player, column_index):
                        display_board(board)
                        player_turn_counter += 1
                        break

                if player_input[0] == "h" or player_input[0] == "H":
                    print(HELP_MESSAGE)
                    display_board(board)
                    if player_turn_counter % 2 == 0:
                        current_player = PLAYER_1_PIECE
                        print(PLAYER_1_MOVE_MESSAGE)
                    if player_turn_counter % 2 == 1:
                        current_player = PLAYER_2_PIECE
                        print(PLAYER_2_MOVE_MESSAGE)
                    # prompts correct move message for each player after 
                    #  entering "h" or "H" for help message
                    # if turn counter is divisible by 2, then it is 
                    #  Player 1's turn
                    # if turn counter gives remainder of 1 after being divided 
                    #  by 2, then it is Player 2's turn

                if player_input[0] == "q" or player_input[0] == "Q":
                    return
                # game terminates gracefully


        winner = check_win(board)
        if winner == PLAYER_1_PIECE:
            print(PLAYER_1_VICTORY_MESSAGE)
            return
        if winner == PLAYER_2_PIECE:
            print(PLAYER_2_VICTORY_MESSAGE)
            return
        if winner == BLANK_PIECE:
            print(DRAW_MESSAGE)
            return

def main() -> None:
    """
    Initiates Connect 4(ish) game & follows complete gameplay process.
    
    Returns:
        None

    Preconditions:
        - "play_game()" function must be implemented correctly & 
            available for use.
        - Script must be run directly to initiate Connect 4(ish) game.
    """
    play_game()

    while True:
        play_again = input(CONTINUE_MESSAGE)
        if play_again == "y" or play_again == "Y":
            play_game()
        else:
            break

if __name__ == "__main__":
    main()

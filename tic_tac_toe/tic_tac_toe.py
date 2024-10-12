# -*- coding: utf-8 -*-

'''Tic Tac Toe'''

import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for i in range(3):
            print('| ' + ' | '.join(self.board[i*3:(i+1)*3]) + ' |')

    def print_board_nums(self):
        """Prints the numbers corresponding to board positions."""
        number_board = [str(i + 1) for i in range(9)]
        for i in range(3):
            print('| ' + ' | '.join(number_board[i*3:(i+1)*3]) + ' |')

    def make_move(self, square, letter):
        """Places a move on the board and checks for a winner."""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        """Check the board for a win condition."""
        row_start = (square // 3) * 3
        row = self.board[row_start:row_start + 3]
        if all([spot == letter for spot in row]):
            return True

        col_start = square % 3
        column = [self.board[col_start + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move. The position is either occupied or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    game = TicTacToe()

    while True:
        player = 'X'
        ai_player = 'O'

        print("Do you want to go first (y/n)?")
        user_first = input().lower() == 'y'

        print("\nWelcome to Tic-Tac-Toe!")
        game.print_board_nums()
        print("\nThe game board:")
        game.print_board()

        if not user_first:
            move = random.choice([i for i in range(9) if game.board[i] == ' '])
            game.make_move(move, ai_player)
            print(f"pc ({ai_player}) chooses position {move + 1}")
            game.print_board()

        current_player = player

        while True:
            if current_player == player:
                move = get_move(game.board, player)
            else:
                move = random.choice([i for i in range(9) if game.board[i] == ' '])
                print(f"pc ({ai_player}) chooses position {move + 1}")

            game.make_move(move, current_player)
            game.print_board()

            if game.current_winner:
                print(f"Player {current_player} wins!")
                break

            if game.is_board_full():
                print("It's a tie!")
                break

            current_player = player if current_player == ai_player else ai_player

        if input("Would you like to play again (y/n)? ").lower() != 'y':
            print("Thank you for playing! Goodbye!")
            break
        else:
            game.reset()

if __name__ == "__main__":
    play_game()

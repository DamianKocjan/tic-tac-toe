import random
from enum import Enum

class Player(Enum):
  HUMAN = 1
  COMPUTER = 2

class TicTacToe:
  def __init__(self) -> None:
    self.board = [
      [None, None, None],
      [None, None, None],
      [None, None, None],
    ]

  def print_board(self) -> None:
    print('  0 1 2')
    print('  ------')

    for idx, row in enumerate(self.board):
      print(f'{idx}|{row[0] or " "} {row[1] or " "} {row[2] or " "}')

    print('  ------')

  def move(self, who: Player) -> None:
    if self.is_full():
      if who == Player.HUMAN:
        x, y = None, None

        x = int(input("What is your X co-ordinate?: "))
        y = int(input("What is your Y co-ordinate?: "))

        while x > 2 or \
          y > 2 or \
          self.board[y][x]:
          print('This field is not empty or your co-ordinates are wrong!')

          x = int(input("What is your X co-ordinate?: "))
          y = int(input("What is your Y co-ordinate?: "))
        else:
          self.board[y][x] = 'X'
      elif who == Player.COMPUTER:
        x, y = None, None

        x = random.randint(0, 2)
        y = random.randint(0, 2)

        while self.board[y][x]:
          x = random.randint(0, 2)
          y = random.randint(0, 2)
        else:
          self.board[y][x] = '0'
      else:
        raise ValueError('Wrong player!')
    else:
      return

  def is_full(self) -> bool:
    i = 0

    for row in self.board:
      for col in row:
        if col:
          i += 1

    if i == 9:
      return False
    return True

  def check(self):
    for row in self.board:
      r_sum = 0

      for col in row:
        if col == 'X':
          r_sum += 1
        elif col == '0':
          r_sum -= 1

        if r_sum == 3:
          return [True, Player.HUMAN]
        elif r_sum == -3:
          return [True, Player.COMPUTER]

      r_sum = 0

    cross_1 = 0

    if self.board[0][0] == 'X':
      cross_1 += 1
    elif self.board[0][0] == '0':
      cross_1 -= 1

    if self.board[1][1] == 'X':
      cross_1 += 1
    elif self.board[1][1] == '0':
      cross_1 -= 1

    if self.board[2][2] == 'X':
      cross_1 += 1
    elif self.board[2][2] == '0':
      cross_1 -= 1

    if cross_1 == 3:
      return [True, Player.HUMAN]
    elif cross_1 == -3:
      return [True, Player.COMPUTER]


    cross_2 = 0

    if self.board[0][2] == 'X':
      cross_2 += 1
    elif self.board[0][2] == '0':
      cross_2 -= 1

    if self.board[1][1] == 'X':
      cross_2 += 1
    elif self.board[1][1] == '0':
      cross_2 -= 1

    if self.board[2][0] == 'X':
      cross_2 += 1
    elif self.board[2][0] == '0':
      cross_2 -= 1

    if cross_2 == 3:
      return [True, Player.HUMAN]
    elif cross_2 == -3:
      return [True, Player.COMPUTER]

    return [False, Player.HUMAN]

  def run(self) -> None:
    status = self.check()

    while not status[0] and self.is_full():
      self.print_board()
      self.move(Player.HUMAN)

      status = self.check()
      if status[0]:
        if status[1] == Player.HUMAN:
          print('You have won!')
        else:
          print('You lost!')
          exit()

      if self.is_full():
        exit()

      self.print_board()
      self.move(Player.COMPUTER)

      status = self.check()
    else:
      self.print_board()

      if status[1] == Player.HUMAN:
        print('You have won!')
      else:
        print('You lost!')
        exit()


if __name__ == '__main__':
  tictactoe = TicTacToe()

  tictactoe.run()

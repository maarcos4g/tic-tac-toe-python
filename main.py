import os

play_again = "S"
plays = 0
who_play = 2 # 1-Jogador 1  |  2-Jogador 2
max_plays = 9
board=[
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "]
]
player1 = input('Digite o nome do Jogador 1 (X): ')
player2 = input('Digite o nome do Jogador 2 (O): ')
score = {player1: 0, player2: 0}

def draw_board():
  os.system('cls')
  print("   C0   C1   C2")
  print("L0:  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
  print("   -----------")
  print("L1:  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
  print("   -----------")
  print("L2:  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
  print("Jogadas: " + str(plays))
  

def play():
  global plays
  global who_play
  
  current_player = player1 if who_play == 1 else player2
  symbol = "X" if who_play == 1 else "O"
  
  if plays < max_plays:
    try:
      line = int(input(f'{current_player} em qual linha quer jogar? '))
      column = int(input(f'{current_player}, em qual coluna quer jogar? '))
      while board[line][column] != " ":
        print('Informe uma outra posição, essa já foi utilizada.')
        line = int(input(f'{current_player} em qual linha quer jogar? '))
        column = int(input(f'{current_player}, em qual coluna quer jogar? '))
      board[line][column] = symbol
      who_play = 1 if who_play == 2 else 2
      plays += 1
    except:
      print('Jogada inválida!')
      os.system('pause')
      

def verify_win():
  global board
  win = "N"
  symbols = ["X", "O"]
  
  for symbol in symbols:
    for i in range(3):
          if all([board[i][j] == symbol for j in range(3)]) or all([board[j][i] == symbol for j in range(3)]):
              win = symbol
              return win
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
          win = symbol
          return win
  return win


def save_result(winner):
  with open('placar_do_jogo.txt', 'a') as file:
    file.write(f"{player1} (X) x {player2} (O)\n")
    file.write(f"Placar: {player1} ({score[player1]}) x {player2} ({score[player2]})\n")
    file.write("Tabuleiro final:\n")
    for row in board:
      file.write(' | '.join(row) + '\n')
    file.write('\n')

def reset_game():
  global plays
  global who_play
  global board
  plays = 0
  who_play = 1
  board=[
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "]
]

def game():
  global score
  while True:
    draw_board()
    play()
    draw_board()
    winner = verify_win()
    if (winner != "N") or (plays >= max_plays):
      if winner == "X":
        print(f'{player1} ganhou!')
        score[player1] += 1
      elif winner == 'O':
        print(f'{player2} ganhou!')
        score[player2] += 1
      else:
        print('Empate!')
      save_result(winner)
      reset_game()
      play_again = input('Deseja jogar novanmente? (S/N)')
      if (play_again.upper() != "S"):
        break
        
game()
import random

sample_space = ['HEAD','TAIL']
is_game_over = False

def user_choice():
  '''
  INPUTS USER CHOICE AND RETURNS IT.
  '''
  choice ='wrong'
  while choice not in sample_space:
    choice=input('\nEnter your choice: (Head/Tail): ').upper()
    if choice not in sample_space:
      print('Invalid choice!')

  if choice=='HEAD':
    return ('HEAD','TAIL')
  return ('TAIL','HEAD')
#player1, player2=user_choice()

def replay():
  '''
  INPUTS IF USER WANTS TO REPLAY AND RETURNS IT.
  '''
  play='no'
  while play not in ['Y','N']:
    play=input('\nDo u want to play again? (Y/N): ').upper()
    if play not in ['Y','N']:
      print('Invalid choice!')

  return play=='Y'
#b=replay()

def toss():
  '''
  RETURNS TOSS OUTCOME
  '''
  output=''
  output=random.choice(sample_space)
  return output
#outcome=toss()

def winner(output_list,player1):
  '''
  CALLED FROM DISPLAY FN
  INPUTS OUTCOMES LIST, PLAYER CHOICE AND RETURNS WINNER
  '''
  counter=False
  global is_game_over

  if len(output_list)==2 and output_list[0]==output_list[1]==player1:
    counter=True
    is_game_over=True
    print('Congratulations, You won the game!')

  if counter==False and len(output_list)==3:
    if output_list[0]==output_list[1]==player1 or output_list[0]==output_list[2]==player1 or output_list[1]==output_list[2]==player1:
      print('Congratulations, You won the game!')
    else:
      print('Oops, Computer won the game!')

def display(output_list,i,player1):
  '''
  DISPLAY RESULT OF EACH ROUND
  CALLS WINNER FN TO CHECK FOR WINNER AFTER EACH ROUND.
  '''
  print('\noutcome of toss no: ', i+1)
  print(output_list)
  winner(output_list,player1)

def game():
  '''
  MAIN FN - CALLS ALL FN IN ORDER .
  '''
  play=True
  while play:
    print('Welcome to Coin-toss Game!')
    #user=input('Enter your name: ')
    print('Lets play! ')
    output_list=[]
    player1, Computer = user_choice()

    for i in range(3):
      if not is_game_over:
        output=toss()
        output_list.append(output)
        display(output_list,i,player1)
    
    play=replay()
    print('\n')

#CALLING THE MAIN FN    
game()


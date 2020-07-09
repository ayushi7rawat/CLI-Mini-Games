from random import shuffle
#function -1
def shuffle_list(l1):
  shuffle(l1)
  return l1

#function-2
def player_guess():
  print('Hello!')
  print('Welcome to the Carnival guessing game: Three Cup Monte')
  guess=''
  while guess not in ['0','1','2']:
    guess=input('choose: 0, 1 or 2: ')
  return int(guess)

#function-3
def check_guess(my_list,guess):
  print(my_list)
  if my_list[guess]=='o':
    print('You won!')
  else:
    print('You lose!')

#fuction-4
def game(choice):
  if choice.lower() == 'y':
    #final composition
    #INITIAL LIST
    my_list=['','o','']
    #SHUFFLE LIST
    mixedup_list=shuffle_list(my_list)
    #USER GUESS
    guess=player_guess()
    #CHECK GUESS
    check_guess(mixedup_list,guess)
  else:
    print("Thanks for playing")
    return False

gameplay = True
game('y')
while gameplay == True:
  gameplay = game(input("Do you wana play again? Y/N\n"))
#Dice Race Game
if __name__ == '__main__':
  from random import randint

  name1 = input('Enter Player 1 Name: ')
  name2 = input('Enter Player 2 Name: ')
  finishing_score = int(input('\nEnter Finishing Score: '))

  user_choice=input('\nStart the game Y/N ').upper()

  name1_score=name2_score=0
  flag1=flag2=False
  
  if user_choice=='Y':
    user_continue='Y'

    while user_continue=='Y':
      print("\nIts {}'s Turn: ".format(name1))
      player1_tempscore=randint(1,6)
      print(f"{name1} got: {player1_tempscore}")
      name1_score=name1_score+player1_tempscore

      if int(name1_score)>=finishing_score:
        flag1=True
        break

      print("Its {}'s Turn: ".format(name2))
      player2_tempscore=randint(1,6)
      print(f"{name2} got: {player2_tempscore}")
      name2_score=name2_score+player2_tempscore

      if int(name2_score)>=finishing_score:
        flag2=True
        break

      print('\nscore for this round: ')
      print(f"{name1}'s score: {name1_score}")
      print(f"{name2}'s score: {name2_score}")

      user_continue = input('next move? Y/N: ').upper()
    else:
      print('\nGAME OVER! Thank you for joining ')
  else:
    print('\nThankyou for participating!')

  if flag1==True:
    print('\nGAME OVER! ')
    print(f"{name1}'s score: {name1_score}")
    print(f"{name2}'s score: {name2_score}")
    print(f'{name1} won! Congratulations! ')
  if flag2==True:
    print('\nGAME OVER! ')
    print(f"{name1}'s score: {name1_score}")
    print(f"{name2}'s score: {name2_score}")
    print(f'{name2} won! Congratulations! ')
from random import randint
num=randint(0,101)
print(num)

guess_list=[]
  
while True: 
  a = input('enter a number between 1-100 \n')

  if int(a)>=1 and int(a)<=100:
    guess_list.append(int(a))
  else:
    print('num is out of bounds,please enter again \n')
    continue 

  if guess_list[-1]==num:
    print('you guessed it!')
    break
  elif abs(guess_list[0]-num) <=10 and len(guess_list) == 1:
    print('WARM')
  elif len(guess_list) == 1:
    print('COLD')
  else:
    if abs(num-guess_list[-2]) > abs(num-guess_list[-1]):
      print("Warmer")
    else:
      print("Colder")

print("Game over!")
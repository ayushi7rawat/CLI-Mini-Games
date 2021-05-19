#  A simple Calculator program
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

print('Hi There, Lets calculate!')
print('\nChoose the operation you wish to perform: ')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

user_choice=int(input('Enter your choice: ')) # Corrected this on basis of Opened Issue by @Madhusudan pareek

if user_choice in [1,2,3,4]:
  n1=float(input('Enter 1st num: '))
  n2=float(input('Enter 2nd num: '))

  if user_choice==1:
    print(add(n1,n2))
  elif user_choice==2:
    print(sub(n1,n2))
  elif user_choice==3:
    print(mul(n1,n2))
  else:
    print(div(n1,n2))
else:
  print('Invalid choice!')
  

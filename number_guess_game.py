import random

top_of_range =input('Type your number ')
if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range<=0:
    print('write the number larger than 0 next time')
    quit()

else:
  print('please write a number ')
  quit()    

r = random.randint(0,top_of_range)

while True:
  guess = input('make guess again')
  if guess.isdigit():
    guess =int(guess)

  else:
    print('please enter a number next time')


  if guess == r:
      print('you got it')
      break
  else:
      print('wrong')
      continue
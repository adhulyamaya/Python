print('hellow world!! welcome to computer QUIZ')
play = input('Are you intrested to play quiz? ')

if play != 'yes':
  quit
else:
  print('okey!Lets play :)')  
score=0
ans = input('what is the full form of CCNA?')
if ans == 'Cisco Certified Network Associate':
  print('correct ans')
  score+=1
else:
  print('wrong ans')
ans = input('what is the full form of OOPS?')
if ans == 'object oriented programming language':
  print('correct ans')
  score+=1
else:
  print('wrong ans')

ans = input('what is the full form of ccnp?')
if ans == 'Cisco Certified Network Professional':
  print('correct ans')
  score+=1
else:
  print('wrong ans')  
print("you got"+ str(score) +'correct ans')
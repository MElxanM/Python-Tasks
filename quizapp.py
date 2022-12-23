n=5
t=0
print('You will be asked 5 questions')
print('1) What is the capital city of USA?')
a=input()
if a=='Washington':
  t=t+1
print('2) What is the longest river in the world?')
a=input()
if a=='Nile':
  t=t+1
print('3) What is the biggest lake in the world?')
a=input()
if a=='Caspian Sea':
  t=t+1
print('4) How many letters are there in Azerbaijani alphabet?')
a=input()
if a=='32':
  t=t+1
print('5) What is the largest continent in the world?')
a=input()
if a=='Asia':
  t=t+1

print('Your scoe is', t/n*100)

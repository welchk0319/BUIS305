number1=int(input('Enter Number 1:'))
if(number1%3==0 and number1%5==0):
    print('Tic Tac')
elif(number1%5==0):
    print('Tac')
elif(number1%3==0):
    print("Tic")

count=1
while(count<20):
    print(count,end=',')
    if (count%3==0 and count%5==0):
        print('Tic Tac')
    elif (count%5==0):
        print('Tac')
    elif (count%3==0):
        print("Tic")
    count=count+1

import random
print(random.randint(1,50))

number2=int(input('Enter Numbber 2:'))
tmpcount=1
while(number2<=0 and tmpcount<5):
    number2=int(input('Enter Value Greater Than 0:'))
    print('Value of tmpcount:',tmpcount)
    tmpcount=tmpcount+1
import random
tmp2=(random.randint(1,50))
if(tmp2==number2):
    print('Perfect Match!')
elif(tmp2!=number2):
    print(tmp2,number2)

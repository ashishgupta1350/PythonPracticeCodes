import random

print("This game is simple, you will be asked to guess the number to accuracy that you decide. Accuracy may be set between 10% to 40%. Based on the accuracy, you will have multiple attempts at the guess. If your number is in the accurate part, and accuracy is high enough, then you will be scored or else a life will be taken away from you! You have 3 lives. You win if you guess the exact number! But if you dont, the higest score in all the rounds will be calculated. If you manage a score past 50, you win. Else you Loose.")

score=int(0)
lives=int(3)
print('')
accuracy=int(input('Enter Accuracy, can be 10 or 20 or 30. For 10, reward of correct guess is 10 pts, for 20, reward is 7 and for 30 reward is 5 pts :: '))

reward=5

if accuracy==10:
    reward=10
elif accuracy==20:
    reward=7
elif accuracy==30:
    reward=5
else:
    print('Invalid Accuracy selected')
    exit()

while(lives>0):
    num=random.randint(1,100)
    x=int(input('Enter the number you guessed : '))
    if x==accuracy:
        print('Oh, You won!')
        exit()
        
    elif x>=num-accuracy/2 and x<=num+accuracy/2:
        print('Scored')
        score=score+reward
    else:
        print('Oopes, That didnot count')
        
        lives-=1

print('So your final score is : ',score)

if score>=50:
    print('Great, you won!')
else :
    print('Sorry, other people were more lucky than you, so you lost.')


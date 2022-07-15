'''
This is a quiz game made by Aansh Ojha 
It's Attempt Number - 1
'''

approval = input('Hi, I want to ask you a few questions. Can I ?\n')

# if approval == 'yes' or 'Yes' or 'ok' : not working 

if approval in ('yes','Yes','ok') :
    print('Sure ! Let\'s start...')
    q1 = input('Question 1 -\nWhich is the longest word in English Dictionary?\n I. Chlorofluorocarbon\n II. Antidisestablishmentarianism\n III. Mississippisistant\n')
    
    if q1 in ('2' , 'b' , 'second' , 'Antidisestablishmentarianism') :
        a1point = 10
        print('Hurrah ! You got 10 points...\nNow next question...')

    else :
        a1point = 0
        print('Ohh... You missed it.\nNow next question.')

    q2 = input('Which is the costliest thing in world?\n I. Bugatti Veyron with Gold paint\n II. Apple Ecosystem\n III. Respect\n')

    if q2 in ('3' , 'respect' , 'last one') :
        a2point = 10
        total = a1point + a2point
        print('Your total score is ' + str(total) + ' points 👍')

    else :
        a2point = 0
        total = a1point + a2point 
        print('Your Score is ' + str(total) + ' points.' )

else :
    print('OK 😊 Never Mind') 


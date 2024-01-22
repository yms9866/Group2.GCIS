def my_birthday():
    print('Hey I am going to tell you your birth day. please enter the approprate data for the following questions.')
    i = input('What is your name? ')
    age = int(input('Your age in days '))
    j = age%365
    a = 365 - j
    f = a//30
    k = int(input('What is the date today? '))
    x = input('And month ')
    if x == 'January':
        z = 0 + f
    elif x == 'February':
        z = 1 + f
    elif x == 'March':
        z = 2 + f
    elif x == 'April':
        z = 3 + f
    elif x == 'May':
        z = 4 + f
    elif x == 'June':
        z = 5 + f
    elif x == 'July':
        z = 6 + f
    elif x == 'August':
        z = 7 + f
    elif x == 'September':
        z = 8 + f
    elif x == 'October':
        z = 9 + f
    elif x == 'November':
        z = 10 + f
    elif x == 'December':
        z = 11 + f
    g = a-f*30
    h = k + g
    if h > 30:
        s = h - 30
    
    print(i+', '+ 'your birth day is in','2024',str(s)+'th of',x+'.')

my_birthday()
def my_birthday():
    print('Hey I am going to tell you your birth day. please inter the approprate data for the following questions.')
    i = input('What is your name? ')
    age = int(input('Your age '))
    j = 2024 - age
    c = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    l = c[3]
    k = input('What is the date today? ')
    print(i+', '+ 'your birth day is in',j,str(k)+'th of',l+'.')

my_birthday()


   
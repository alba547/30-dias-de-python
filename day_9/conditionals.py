import compileall


age = input(30)
if age >= 18:
    print ('You are old enough to learn to drive.')
age = input(15)
if age < 18:
    print ('You need 3 more years to learn to drive.')  #1

my_age = input(16)
your_age = input(30)
print(f'I am{your_age - my_age} older than you') if your_age > my_age else print (f'You are {my_age - your_age} older than me') #2

a = 4
b = 3
if a > b : 
    print('a is greater than b')
elif a < b :
        print ('a is smaller than b')
else :
    print('a is equal to b') #3
mark = int(input('Un número entre 1 y 100'))
if 80 <= mark <= 100:
    score = 'A'
    print('A')
elif 70 <= mark <= 79:
    score = 'B'
    print('B')
elif 60 <= mark <= 69:
    score = 'C'
    print('C')
elif 50 <= mark <= 59:
    score = 'D'
    print('D')
else :
    score = 'F'
    print('F')  #1

if 'September' or 'October' or 'November':
    print('The season is Autumn.')
if 'December' or 'January' or 'February':
    print('The season is Winter')
if 'March' or 'April' or 'May':
    print('The season is Spring')
if 'June' or 'July' or 'August':
    print('The season is autumn')  #2

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = int(input('Una fruta'))
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    print(list.append(fruit))
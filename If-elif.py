score = input("Please Enter your Score: ")
score = int(score)

if score < 10:
    print('Fail!')
elif 10 < score <= 12:
    print('Low')
elif 12 < score <= 15:
    print('Mid')
elif 15 < score <= 17:
    print('Good')
elif 17 < score <= 20:
    print('Excellent')
else : print('The score entered is incorrect')

# -------------------------------------------------- 
clock = input("Please Enter Clcok: ")
clock = int(clock)

if 6 < clock <= 7:
    print('good morning!')
elif 7 < clock <= 8:
    print('Go to work!')
elif 8 < clock <= 13:
    print('Hellooooooooooo!')
elif 13 < clock <= 15:
    print('good job')
elif clock > 24 or clock < 0:
    print('The time entered is incorrect!')
else : print('By')

# -------------------------------------------------- 
x = 32
m = x/(x+1)

# -------------------------------------------------- 

b = 8 
a = 4 
c = 2

d = (b**2) - 4*(a*c)

# -------------------------------------------------- 

x = 4
y = 7
n = (x+y)/(2*x+8)+1/2

# -------------------------------------------------- 

x1 = (-b +(b**2 - 4*a*c)**0.5)/(2*a)

# -------------------------------------------------- 

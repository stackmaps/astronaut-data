#A for loop is traditionally used to run a block of code a set number of times, rather than until a condition is done.
    #Examples:

for x in range(0, 10):
    print(x)

colors = ['red', 'blue', 'yellow']

for x in colors:
    print(x)

#Run a for loop that prints your name 10 times.




#Conditions are used in Python to check if something is True or False.
#You can use the built-in Python operators if and else to do so.
    #Examples:

password = 'random_text'
if password == 'random_text':
    print('Correct Password')
else:
    print('Incorrect Password')

today = 'Friday'
tomorrow = 'Sunday'
if today == 'Friday':
    print('Today is Friday')
elif today == 'Sunday':
    print('Today is Sunday')
else:
    print('Today is not Friday or Sunday')

a = 1
b = 2
if a+b == 3:
    print('a+b=3')
if a==1 and b==2:
    print('a=1 and b=2')
if a==1 or b==1:
    print('a=1 or b=1')


#Write an if statement that prints all numbers in between 0 and 100 that are divisible by 5.
    #You can determine divisibility using the %, which returns the remainder of a quotient. For example, 25%5=0 and 26%5=1.




#Functions can be used to perform certain operations easily. They follow the syntax below.

def addition(argument1, argument2):
    return argument1 + argument2

#This function takes in 2 arguments and returns the sum of the two numbers.

#Not all functions take in arguments, for example:
def hello():
    print('Hello!')

#This is how you call functions with or without arguments.
print(addition(5, 10))
hello()


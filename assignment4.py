#  ASSIGNMENT ON RECURSSIONS

# This COUNTUP function is a recurssive function that takes a parameter(m)
# and checks if the value of the parameter is equal to 0, if it is false,
# it then prints the value (n) and then perform a recurssion by
# adding 1 to the value until it meets the if n == 0 condition which will then
# print BLASTOFF to the console.
def countup(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

# This COUNTDOWN function is a recurssive function that takes a parameter(m)
# and checks if the value of the parameter is less than or equal to 0, if it is false,
# it then prints the value (n) and then perform a recurssion by
# subtracting 1 to the value until it meets the if n <= 0 condition which will then
# print BLASTOFF to the console.
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

# number_choice is a variable which serves as an arguement that is being passed to the COUNTDOWN AND COUNTUP functions,
# This variable/arguement takes a USER KEYBOARD INPUT and assigns it to it self
number_choice = input('Enter number: ')

# This is a conditional statement which checks the value of the user input and checks if it is a positive or negative number,
# If it is a positive number, it then carry out the if condition and carries out COUNTUP function if it is a negative number.
# The int() method is used to convert the user input to an integer so as to prevent runtime error(TYPE-ERROR)
if int(number_choice) >= 0:
     countdown(int(number_choice))
else:
     countup(int(number_choice))

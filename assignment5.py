# ASSIGNMENT ON RUNTIME ERROR

# This user_name variable takes in the  input of a user which will be in a 'STRING FORMAT'.
user_name = input('What is your username?: ')
# It then perform this basic operation with the user input which will eventually result to a TYPEERROR which is a RUNTIME ERROR.
# This error will happen because we are trying to deduct an integer
# from a string which is not possible to work, which then results in TYPE ERROR
# due to the different data type of both arguements
print(user_name - 1)

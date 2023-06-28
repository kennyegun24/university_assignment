# function to calculate the circumference and it takes one parameter
def print_circum(radius):
    # the circumference variable is assigned the final result after the basic operatioin has been done
    circumference=2 * 3.14159 * radius
    # This then print out the final result
    print(f"The circumference of the radius is {circumference}")

# Calling the function and passing different parameters
print_circum(300)
print_circum(140)
print_circum(20)

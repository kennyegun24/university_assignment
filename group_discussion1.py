# CHAINED CONDITIONAL
x = 10
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")


# NESTED CONDITIONAL
x = 10
y = 5
if x > 5:
    if y > 10:
        print("Both x and y are greater than their.")
    else:
        print("x is greater than 5, but y is not greater than 10.")
else:
    print("x is not greater than 5.")


# AVOID DEEP NESTED CONDITIONS
def check_voting_eligibility(age, is_citizen, is_registered):

    if age < 18:

        return "You must be at least 18 years old to vote."

    if not is_citizen:

        return "You must be a citizen to vote."

    if not is_registered:

        return "You are not registered to vote."

    return "You are eligible to vote."

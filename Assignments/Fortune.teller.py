def fortune_teller():
    print("I am the fortune teller")
    print("I will needs to get your numbers")


def get_number():
    try:
        lucky_number= int(input(" What is your lucky number"))
    except ValueError:
        (" That is not a number, try again")

import random


def function_check():
    luck = random.random()
    if luck < 0.5:
        print("Sorry")
    else:
        print("Congratulations")


function_check()

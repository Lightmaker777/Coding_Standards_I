def check_arguments(**kwargs):
    # Checking arguments before the conditional
    first_five_true = all(value is True for value in list(kwargs.values())[:5])
    last_five_false = all(
        value is False for value in list(kwargs.values())[5:])

    if first_five_true and last_five_false:
        print("ok")  # arguments are ok
    else:
        print("not ok")


check_arguments(
    arg1=True, arg2=True, arg3=True, arg4=True,
    arg5=True, arg6=False, arg7=False, arg8=False,
    arg9=False, arg10=False)

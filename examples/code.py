# import the datetime to show current date and time
import datetime

def my_function(x):
    """purpose of this function is to increase the given parameter by one

    Parameters
    ----------
    x : int
        a numeric value that will be increased by one

    Returns
    -------
    int
        increases parameter 'x' by one and returns the result from the function
    """

    return x + 1


# print current date and time
print(datetime.datetime.now())

# declare a variable as 'name' and assign some text into it
name = "Jani Immonen"

# print the contents of the 'name' variable
print(name)

# call the function
value = my_function(100)
print(value)

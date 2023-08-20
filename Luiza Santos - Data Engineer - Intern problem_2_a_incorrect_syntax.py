# Luiza Santos - Data Engineer - Intern
# Problem 2.a: Given a string made of opening and closing brackets, how to check if its syntax is OK? 
# Examples: ()(()()) is correct, ()))) is not, )( is not

def syntax_checker(string):
    """
    Decide whether the syntax of a string is correct

    Parameters: 
    string: string containing only parenthesis

    Returns:
    Boolean, True if the syntax is good and False if the syntax is bad

    Examples:
    syntax_checker("())))") # False closed too soon
    syntax_checker("()(()())") # True syntax is good
    syntax_checker("((())") # False open bracket left over

    """
    # start the number of open_brackets as 0
    open_brackets = 0
    # loop over all parenthesis in string
    for i in string:
        # increase counter if it's an open parenthesis
        if i == "(":
            open_brackets += 1
        # decrease counter if it's a closed parenthesis
        elif i == ")":
            open_brackets -= 1
        # if at any point you close a parenthesis without a match, return False
        if open_brackets < 0:
            return False
    # if nothing is left over, the syntax is good, return True
    if open_brackets == 0:
        return True
    # if there's an open parenthesis left over, return False
    return False

    
incorrect = "())))"
print(incorrect)
print(syntax_checker(incorrect))

correct = "()(()())"
print(correct)
print(syntax_checker(correct))

incorrect = "(abc)d)))"
print(incorrect)
print(syntax_checker(incorrect))

correct = "(ba)(n(a)(na))"
print(correct)
print(syntax_checker(correct))
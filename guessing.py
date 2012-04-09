def prompt_from_terminal(prompt):
    """prompt user for input from terminal with string prompt"""
    while True:
        yield input(prompt)

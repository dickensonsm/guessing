import unittest


def prompt_from_terminal(prompt):
    """prompt user for input from terminal with string prompt"""
    while True:
        yield input(prompt)

def prompt_n_times(prompt, n):
    for answer in prompt_from_terminal(prompt):
        yield answer


class MyTest(unittest.TestCase):

    def test_prompt_n_times(self):
        self.assertEqual(len(list(prompt_n_times("Guess: ", 0))),
                         0)
        self.assertEqual(len(list(prompt_n_times("Guess: ", -1))),
                         0)
        self.assertEqual(len(list(prompt_n_times("Guess: ", 1))),
                         1)
        self.assertEqual(len(list(prompt_n_times("Guess: ", 2))),
                         2)
        return
        



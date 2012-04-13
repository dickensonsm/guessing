import unittest
import itertools


def prompt_from_terminal(prompt):
    """prompt user for input from terminal with string prompt"""
    while True:
        yield input(prompt)

def prompt_n_times(guesses, n):
    """yield the first n items in guesses"""
    for answer in guesses:
        yield answer


class MyTest(unittest.TestCase):

    def test_prompt_n_times(self):
        self.assertEqual(len(list(prompt_n_times(itertools.count(), 0))),
                         0)
        self.assertEqual(len(list(prompt_n_times(itertools.count(), -1))),
                         0)
        self.assertEqual(len(list(prompt_n_times(itertools.count(), 1))),
                         1)
        self.assertEqual(len(list(prompt_n_times(itertools.count(), 2))),
                         2)
        return
        



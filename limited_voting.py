#players = ("affiliated", "with_preferences", "neutral")

players = (
    "affiliated1",
    "affiliated2",
    "affiliated3",
)

strategies1 = (
    ("vote_for_yourself", 1), 
    ("vote_for_yourself_and_pay", 1),
    ("vote", 2), 
    ("vote", 3),
)

strategies2 = (
    ("vote", 1),
    ("vote_for_yourself", 2), 
    ("vote_for_yourself_and_pay", 2),
    ("vote", 3),
)

strategies3 = (
    ("vote", 1),
    ("vote", 2),
    ("vote_for_yourself", 3), 
    ("vote_for_yourself_and_pay", 3),
)

from itertools import product

multiplied_strategies = list(product(
    strategies1,
    strategies2,
    strategies3,
))

def calculate_payoffs(multiplied_strategies):
    r = {}
    return r
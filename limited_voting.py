#players = ("affiliated", "with_preferences", "neutral")

players = (
    "affiliated1",
    "affiliated2",
    "affiliated3",
)

strategies1 = ("vote_for_yourself", "vote2", "vote3", "vote_for_yourself_and_pay")
strategies2 = ("vote1", "vote_for_yourself", "vote3", "vote_for_yourself_and_pay")
strategies3 = ("vote1", "vote2", "vote_for_yourself", "vote_for_yourself_and_pay")

from itertools import product

multiplied_strategies = list(product(
    strategies1,
    strategies2,
    strategies3,
))

def calculate_payoffs(multiplied_strategies):
    r = {}
    return r
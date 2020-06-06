#players = ("affiliated", "with_preferences", "neutral")

players = (
    "affiliated1",
    "affiliated2",
    "affiliated3",
    "with_preferences1",
    "with_preferences2", 
    "with_preferences3",
    "neutral",
)


strategies = ("vote1", "vote2", "vote3")

from itertools import product

multiplied_strategies = list(product(
    strategies,
    strategies,
    strategies,
    strategies,
    strategies,
    strategies,
    strategies,
))

def calculate_payoffs(multiplied_strategies):
    r = {}
    return r
#players = ("affiliated", "with_preferences", "neutral")

players = (
    "affiliated1",
    "affiliated2",
    "affiliated3",
)

strategies1 = (
    ("vote_for_yourself", 1, "pay"), 
    ("vote_for_yourself", 1, "cheat"),
    ("vote", 2, "pay"), 
    ("vote", 2, "cheat"), 
    ("vote", 3, "pay"),
    ("vote", 3, "cheat"),
)

strategies2 = (
    ("vote", 1, "pay"), 
    ("vote", 1, "cheat"),
    ("vote_for_yourself", 2, "pay"), 
    ("vote_for_yourself", 2, "cheat"), 
    ("vote", 3, "pay"),
    ("vote", 3, "cheat"),
)

strategies3 = (
    ("vote", 1, "pay"), 
    ("vote", 1, "cheat"),
    ("vote", 2, "pay"), 
    ("vote", 2, "cheat"), 
    ("vote_for_yourself", 3, "pay"),
    ("vote_for_yourself", 3, "cheat"),
)

from itertools import product

multiplied_strategies = list(product(
    strategies1,
    strategies2,
    strategies3,
))

#print(multiplied_strategies)

def calculate_payoffs(multiplied_strategies):    
    r = {}
    for strategies in multiplied_strategies:

        v = {1:0,2:0,3:0}

        for strategy in strategies:
            v[strategy[1]] += 1

        hstrategies = map(lambda x: x[0], strategies)

        winner = -1
        #winner = 1

        for k in v.keys():
            if v[k] > 1:
                winner = k
        
        if winner != -1:
            if strategies[winner-1][2] == "pay":
                pay = 1
            else:
                pay = 0
            payoff = {}

            for k in v.keys():
                if winner == k:
                    if pay == 1:
                        payoff["affiliated" + str(k)] = 2
                    else:
                        payoff["affiliated" + str(k)] = 3
                else:
                    if pay == 1:
                        payoff["affiliated" + str(k)] = 1
                    else:
                        payoff["affiliated" + str(k)] = 0
        else:
            payoff = {
                "affiliated1": 0,
                "affiliated2": 0,
                "affiliated3": 0,
            }

        r[strategies] = payoff
    return r

payoffs = calculate_payoffs(multiplied_strategies)

from primitivegametheory.nash_equilibrium import check_nash_equilibrium

for k in multiplied_strategies:
    if(check_nash_equilibrium(multiplied_strategies, payoffs, k, players)):
    #if True:
        print(k)
        print("")
        print(payoffs[k])
        print("")
        print("")
        print(check_nash_equilibrium(multiplied_strategies, payoffs, k, players))
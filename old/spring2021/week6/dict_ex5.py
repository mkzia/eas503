######################################################
# dict_ex5.py
# Simulate two dice. Print the total, theoretical/expected probability, 
# and simulated probability
# input: the number of simulations
# https://socratic.org/questions/what-is-the-expected-value-of-the-sum-of-two-rolls-of-a-six-sided-die
# Total     Simulated Percent     Expected Percent 

# 2                      2.76                 2.78
# 3                      5.57                 5.56
# 4                      8.34                 8.33
# 5                      11.1                11.11
# 6                     13.83                13.89
# 7                     16.68                16.67
# 8                      13.9                13.89
# 9                      11.1                11.11
# 10                     8.36                 8.33
# 11                     5.57                 5.56
# 12                     2.79                 2.78


import random

def simulate_two_dice(no_simulations):
    random.seed()
    expected = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36,


    }
    sim_dict = {}
    for no in range(no_simulations):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        total = dice1 + dice2

        if total not in sim_dict:
            sim_dict[total] = 0

        sim_dict[total] += 1

    # sim_dict2 {}
    # for total, count in sim_dict.items():
    #     sim_dict2[total] = count/no_simulations

    sim_dict_p = {total: round(count/no_simulations*100, 3) for total, count in sim_dict.items()}

    print('Total'.ljust(6), 'Simulated Percent'.rjust(25), 'Expected Percent'.rjust(25))
    for total in range(2, 13):
        print(
            str(total).ljust(6),
            str(sim_dict_p[total]).rjust(25),
            str(round(expected[total]*100,3)).rjust(25)
        )

    
simulate_two_dice(10000)


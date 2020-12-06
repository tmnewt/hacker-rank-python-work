# https://www.hackerrank.com/challenges/luck-balance/problem
#
# A person believes they can accumulate luck if they lose at programming contests.
#
#   If they lose any event they gain amount of luck L 
#   If they win an event they lose amount of luck L
#     The amount of luck L varies from contest to contest.
#
# Each contest is considered either important, or not important.
#   Given a limited number of important loses, defined as k, 
#   what is the maximum luck they could accumulate?
#
#
#
#
#
# Some immediate observations:
#   This is obviously a maximization problem...
#   All non-important competitions can immediately be considered losses
#       This will assist in maximizing the value of luck.
#
#   The important thing is to minimize the expenditure of luck.
#   This means winning the lowest value contests.
#
# The simplest method would be to filter each entry by important and non-important.
# In fact only important entries need to be remembered. Non-important can be
# ignored after adding their value to the total luck value.
# As for the important entries, store them in a new list and then bubble sort them based on
# value. Then sum the K top values with the current total luck value and subtract 
# the sum of the 'wins' entries


def luckBalance(k, contests):
    important = []
    total = 0
    for contest in contests:
        if contest[1] == 0:
            total += contest[0]
        else:
            important.append(contest[0])
    important = sorted(important, reverse=True)
    front = important[:k]
    back = important[k:]

    return sum(front, total) - sum(back)

test = [
    [13, 1],
    [10, 1],
    [9, 1],
    [8, 1],
    [13, 1],
    [12, 1],
    [18, 1],
    [13, 1]
]

print(luckBalance(5, test))
# find the max amount to splurge on 2 different items 
# without going over limit
# print int result

# Must purchase 2 different items.
# if no possible way to spend without going over limit print -1


keyboards = [3, 1, 4, 2, 5]
usbs = [5, 1, 8]
budget = 3

def getMoneySpent(keyboards, drives, b):
    splurge = -1
    for key in keyboards:
        for usb in usbs:
            if ((key + usb) <= budget) and ((key + usb) > splurge):
                splurge = key + usb

    return splurge

print(getMoneySpent(keyboards, usbs, budget))
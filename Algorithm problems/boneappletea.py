# https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=internal-search

test_bill = [3, 10, 2, 9]
k_value = 1
b_value = 7

def bonAppetit(bill, k, b):
    new_bill = bill.copy()
    new_bill.pop(k)
    if sum(new_bill)/2 != b:
        print(b - int(sum(new_bill)/2))

    else:
        print('Bon Appetit')

bonAppetit(test_bill, k_value, b_value)
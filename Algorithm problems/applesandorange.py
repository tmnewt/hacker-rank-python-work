start = 7
end = 11

a_tree = 5
b_tree = 15


apples_fallen = [2, 2, 1]
oranges_fallen = [5, -6, -7, -8]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_distance = []
    for i in apples:
        a_distance.append(a+i)
    
    b_distance = []
    for i in oranges:
        b_distance.append(b+i)
    
    a_count = 0
    b_count = 0
    for i in a_distance:
        if i >= s and i <= t:
            a_count += 1
    for i in b_distance:
        if i >= s and i <= t:
            b_count += 1

    print(a_count)
    print(b_count)

countApplesAndOranges(start, end, a_tree, b_tree, apples_fallen, oranges_fallen)
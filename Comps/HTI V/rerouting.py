# if a value equals it's 1-indexed index then the node is referencing itself
# example: [1, 2, 3, 4]
# oherwise think of the index as the node and its value as the pointer to the next node (based on 1-indexed)
# example: [2, 3, 4, 1, 5]
# is 1(2) -> 2(3) -> 3(4) -> 4(1) with 5 by iteslf
# making 1 change here is the minimum amount of work
# could have 5(n but not 5) or 4(5)

# another example [3, 3, 3, 4, 4, 4] 
# is node 1 and 2 lead to 3 and 3 leads to itself 
# meanwhile nodes 5 and 6 lead to 4 and 4 leads to itself.

# if none are linked then the minimum is always n - 1 

def getMinConnectionChange(connections):
    # connections are directional which makes this much easier
    pass 
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque  # pronounced 'deck' which is short for 'double-ended queue'

# actual problem solution

if __name__ == '__main__':
    n = int(input())
    deck = deque()
    for _ in range(n):
        line = input()
        try:
            instruction, value = line.split()
        except:
            instruction = line; value = None
        if instruction == 'append': deck.append(value)
        if instruction == 'appendleft': deck.appendleft(value)
        if instruction == 'pop': 
            try: deck.pop()
            except IndexError: pass
        if instruction == 'popleft': 
            try: deck.popleft()
            except IndexError: pass
    print(' '.join(list(deck)))





# some examples of usage:
# https://docs.python.org/3/library/collections.html#collections.deque
# holy cow. Deque is so much faster than lists when it comes to poping from either the front or the end of the deck

# Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

d = deque()
d.append(3); d.append(2); d.append(9)
print(d)
d.appendleft(200)
print(d)


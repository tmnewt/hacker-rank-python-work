# https://www.hackerrank.com/challenges/sparse-arrays/problem

# return an integer array of the results of all queries in order.

def matchingStrings(strings: list, queries: list):
    answer = []
    for query in queries:
        counter = 0
        for text in strings:
            if query == text:
                counter += 1
        answer.append(counter)
    return answer


# https://www.hackerrank.com/challenges/grading/problem?h_r=internal-search

test = [4, 38, 44, 66, 45, 89, 92, 98, 97]

def gradingStudents(grades):
    # Write your code here
    g = []
    
    for i in grades:
        if i%5 > 2:
            if i < 38:
                g.append(i)
            else:
                g.append(5 * round(i/5))
        else:
            g.append(i)
    return g

    #for i in grades:
    #    state = False
    #    m = i%5
    #    if m > 2:
    #        state = True
    #    print(f'{i} so remainder {m}, so {state}')
    #return g

print(gradingStudents(test))


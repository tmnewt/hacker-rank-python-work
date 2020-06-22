# https://www.hackerrank.com/challenges/text-wrap/problem?h_r=internal-search

test = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

def wrap(s, max_w):
    st = ''
    for i in range(0, len(s), max_w):
        st += s[i:i+max_w]
        if i != len(s)-2:
            st += '\n'
        #print(s[i:i+max_width])
    return st


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)       


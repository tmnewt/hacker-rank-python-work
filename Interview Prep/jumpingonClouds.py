# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

test = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0] # minimum here is 5 jumps
test2 = [0, 0, 1, 0, 0, 1, 0]

def jumpingOnClouds(c : list):
    count = 0
    i = 0
    while i < len(c)-1:
        try:
            if c[i+2] == 0:
                count += 1
                i += 2
        
            else:
                count += 1
                i += 1

        except IndexError:
            count += 1
            break

    return count

print(jumpingOnClouds(test2))
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# consider the following bubble sort code:
'''for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }    
}  '''

# implement a bubble sort to sort the array in assending order:
# in the StdOUT print 3 lines
# line 1:  Array is sorted in x swaps.
# line 2:  First Element: x[first]
# line 3:  Last Element: x[last]


def countSwaps(a: list):
    count = 0
    for _ in range(len(a)):
        j = 0 
        while j < (len(a)-1):
            if a[j] > a[j+1]:
                store = a[j]
                a[j] = a[j+1]
                a[j+1] = store
                count += 1
            j += 1
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


test = [6, 4, 7, 1, 3]  
countSwaps(test)


# original test is [6, 4, 7, 1, 3]
# start for loop:
# j = 0
# swap 1:  [4, 6, 7, 1, 3]
# couple increments nothing happens
# j reaches index 2 (which holds 7) and can swap it with index 3
# swap 2:  [4, 6, 1, 7, 3]
# j increments
# swap 3:  [4, 6, 1, 3, 7]  also while loop ends so loop back
# 1 loop of the for loop completed 
# j = 0 
# nothing to swap
# j = 1
# swap 4:  [4, 1, 6, 3, 7]
# j = 2
# swap 5:  [4, 1, 3, 6, 7]
# j increments and doesn't do anything
# j resets
# swap 6:  [1, 4, 3, 6, 7]
# j = 1
# swap 7:  [1, 3, 4, 6, 7]
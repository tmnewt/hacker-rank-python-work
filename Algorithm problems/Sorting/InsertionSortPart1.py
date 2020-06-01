# https://www.hackerrank.com/challenges/insertionsort1/problem

# a single run brute force algorithm
def insertionSort1(n: int, arr: list):
    lost_boi = arr[len(arr)-1]
    for i in range(len(arr)-1, -1, -1):
        #print(f'comparing {lost_boi} to {arr[i]}')
        print(i)
        if i == 0:
            arr[i] = lost_boi
            print(' '.join(list(map(str, arr))))
            break
        if lost_boi > arr[i-1]:
            arr[i] = lost_boi
            print(' '.join(list(map(str, arr))))
            break
        else:
            arr[i] = arr[i-1]
            print(' '.join(list(map(str, arr))))



# full fledged brute force algorithm:
def insertionSort2(n: int, arr: list):
    for i in range(n-1):
        if i == n-1:
            print(' '.join(list(map(str, arr))))
            break
        elif arr[i] <= arr[i+1]:
            print(' '.join(list(map(str, arr))))
        else:
            pick = arr[i+1]
            for j in range(i+1, -1, -1):
                if j == 0:
                    arr[j] = pick
                    break
                if pick > arr[j-1]:
                    arr[j] = pick
                    break
                else:
                    arr[j] = arr[j-1]
            print(' '.join(list(map(str, arr))))

#for k in range(3, -1, -1):
#    print(k)

insertionSort2(9, [4, 5, 5, 2, 1, 6, 7, 8, 3])
print()
insertionSort2(6, [1, 4, 3, 5, 6, 2])


#insertionSort1(5, [2, 4, 6, 8, 3]) 
#print()
#insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
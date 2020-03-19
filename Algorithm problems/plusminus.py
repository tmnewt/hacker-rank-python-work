arr = [-4, 3, -9, 0, 4, 1]

# find array length

arr_len = len(arr)

pos_count = 0
neg_count = 0
zero_count = 0

for i in arr:
    if i > 0:
        pos_count += 1
    if i < 0:
        neg_count += 1
    if i == 0:
        zero_count += 1

print(format(pos_count/arr_len, '.6f'))
print(format())
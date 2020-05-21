# each day floor(recipients/2) of the recipients will like the advertisement and will
# share it with 3 friends on the following day. Assuming nobody receives the advertisement
# twice, determine how many people have liked the ad by the end of a given day,
# beginning with launch day as day 1.

# complete the function so that it returns the cumulative number of people who have
# liked the ad at a given time. 

def viralAdvertisingLong(n):
    shared = 5
    total_liked = 0
    for _ in range(n):
        likes = int(shared/2)
        total_liked += likes
        shared = likes * 3
    return total_liked

for i in range(20):
    print(viralAdvertisingLong(i))
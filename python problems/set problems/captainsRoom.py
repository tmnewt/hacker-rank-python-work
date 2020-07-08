# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

junk = int(input()) # useless stdIn line
del junk
mems = list(map(int, input().split()))

rooms = set()
roomsRepeat = set()

for mem in mems:
    if mem in rooms: 
        # means it's not the captains
        roomsRepeat.add(mem)  
    else:
        # could be either a family room or the captain's
        rooms.add(mem)
# get difference in membership.
print(rooms.difference(roomsRepeat).pop())


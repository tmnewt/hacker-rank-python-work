s = '11:05:22AM'
h = s[:2]
mm_ss = s[3:8]
am_pm = s[-2:]
if am_pm == 'PM' and int(h) < 12:
    h = int(h)+12
if am_pm == 'AM' and int(h) == 12:
    h = '00'

print(h)
print(mm_ss)
print(f'{h}:{mm_ss}')


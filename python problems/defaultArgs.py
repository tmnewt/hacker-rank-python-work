# https://www.hackerrank.com/challenges/default-arguments/problem?h_r=next-challenge&h_v=zen


# code that can't be changed
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# code that CAN be changed
def print_from_stream(num, stream=EvenStream()):
    if isinstance(stream, EvenStream):
        stream = EvenStream()
    for _ in range(num):
        print(stream.get_next())


# code that Can't be changed
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

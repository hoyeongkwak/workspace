def CustomRange2(start, end):
    current = start
    while current < end:
        yield current
        current +=1

for i in CustomRange2(1,5):
    print(i)

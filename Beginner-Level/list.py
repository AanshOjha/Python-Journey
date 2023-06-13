# Shortest way to take INPUT, SPLIT by spaces, MAP FUNC. to convert to INTEGER, SORT in ascending order then printing in 1 in a line.
num = sorted(map(int, (input().split())))
for i in num:
    print(i)

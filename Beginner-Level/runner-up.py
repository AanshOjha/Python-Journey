# Takes INPUT, SPLIT it, MAP to integer
# Convert to SET DATA TYPE, to avoid problems with repeated values. 
if __name__ == '__main__':
    n = int(input())
    arr = (sorted(set(map(int, input().split()))))
    print(arr[-2])

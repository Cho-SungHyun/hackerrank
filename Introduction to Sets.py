def average(array):
    # your code goes here
    count = 0
    array = set(array)
    avg = sum(array)/len(array)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

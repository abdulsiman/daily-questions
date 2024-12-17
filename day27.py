def find_pivot(arr):
    for i in range(1, len(arr) - 1):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return arr[i]
    return None

arr = [1, 8, 3, 6, 5, 7]
print(find_pivot(arr))

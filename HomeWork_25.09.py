def max_area(arr):
    l = 0
    r = len(arr) - 1
    max_area = 0

    while l < r:
        leng = r - l
        height = min(arr[l], arr[r])

        area = leng * height

        max_area = max(max_area, area)

        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1

    return max_area


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(arr))

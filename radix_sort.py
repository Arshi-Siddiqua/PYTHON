def radix_sort(arr):
    max_num = max(arr)
    place = 1

    while max_num // place > 0:
        counting_sort(arr, place)
        place *= 10

def counting_sort(arr, place):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        digit = (num // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // place) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

arr = [170, 45, 75, 90, 802, 24, 2, 66]

radix_sort(arr)
print("Sorted array:", arr)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array elements into 2 halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Copy data to the sorted array while comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Checking if any element was left
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage
arr = [8, 20, 14, 47, 3, 10, 55]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

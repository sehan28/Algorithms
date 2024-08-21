def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Select the pivot element (here, we are choosing the last element as the pivot)
        pivot = arr[-1]
        smaller, equal, larger = [], [], []

        # Partition the array into three parts
        for x in arr:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                larger.append(x)
        
        # Recursively apply quicksort to smaller and larger arrays
        return quick_sort(smaller) + equal + quick_sort(larger)

# Example usage
arr = [8, 20, 14, 47, 3, 10, 55, 31]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

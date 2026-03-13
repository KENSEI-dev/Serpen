def partition(arr, low, high):
    """Lomuto partition: places pivot at correct position."""
    pivot = arr[high]          # pivot is last element
    i = low - 1                # index of smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_lomuto(arr, low, high):
    """Quicksort using Lomuto partition scheme."""
    if low < high:
        pi = partition(arr, low, high)
        quicksort_lomuto(arr, low, pi - 1)
        quicksort_lomuto(arr, pi + 1, high)


# Example usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    n = len(data)
    quicksort_lomuto(data, 0, n - 1)
    print("Sorted array:", data)

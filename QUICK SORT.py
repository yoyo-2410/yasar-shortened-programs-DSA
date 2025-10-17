# Quick Sort

def quickSort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quickSort(a, low, p - 1)
        quickSort(a, p + 1, high)

def partition(a, low, high):
    pivot = a[low]
    i, j = low + 1, high
    while True:
        while i <= j and a[i] <= pivot: i += 1
        while i <= j and a[j] >= pivot: j -= 1
        if i <= j: a[i], a[j] = a[j], a[i]
        else: break
    a[low], a[j] = a[j], a[low]
    return j

print("QUICK SORT METHOD\n")
data = [int(x) for x in input("Enter the elements of a list separated by space:\n").split()]
print("\nAccepted data:", data, "\n")
print("Unsorted Array:"); print(data)
quickSort(data, 0, len(data)-1)
print("\nSorted array using quicksort in ascending order:"); print(data)

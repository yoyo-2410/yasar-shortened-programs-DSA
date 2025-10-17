# Merge Sort

def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    L, R = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(L, R)

def merge(L, R):
    m, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]: m.append(L[i]); i += 1
        else: m.append(R[j]); j += 1
    m.extend(L[i:]); m.extend(R[j:])
    return m

print('MERGE SORT METHOD\n\n')
data = [int(x) for x in input('Enter elements of a list separated by space \n').split()]
print('Accepted Data:', data, '\n')
print('Unsorted Array'); print(data)
data = merge_sort(data)
print('\nSorted Array using Merge Sort in Ascending Order:'); print(data)

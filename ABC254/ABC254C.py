
def merge_sort(array):
    print(line)
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left, right):
    merged = []
    l_i, r_i = 0,0
    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1
        if l_i < len(left):
            merged.extend(left[l_i:])
        if r_i < len(right):
            merged.extend(right[r_i:])
        return merged
    
n, k = map(int,input().split())
line = list(map(int, input().split()))
merge_sort(line)
print(line)

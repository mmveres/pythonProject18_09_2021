def bubble_sort(arr):
    global count
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            count += 1
            swap(arr, i, i+1)

def swap(arr, h, k):
    if arr[h] > arr[k]:
        temp = arr[h]
        arr[h] = arr[k]
        arr[k] = temp


def partition(arr, l, r):
    im = int((l + r) / 2)
    v = arr[im]
    i = l
    j = r
    global count
    while i <= j:
        while arr[i] < v:
            count+=1
            i+=1
        while arr[j] > v:
            count+=1
            j-=1
        if i >= j:
            break
        swap(arr,i, j)
        i+=1
        j-=1
    return j

def quicksort(arr,  l, r ):
    if l < r:
        q = partition(arr, l, r)
        quicksort(arr, l, q)
        quicksort(arr, q + 1, r)

if __name__ == '__main__':
    arr = [1,2,43,2,3,2,4,2,332,4,23,4,234,3,1,2,43,2,3,2,4,2,332,4,23,4,234,3]
    count=0
    bubble_sort(arr)
    print(count)
    arr = [1,2,43,2,3,2,4,2,332,4,23,4,234,3,1,2,43,2,3,2,4,2,332,4,23,4,234,3]
    count=0
    quicksort(arr, 0 , len(arr)-1)
    print(count)
    # count=0
    # bubble_sort(arr)
    # print(count)
    print(arr)

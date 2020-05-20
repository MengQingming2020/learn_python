#快速排序的一个版本，适用于待排序数据数值分布比较均匀的情况
#先确定待排序数据的取值范围，然后以这个取值范围的中间值作为比较基数pivot
#pivot为浮点数，自身不参与排序
#最坏情况为待排序数值分布极不均匀，如[3,2,4,10000]，其他类似快速排序

def quickSortA(arr):
    left = 0
    right = len(arr) - 1
    max_item = arr[0]
    min_item = arr[0]
    for i in arr:
        if i > max_item:
            max_item = i
        if i < min_item:
            min_item = i
    quickSort(arr, left, right, min_item, max_item)

def quickSort(arr, left, right, min_item, max_item):
    if left < right:
        t = partition(arr, left, right, min_item, max_item)
        pi = t[0]
        ppivot = t[1]
        quickSort(arr, left, pi, min_item, ppivot)
        quickSort(arr, pi + 1, right, ppivot, max_item)
        
def partition(arr, left, right, min_item, max_item):
    i = left - 1
    pivot = (min_item + max_item)/2
    for j in range(left,right + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return (i, pivot)

if __name__ == '__main__':
    arr = [3, 6, 4, 2, 9, 5, 7, 8]
    quickSortA(arr)
    print(arr)

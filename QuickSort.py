#快速排序

def partition(arr, low, high):
    """以数组arr的最后一个元素作为基数将数组分为两个部分
    参数：
        arr:待排序数组
        low:待排序部分左边第一个元素的索引
        high:嗲排序部分右边第一个元素的索引
    """
    i = low - 1
    key = arr[high] #最后一个元素做基数
    
    #将比基数key小的元素放到数组的左边
    for j in range(low,high):
        if arr[j] <= key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    #将基数key与左半部分的下一个元素交换位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def quickSort(arr, low, high):
    """快速排序
    参数：
        arr:待排序数组
        low:待排序部分左边第一个元素的索引
        high:嗲排序部分右边第一个元素的索引
    """
    if low < high:  #分区的终止条件
        pi = partition(arr, low, high)  #基数的索引位置
        quickSort(arr, low, pi - 1)     #左半部分
        quickSort(arr, pi + 1, high)    #右半部分

if __name__ == '__main__':
    arr = ['a','f','d','e','g','s','c']
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print(arr)
""" 根据王争老师在算法课14节《排序优化》中的描述
    组合运用归并排序、快速排序、插入排序
    并对快速排序进行了三处主要优化
    
    -----------三种算法的分配逻辑-------------------------------
    if 元素总个数 <= 1024:
        归并排序
    else:
        if 元素个数 > 16 and 递归深度 < log(len(arr), 2)*2 :
            快速排序
        else:
            插入排序
    ----------------------------------------------------------
"""

#排序算法的第一层判断，如果数据量较小，使用归并排序
def zsort(arr, first, last):
    if last - first <= 1024:
        merge_sort(arr, first, last)
    else:
        if first != last:
            __quick_sort(arr, first, last, __lg(last-first)*2)
            insertion_sort(arr, first, last)


#计算快速排序的递归深度限制
def __lg(value):
    power = 4
    number = 16
    while number < value:
        number *= 2
        power += 1
    return power


#普通的归并排序的主函数，不知道怎么优化
def merge_sort(arr, first, last):
    if first < last:
        middle = first + ((last - first)>>1)
        merge_sort(arr, first, middle)
        merge_sort(arr, middle+1, last)
        __merge(arr, first, middle, last)


#归并排序的辅助函数，负责合并
def __merge(arr, first, middle, last):
    i = first
    j = middle + 1
    k = 0
    tmp = [0]*(last - first + 1)

    while i <= middle and j <= last:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    start = i
    end = middle
    if j <= last:
        start = j
        end = last
    while start <= end:
        tmp[k] = arr[start]
        k += 1
        start += 1

    for i in range(0, last - first+1):
        arr[first + i] = tmp[i]


#划分快速排序与插入排序的阈值
__threshold = 16


#快速排序的递归方法；在元素个数小于阈值、或者递归深度超出限制时调用插入排序
def __quick_sort(arr, first, last, depth_limit):
    while last - first > __threshold:
        if depth_limit == 0:
            insertion_sort(arr, first, last)
            return
        depth_limit -= 1    #每一次递归要depth_limit要自减两次，所以设定depth_limit<log(len(arr), 2)*2
        cut = __parrtition(arr, first, last)
        __quick_sort(arr, cut, last, depth_limit)
        last = cut #借用while循环，通过重新设定last的值处理左侧序列，以节省递归调用开销


#快速排序的辅助函数，主要负责排序
def __parrtition(arr, first, last):

    middle = first+((last-first)>>1)

    # pivot三数取中法
    # 排列成arr[first]<=arr[last]<=arr[middle]
    if arr[first] > arr[middle]:
        arr[first], arr[middle] = arr[middle], arr[first]
    if arr[first] > arr[last]:
        arr[first], arr[last] = arr[last], arr[first]
    if arr[last] > arr[middle]:
        arr[last], arr[middle] = arr[middle], arr[last]
    pivot = arr[last]

    j = last
    while True:
        while arr[first] <= pivot:   #左侧first选一个大于pivot的数
            first += 1
        j -= 1
        while pivot <= arr[j]:   #右侧j选一个小于pivot的数
            j -= 1
        if first >= j:  #while循环的停止条件
            arr[first], arr[last] = arr[last], arr[first]   #最后将pivot的值放入正确位置
            return first    #返回pivot的位置，也即下一次切分的位置
        arr[first], arr[j] = arr[j], arr[first]     #交换两个处于不当位置的元素
        first += 1
'''
F:first  j:j   P:pivot
一开始：
    F 12    |   24  |   19  |   11  |   20  |   36  |   15  |   21  |   17   |   24  | j  20 P
first和j各自找到对应的值
      12    | F 24  |   19  |   11  |   20  |   36  |   15  |   21  |  j 17  |   24  |   20 P
交换F与j所在位置的值
      12    | F 17  |   19  |   11  |   20  |   36  |   15  |   21  |  j 24  |   24  |   20 P
继续下一轮循环
      12    |   17  |   19  |   11  |   20  | F 36  | j 15  |   21  |    24  |   24  |   20 P
交换first与j所在位置的值
      12    |   17  |   19  |   11  |   20  | F 15  | j 36  |   21  |    24  |   24  |   20 P
first,j继续前进,达到退出循环条件
      12    |   17  |   19  |   11  |   20  | j 15  | F 36  |   21  |    24  |   24  |   20 P
将pivot交换到正确位置,并返回first
      12    |   17  |   19  |   11  |   20  | j 15  | F 20 p|   21  |    24  |   24  |   36 
'''

#普通的插入排序函数，不知道怎么优化
def insertion_sort(arr, first, last):
    if first == last:
        return
    for i in range(first+1, last+1):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


#用于判断数列是否有序
def is_sorted(arr, first, last):
    while first < last:
        if arr[first] <= arr[first+1]:
            first += 1
        else:
            return False
    return True


if __name__ == '__main__':
    import random

    arr = [x for x in range(1999)] + [y for y in range(500)]
    random.shuffle(arr)
    n = len(arr)
    zsort(arr, 0, n-1)
    #print(arr)
    print(is_sorted(arr, 0, n-1))
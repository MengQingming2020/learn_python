#二分查找

#没有重复数据的二分查找，循环实现
def bsearch_a1(arr, first, last, value):
    while first <= last:
        middle = first + ((last - first)>>1)    #位移操作外要加括号，否则死循环
        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            first = middle + 1
        else:
            last = middle - 1
    else:
        return None

#没有重复数据的二分查找，递归实现
def bsearch_a2(arr, first, last, value):
    if first > last: return None
    middle = first + ((last - first)>>1)
    if arr[middle] == value:
        return middle
    elif arr[middle] < value:
        return bsearch_a2(arr, middle+1, last, value)
    else:
        return bsearch_a2(arr, first, middle-1, value)


#有重复数据
#查找第一个等于value元素的位置
def bsearch_b(arr, first, last, value):
    while first <= last:
        middle = first + ((last - first)>>1)
        
        if arr[middle] > value:
            last = middle - 1
        elif arr[middle] < value:
            first = middle + 1
        else:
            if middle == 0 or arr[middle - 1] != value:
                return middle
            else:
                last = middle - 1
    return None

#查找最后一个等于value元素的位置
def bsearch_c(arr, first, last, value):
    n =  last

    if first > last: return None

    middle = first + ((last - first)>>1)

    if arr[middle] == value:
        if middle == n or arr[middle + 1] != value:
            return middle
        else:
            return bsearch_c(arr, middle + 1, last, value)
    elif arr[middle] < value:
        return bsearch_c(arr, middle+1, last, value)
    else:
        return bsearch_c(arr, first, middle-1, value)

#查找第一个大于等于value元素的位置
def bsearch_d(arr, first, last, value):
    while first <= last:
        middle = first + ((last - first)>>1)
        
        if arr[middle] > value:
            if middle == 0 or arr[middle - 1] < value:
                return middle
            else:
                last = middle - 1
        elif arr[middle] < value:
            first = middle + 1
        else:
            if middle == 0 or arr[middle - 1] != value:
                return middle
            else:
                last = middle - 1
    return None


#查找最后一个小于等于value元素的位置
def bsearch_e(arr, first, last, value):
    n =  last

    if first > last: return None

    middle = first + ((last - first)>>1)

    if arr[middle] == value:
        if middle == n or arr[middle + 1] != value:
            return middle
        else:
            return bsearch_e(arr, middle + 1, last, value)
    elif arr[middle] < value:
        if middle == n or arr[middle + 1] > value:
            return middle
        else:
            return bsearch_e(arr, middle+1, last, value)
    else:
        return bsearch_e(arr, first, middle-1, value)


#在一个没有重复数据的循环有序数组中进行二分查找,如[4,5,6,1,2,3]
def bsearch_f(arr, first, last, value):   
    if first <= last:
        middle = first + ((last - first)>>1)
        if arr[first] == value: return first
        elif arr[last] == value: return last
        #value在区间的左序列
        elif arr[first] < value and arr[last] < value:
            if arr[middle] < value:
                a = bsearch_f(arr, first+1, middle-1, value)
                b = bsearch_f(arr, middle+1, last-1, value)
                if a: return a
                else: return b
            elif arr[middle] > value:
                return bsearch_f(arr, first+1, middle-1, value)
            else:
                return middle
        #value在区间的右序列
        elif arr[first] > value and arr[last] > value:
            if arr[middle] < value:
                return bsearch_f(arr, middle+1, last-1, value)
            elif arr[middle] > value:
                c = bsearch_f(arr, first+1, middle-1, value)
                d = bsearch_f(arr, middle+1, last-1, value)
                if c: return c
                else: return d
            else:
                return middle
        #区间是有序的
        elif arr[first] < value and arr[last] > value:
            if arr[middle] < value:
                return bsearch_f(arr, middle+1, last-1, value)
            elif arr[middle] > value:
                return bsearch_f(arr, first+1, middle-1, value)
            else:
                return middle
        #在区间之外
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    import random
    import zsort

    #在无重复数据的有序数组中查找
    arr1 = [x for x in range(10)]
    n = len(arr1)
    print('a',bsearch_a2(arr1, 0, n-1, 3))

    #在有重复数据的有序数组中查找
    arr2 = []
    for x in range(16):
        arr2.append(random.randrange(0,5,1))
    n2 = len(arr2)
    zsort.zsort(arr2, 0, n2-1)
    print(arr2)
    print('b',bsearch_b(arr2, 0, n2-1, 1))  #第一个=value
    print('c',bsearch_c(arr2, 0, n2-1, 4))  #最后一个=value
    print('d',bsearch_d(arr2, 0, n2-1, 0))  #第一个>=value
    print('e',bsearch_e(arr2, 0, n2-1, 3))  #最后一个<=value

    #在循环有序数组中查找
    arr = [5,6,7,8,9,2,3,4]
    n = len(arr)
    print('f',bsearch_f(arr, 0, n-1, 2))
    
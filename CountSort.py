#计数排序
#基本思路：使用字典的 键/值 记录 元素/出现次数

def countSort(arr):
    """计数排序
    参数：
        arr:待排序数组
    """
    #确定数组arr中元素的取值范围
    min_item = arr[0]   #最小元素
    max_item = arr[0]   #最大元素
    for i in arr:
        if i > max_item: max_item = i
        if i < min_item: min_item = i

    #初始化用来计数的字典，每一个key的value = 0
    dic = {key:0 for key in range(min_item,max_item + 1)}

    #用value统计对应key出现的次数
    for i in arr:
        dic[i] += 1

    #讲字典记录的排序结果写入原来的数组arr
    i = 0
    for key in dic:
        while dic[key] > 0:
            arr[i] = key
            i += 1
            dic[key] -= 1

if __name__ == '__main__':
    arr = [23, 19, 20, 20, 21, 21, 22, 23, 20, 19, 20]
    countSort(arr)
    print(arr)
   
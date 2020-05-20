#归并排序
def mergeSort(arr,left,right):
	"""归并排序
	参数：
		arr:待排序数组
		left:待排序部分左边第一个元素的索引
		right:待排序部分右边第一个元素的索引
	"""
	while left < right:	#分治的终止条件，每一个部分都只有一个元素
		middle = (left + right) // 2	#待排序部分中间索引
		mergeSort(arr, left, middle)	#左半部分
		right = middle + 1
		#mergeSort(arr, middle + 1, right)	#右半部分
		merge(arr, left, middle, right)	#有序合并左右两个部分

def merge(arr,left,middle,right):
	"""对数组的左右两部分有序合并
	参数：
		arr:待排序数组
		left:左索引
		middle:中间索引
		right:右索引
	"""
	#初始化索引i, j, k，临时数组tmp
	i = left
	j = middle +1
	k = 0
	tmp = [0]*(right - left + 1)

	#按照从小到大的顺序合并数组的左右两个部分到临时数组tmp
	while i <= middle and j <= right:
		if arr[i] <= arr[j]:
			tmp[k] = arr[i]
			i += 1
		else:
			tmp[k] = arr[j]
			j += 1
		k += 1
	
	#将剩余部分写入临时数组tmp
	start = i
	end = middle
	if j <= right:
		start = j
		end = right
	while start <= end:
		tmp[k] = arr[start]
		k += 1
		start += 1

	#将临时数组tmp中存储的排序结果写入原数组arr
	for i in range(0,right - left + 1):
		arr[left + i] = tmp[i]

if __name__ == '__main__':	
    arr = [3, -2, 12, -1 , 5, -6, 8]
    n = len(arr)
    mergeSort(arr,0,n - 1)
    print(arr)
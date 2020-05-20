'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

'''

class Solution:
    def search(self, nums, target):
        last = len(nums) - 1
        '''在[]中查找'''
        if last == -1 : return -1

        '''将首尾节点单独考虑，使之后的判断更清晰,也能稍稍提高这两种特殊情况的查找效率'''
        if nums[0] == target: return 0
        if nums[last] == target: return last

        '''找出第一个小于nums[0]的元素，作为分界点'''
        cut = self.find_cut(nums, 0, last)

        if nums[0] > target and nums[last] > target:    #target在右侧序列
            return self.bsearch(nums, cut, last - 1, target)

        elif nums[0] < target and nums[last] < target:  #target在左侧序列
            return self.bsearch(nums, 1, cut -1, target)

        elif nums[0] < target and nums[last] > target:  #数组nums本身是有序的'''
            return self.bsearch(nums, 1, last - 1, target)

        else:       #若nums[0] > target and nums[last] < target，说明target不在数组nums之内
            return -1

    def find_cut(self, nums, first, last):
        '''找出数组nums中第一个小于nums[0]的元素的索引，并返回'''

        while first <= last:
            middle = first + ((last - first)>>1)
            if nums[middle] > nums[first]:
                if nums[first] > nums[last]:    #在有旋转的升序数组中
                    first = middle + 1
                else:   #在没有旋转的升序数组中
                    return first

            elif nums[middle] < nums[first]:
                
                if nums[middle - 1] >= nums[first]: #如果前一个节点大于nums[first],或者前一个节点就是nums[first]
                    return middle
                else:   #若nums[middle - 1] < nums[first],说明分界点在middle左侧
                    last = middle - 1
            else:   #
                if first == last:   #只剩一个元素
                    return first 
                elif middle == first and nums[middle + 1] < nums[first]:    #只剩两个元素
                    return middle + 1
                else:   #剩余元素个数大于2的普通情况
                    return middle

    def bsearch(self, nums, first, last, target):
        '''在不存在重复元素的升序数组中二分查找target'''

        while first <= last:
            middle = first + ((last - first)>>1)
            if nums[middle] > target:
                last = middle - 1
            elif nums[middle] < target:
                first = middle + 1
            else:
                return middle
        else:
            return -1

if __name__ == '__main__':
    arr = [4,5,1]
    s = Solution()
    index = s.search(arr, 1)
    print(index)


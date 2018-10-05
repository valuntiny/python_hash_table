"""
author: Guojing Wu
date: 2018-10-4
description: this is the basic testing for hash table
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


test = Solution()

list1 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 1, 6]

print(test.singleNumber(list1))
"""1  Two Sum"""
class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


"""15.3sum"""
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        new_list=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    new_list.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif sum>0:
                    right-=1
                else:
                    left +=1
        return new_list


    
"""167. Two Sum II - Input Array Is Sorted"""
class Solution(object):
    def twoSum(self, numbers, target):
      left=0
      right=len(numbers)-1
      while left <right:
        if numbers[left]+numbers[right]==target:
            return [left+1,right+1]
        if numbers[left]+numbers[right]<target:
            left+=1
        else:
            right-=1


        
"""283. Move Zeroes"""
class Solution(object):
    def moveZeroes(self, nums):
        left=0
        right=0
        for i in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1

    
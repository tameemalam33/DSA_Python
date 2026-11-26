"""Print an array in reverse order"""
class reverse:
    def reverse_arr(self,arr):
        left=0
        right=len(arr)-1
        while left <right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
arr=list(map(int,input("enter the array : ").split(",")))
rev=reverse()
print(rev.reverse_arr(arr))

"""	Check whether an array is a palindrome"""
class Palindrome:
    def rev(self,arr):
        left=0
        right=len(arr)-1
        while left<right:
            if arr[left]==arr[right]:
                left+=1
                right-=1
                return "palindrome"

            else:
                return "not a palindrome"
arr=list(map(int,input("enter the array : ").split(",")))
p1=Palindrome()
print(p1.rev(arr))

"""	Find a pair with a given sum in a sorted array"""
class pair_index:
    def target_sum(self,x,target):
        left=0
        right=len(x)-1
        while left <right:
            sum=x[left]+x[right]
            if sum==target:
                return left,right
            elif sum>target:
                right-=1
            else:
                left+=1
arr=list(map(int,input("enter the array : ").split(",")))
target=int(input("enter the target : "))
pair1=pair_index()
print(pair1.target_sum(arr,target))


"""	Remove duplicates from a sorted array"""
class duplicates:
    def duplicate_arr(self,arr):
        left=0
        right=1
        while right <len(arr):
            if arr[left]!=arr[right]:
                left+=1
                arr[left]=arr[right]
            right += 1

        return arr[:left+1]
arr=list(map(int,input("enter array : ").split(",")))
dup=duplicates()
print(dup.duplicate_arr(arr))

"""	Move all zeros to the end"""
class mov_zeros:
    def mov_0(self,arr):
        left=0
        for right in range(len(arr)):
            if arr[right] !=0:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
        return arr
arr=list(map(int,input("enter array ").split(",")))
m1=mov_zeros()
print(m1.mov_0(arr))

arr=[0,1,1,2,2,2,2,3,4,4,5,5,6]
left=0
for right in range(len(arr)):
    if arr[left]==arr[right]:
        right+=1
    else:
        left+=1
        arr[left]=arr[right]
print(arr[:left+1])   


"""quaring the sorted array with negatives"""
"""using merge sort and twopointer technique"""
def square():
    arr=[-2,-1,0,1,2,3,4,5,6,7]
    n=[]
    p=[]
    for i in arr:
        if i<0:
            n.append(i)
        else:
            p.append(i)
    if len(n)==0:
        return [x*x for x in p]
    if len(p)==0:
        res=[x*x for x in n]
        res.reverse()
        return res
    else:
        n=[x*x for x in n][::-1]
        p=[x*x for x in p]
        res=[]
        i=j=0
        while i<len(n) and j <len(p):
            if n[i]<=p[j]:
                res.append(n[i])
                i+=1
            else:
                res.append(p[j])
                j+=1
        while i<len(n):
            res.append(n[i])
            i+=1
        while j<len(p):
            res.append(p[j])
            j+=1
    return res
print(square())

"""normal two pointer approach"""
def sortt():

    nums=list(map(int,input("enter array : ").split(",")))
    left=0
    right=len(nums)-1
    result=[0]*len(nums)
    position=len(nums)-1
    while left<=right:
        if abs(nums[left]) >= abs(nums[right]):
            result[position]=nums[left]**2
            left+=1
        else:
            result[position]=nums[right]**2
            right -=1
        position-=1
    return result

print(sortt())

"""merge sort array  basic brute force"""
def merge():
    num1=list(map(int,input("enter : ").split(",")))
    m=int(input("enter the no of elements to merge"))
    num2=list(map(int,input("enter the 2nd array ele : ").split(",")))
    n=int(input("enter the lenght of eles to merge "))
    new_arr=[]
    left=0
    right=0
    while left <m and right <n:
        if num1[left] < num2[right]:
            new_arr.append(num1[left])
            left +=1
        else:
            new_arr.append(num2[right])
            right+=1
    while left <m:
        new_arr.append(num1[left])
        left+=1
    while right <n:
        new_arr.append(num2[right])
        right +=1
    return new_arr

print(merge())

"""merge sort by optimized"""

def merge(nums1, m, nums2, n):
    left = m-1
    right = n-1
    pos=m+n-1
    while right >=0:
        if nums1[left]>nums2[right] and left >=0:
            nums1[pos]=nums1[left]
            left -=1
        else:
            nums1[pos]=nums2[right]
            right-=1
        pos -=1
    return nums1
num1=list(map(int,input("enter : ").split(",")))
m=int(input("enter the no of elements to merge"))
num2=list(map(int,input("enter the 2nd array ele : ").split(",")))
n=int(input("enter the lenght of eles to merge "))
print(merge(num1,m,num2,n))
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
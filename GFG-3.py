class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        if n>0:
            arr[:]=arr[::-1]
        return arr

r1=Solution()
arr=[1,2,3,4,5]
print(r1.reverseArray(arr))
#Reversing an array

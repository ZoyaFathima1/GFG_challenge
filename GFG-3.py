# To reverse elements in an array
class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        if n>0:
            l1=arr[::-1]
            for i in range(n):
                arr[i]=l1[i]
            return arr[i]
        return []

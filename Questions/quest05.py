"""
5. Check Subset 
Given two sets A and B. 
check whether A is subset of B ?
A is subset of B, if all elements 
of a set A are present in another set B.
"""

class Solution:
    def checkSubset(self, A, B):
        self = A.issubset(B);
        return self

def main():
    t = int(input())
    while(t>0):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a=set(a);b=set(b);
        ob = Solution()
        res = ob.checkSubset(a,b)
        print(res)
        t-=1
        
if __name__ == "__main__":
    main()

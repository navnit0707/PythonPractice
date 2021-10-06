"""
4. Find Union 
Given two sets A and B. find the Union of both the sets.
Union of two given sets A and B is a set which consists 
of all the elements of A and all the elements of B such
 that no element is repeated.
"""

class Solution:
    def Union(self, A, B):
        self = A.union(B)
        return self

def main():
    t = int(input())
    while(t>0):
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a=set(a);b=set(b);
        ob = Solution()
        res = ob.Union(a,b)
        for i in res:
            print(i,end = " ")
        print()
        t-=1
        
if __name__ == "__main__":
    main()

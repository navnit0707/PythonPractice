"""
7. Test if tuple is distinct
Given a tuple A , 
find if all elements of tuple are different or not.
"""
class Solution:
    def checkDistinct(self, A):
        #this line will first convert tupple into set
        #since set didnt store duplicates the size will be reduced
        #if dupicates there so when we compare we got diff means there is duplicate
        res=len(A) == len(set(A))
        if res:
            return "Distinct"
        
        return "Not Distinct"
#{ 
#Driver Code Starts.
def main():
    t = int(input())
    while(t > 0):
        a=tuple(map(int,input().split()))
        ob = Solution()
        res = ob.checkDistinct(a)
        print(res)
        t-=1
if __name__ == "__main__": 
    main()
#} Driver Code Ends

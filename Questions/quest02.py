""""
2. Swap The Numbers 
Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.
"""

class Solution:
    def utility(self, a, b):
        #code here
        a,b = b,a 
        print(a,b);

def main():
    t=int(input())
    while(t>0):
        a = int(input())
        b = int(input())
        oj = Solution();
        oj.utility(a, b)
        t-=1

if __name__ == "__main__":
    main()

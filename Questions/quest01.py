""""
1. TypeCast And Double It
Given an input num as a string. 
You need to typecast into an integer and double it.
"""

def utility():
    #The line below takes the input
    num=input()
    
    #Complete the syntax below. Convert num to int and double it
    ans=int(num)
    #Complete the syntax above
    
    #The line below prints the output
    print(2*ans) 

def main():
    t = int(input())
    while(t>0):
        utility()
        t-=1
if __name__ == "__main__":
    main()

""""
3. Given two integers a and b, 
you need to concatenate them so the output is ab.
"""
def utility():
    #The two lines below take input.
    a=int(input())
    b=int(input())
    
    #Complete the code below to concatenate a and b
    ans= str(a) + str(b)
    #Complete the code above to concatenate a and b
    
    #The line below prints the output.
    print(ans)

def main():
    t = int(input())
    while(t>0):
        utility()
        t-=1
if __name__ == "__main__":
    main()

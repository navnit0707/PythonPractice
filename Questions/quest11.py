#You are given two sets A and B
#we need to find whether set A  is a subset of set B .

#Python program 

for i in range(int(input())):
    m=int(input())
    x=set(list(map(int,input().split())))
    n=int(input())
    y=set(list(map(int,input().split())))
    if x.intersection(y)==x:
         print("True")
    else:
         print("False")
         

#sample input
#1
#5
#1 2 3 5 6
#9
#9 8 5 6 3 2 1 4 7
#sample output
#True

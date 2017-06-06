"""
Design an algorithm (using dynamic programming) that given an array A of n integers 
finds the length of the longest increasing subsequence of values in A. For example, 
if A = {1, 6, 3, 7}, the answer is 3.

"""

def largesub(A,B):
  if len(A)==0:
    return max(B)
  else:
    s=1
    t=A[0]
    for i in range(1,len(A)):
      if t<A[i]:
        s+=1
        t=A[i]
    B.append(s)
    A=A[1:]
    return largesub(A,B)
    
A=[6,1,2,3,4,7,8,3,0,1,2,3,1,4,2,5,3,6,3,500,7,3,8,3,9,2,10]
B=list() 
print(largesub(A,B)) #longest substring is 8, with [0,1,2,3,4,5,6,500]
      

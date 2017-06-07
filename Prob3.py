
"""
Design an algorithm (using dynamic programming) that 
given an array A of n integers finds the contiguous subarray
for which the sum of the elements is the largest.

Ex: {-5,-4,1,2,-6,-7} the largest contiguous subarray would be 1,2 
because the sum of that is 3, which is larger than any other subarray 
"""




def start_sum(A):
  return get_sum(A,1,0,0)


def get_sum(A,j,a,b):
  if j>len(A)-1:
    return a,b
  elif A[j-1]+A[j]>a+b:
    a=A[j-1]
    b=A[j]
    return get_sum(A, j+1,a,b)
  else:
    return get_sum(A,j+1,a,b)

"""Test"""

B=[-2,1,3,5,7,-5,1,-80,4,3,5,-34,-3,2,6,8,-4]

print(start_sum(B)) #output 6,8 the largest contiguous

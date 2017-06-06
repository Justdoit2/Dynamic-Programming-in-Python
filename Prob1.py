"""Design an algorithm(using dynamic programming) that gives an array A of n positive integers and an integer value v determine if there is a subset of values in A that sum to v. Ex: A={1,2,3} and v=5 will return true, and 
    if v=9 , then return false
"""





def has_subset(A,v):
  if v in A:
    return True
  elif (len(A)==0 and v>0) or v < min([t for t in A]):
    return False
  else:
    
    j=max([t for t in A if t<v])
    A.remove(j)
    return has_subset(A,v-j)

    
b=[1,2,3,8,40]
s=19
print(has_subset(b,s))

class Mergesort:
  def sort(A):
    if len(A) > 1:
      mid = len(A) / 2
      L = A[0:mid]
      R = A[mid+1:len(A)]
      sort(L)
      sort(R)
      merge(A, L, R)
    


  def merge(A, L, R):
    i = 0 #▷ Index for left subarray
    j = 0 #▷ Index for right subarray
    k = 0 #▷ Index for merged array
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        A[k] = L[i]
        i = i + 1
      else:
        A[k] = R[j]
        j = j + 1
        
      k = k + 1
      
    while i < len(L): #▷ Copy remaining elements of L
      A[k] = L[i]
      i = i + 1
      k = k + 1
  
    while j < len(R): #▷ Copy remaining elements of R
      A[k] = R[j]
      j = j + 1
      k = k + 1
  
        
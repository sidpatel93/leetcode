def selectionSort(arr):
  for i in range(0,len(arr)):
    low = i
    for j in range(i+1,len(arr)):
      if arr[low] > arr[j]:
        low = j  
    if(i != low):
      temp = arr[i]
      arr[i] = arr[low]
      arr[low] = temp
  return arr


print(selectionSort([34,22,0,2,10,19,17]))
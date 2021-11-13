def selectionSort(arr):
  for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
      if arr[j] < arr[i]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  return arr


print(selectionSort([5,6,-3,2,4,-1]))
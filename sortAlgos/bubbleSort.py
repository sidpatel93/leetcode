def bubbleSort(arr):
  # Outer loop
  for i in range(0,len(arr)):
    #inner loop
    for j in range(0,len(arr)-1-i):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  return arr

print(bubbleSort([5,6,-3,2,4,-1]))
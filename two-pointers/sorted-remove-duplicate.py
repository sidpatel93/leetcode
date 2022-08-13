def remove_duplicates(arr):
  next = 1
  for i in range(1,len(arr)):
    if(arr[next - 1] != arr[i]):
      arr[next] = arr[i]
      next += 1;
  return next

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # return  4 -> because resultant array would be [2,3,6,9]
  print(remove_duplicates([2, 2, 2, 11])) # return  2 -> because resultant array would be [2,11]


main()

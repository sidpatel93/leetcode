def merge_lists(lst1: list, lst2: list)-> list:
  ind1, ind2 = 0,0
  while ind1 < len(lst1) and ind2 < len(lst2):
    if(lst1[ind1] > lst2[ind2]):
      lst1.insert(ind1, lst2[ind2])
      ind1 += 1
      ind2 += 1
    else:
      ind1 += 1
  if ind2 < len(lst2):  
    lst1.extend(lst2[ind2:])
  return lst1


print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))
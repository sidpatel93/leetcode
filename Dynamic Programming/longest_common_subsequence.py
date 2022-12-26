def longestCommonSubstring(x,y):
  table = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
  for i in range(0,len(x)):
    for j in range(0,len(y)):
      if x[i] == y[j]:
        table[i+1][j+1] = 1 + table[i][j]
      else:
        # table[i][j] = max(table[i][j-1], table[i-1][j])
          if table[i][j+1] > table[i+1][j]:
            table[i+1][j+1] = table[i][j+1]
          else:
            table[i+1][j+1] = table[i+1][j]
  return table[len(x)][len(y)]


# print(longestCommonSubstring('BCDBCDA', 'ABECBA'))
print(longestCommonSubstring('GTXAYB', 'AGGTAB'))
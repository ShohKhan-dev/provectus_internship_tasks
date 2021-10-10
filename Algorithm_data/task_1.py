def count_connections(list1: list, list2: list) -> int:
  count = 0
  
  for i in list1:
    for j in list2: 
      if i == j:
        count += 1
  
  return count




def optimised(list1: list, list2: list) -> int:
    s = set()
    res = 0
    n = len(list1)
    m = len(list2)
    for i in range(n):
        s.add(list1[i])
    for i in range(m):
        if list2[i] in s:
            res+=1
            s.remove(list2[i])

    return res
  

arr1 = [2,5,7,6,9,4,3]
arr2 = [7,8,9,2,1,3,6,4]

print(count_connections(arr1, arr2))
print(optimised(arr1, arr2))


### Time complexity of optimised one is n+m
### where n and m are lenght of list1 and list2 respectively

### Space complexity is O(n+m)

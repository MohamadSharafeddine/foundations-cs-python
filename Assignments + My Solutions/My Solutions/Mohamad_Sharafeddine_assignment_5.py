# Selection Sort:
def selectionSort(list1):
  border = 0
  while border < len(list1) - 1:
    minIndex = border
    for i in range(border + 1, len(list1)): 
      if list1[i].lower() < list1[minIndex].lower(): # <--- Change in code
        minIndex = i
    list1[border], list1[minIndex] = list1[minIndex], list1[border]
    border += 1
  print(list1)

# Merge Sort:
def mergeSort(list1, start, end):
  list1 = list1[::-1] # <--- Change in code
  if start == end:
    return
  mid = (start + end) // 2
  mergeSort(list1, start,mid)
  mergeSort(list1, mid + 1, end)
  merge(list1, start, mid, end)

def merge(list1, start, mid, end):
  new_list = []
  ind1 = start
  ind2 = mid + 1

  while ind1 <= mid and ind2 <= end:
    if list1[ind1] < list1[ind2]:
      new_list.append(list1[ind1])
      ind1 += 1
    else:
      new_list.append(list1[ind2])
      ind2 += 1

  while ind1 <= mid:
    new_list.append(list1[ind1])
    ind1 += 1
    
  while ind2 <= end: 
    new_list.append(list1[ind2])
    ind2 += 1
  list1[start:end + 1] = new_list

# Exercise 1:
strings = ["aA", "b", "BD", "Bc", "D"]
selectionSort(strings)

# Exercise 2:
lst = [3, 5, 1, 8, -10]
mergeSort(lst, 0, len(lst) - 1)
print(lst)


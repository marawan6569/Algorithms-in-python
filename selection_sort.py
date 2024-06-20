"""
Selection sort in python
RunTime: O(N*N) -> O(N²)
"""

def find_smallest(arr):
  smallest = 0
  for i in range(len(arr)):
    if arr[i] < arr[smallest]:
      smallest = i
  return smallest


def sorter(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
  return new_arr

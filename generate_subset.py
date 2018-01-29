

# Generate all subsets of a given set
# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9


def subsets(nums):
  if nums is None: 
    return None

  subsets = [[]]   
  for n in nums:
    next = [] 
    for s in subsets:
      next.append(s + [n])
    subsets += next    
  return subsets 


def main():
    set = [3, 34, 4, 12, 5, 2]
    result = subsets(set)
    print(result)



if __name__ == '__main__':
    main()

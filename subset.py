# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.


def isSubsetSum(items, l, sum):
    if sum == 0:
        return True
    if l == 0 and sum != 0:
        return False

    if items[l - 1] > sum:
        return isSubsetSum(items, l - 1, sum);

    return isSubsetSum(items, l - 1, sum) or isSubsetSum(items, l - 1, sum - items[l - 1])


# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(items, l, sm):
    # The value of subset[i][j] will be
    # true if there is a subset of
    # set[0..j-1] with sum equal to i
    subset = [[True] * (sm + 1)] * (l + 1)

    # If sum is 0, then answer is true
    for i in range(0, l + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sm + 1):
        subset[0][i] = False

    # Fill the subset table in botton
    # up manner
    for i in range(1, l + 1):
        for j in range(1, sm + 1):
            if (j < items[i - 1]):
                subset[i][j] = subset[i - 1][j]
            if (j >= items[i - 1]):
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - items[i - 1]]

    """uncomment this code to print table
    for i in range(0,n+1) :
        for j in range(0,sm+1) :
            print(subset[i][j],end="")
    print(" ")"""

    return subset[l][sm];


def main():
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")


if __name__ == '__main__':
    main()

def quick_sort(items):
    size = len(items)
    if size < 2:
        return items
    else:
        borne = items[0]
        left = filter(lambda x: x < borne, items)
        right = filter(lambda x: x > borne, items)
        return quick_sort(left) + borne + quick_sort(right)


def binary_tree_contain(items, value):
    count = 1
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (high + low) // 2
        if value == items[mid]:
            return True, count
        elif value < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
        count += 1
    return False, count

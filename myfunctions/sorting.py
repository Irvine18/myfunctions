def bubble_sort(items):

    '''Return array of items, sorted in ascending order

    Args:
        items (array)

    Returns:
        array: sorted in ascending order

    Examples:
        >>>> sum_array([3, 1, 5, 4])
        returns [1, 3, 4, 5]

    '''

    count = 0
    for idx in range(len(items)-1):
        if items[idx] > items[idx + 1]:
            items[idx],items[idx + 1] = items[idx + 1],items[idx]
            count += 1
    if count == 0:
        return items
    else:
        return bubble_sort(items)

def merge_sort(items):

    '''Return array of items, sorted in ascending order

    Args:
        items (array)

    Returns:
        array: sorted in ascending order

    Examples:
        >>>> sum_array([3, 1, 5, 4])
        returns [1, 3, 4, 5]

        '''

    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    return items

def quick_sort(items):

    '''Return array of items, sorted in ascending order

    Args:
        items (array)

    Returns:
        array: sorted in ascending order

    Examples:
        >>>> sum_array([3, 1, 5, 4])
        returns [1, 3, 4, 5]

    '''

    if len(items) <= 1:
        return items
    else:
        return quick_sort([e for e in items[1:] if e <= items[0]]) + [items[0]]\
         + quick_sort([e for e in items[1:] if e > items[0]])

import random

def quicksort(array, left=0, right=None):
    """
    Quicksort takes a list and a lower and upper bound.
    It recursively operates on the segments of the list
    operated by the lower and upper bound.
    """
    if right == None:
        right = len(array)
    elif left >= right:
        return
    # main body
    pivot = array[left]
    i = left + 1
    for j in range(left+1, right):
        if array[j] < pivot:
            # swap array[i] and array[j]
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i-1] = array[i-1], array[left]
    quicksort(array, left, i-1)
    quicksort(array, i, right)


if __name__ == '__main__':
    fail, success = 0, 0
    for i in range(100):
        lst = [int(random.random()*100) for n in range(100)]
        #print(lst)
        s = sorted(lst)
        quicksort(lst)
        if s != lst:
            fail += 1
        else:
            success += 1
    print('succeeded {} times, failed {} times'.format(success, fail)) 

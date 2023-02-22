def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    max = -1000000000
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return None
    for item in int_list:
        if item > max:
            max = item
    return max


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 1:  # base case
        return int_list
    n = int_list[len(int_list) - 1]  # n = last value in int_list
    return [n] + reverse_rec(int_list[:-1])  # appends n to result and calls recursive func


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    if high >= low:
        middle = (low + high) // 2
        if high == low and target != int_list[middle]:  # target is not between high and low
            return None
        if int_list[middle] == target:
            return middle  # base case
        if target < int_list[middle]:
            high = middle - 1
        else:
            low = middle + 1
        return bin_search(target, low, high, int_list)  # recursive call
    else:
        return None


def reverse_list_mutate(int_list):
    '''Reverses a list, mutates the input list, returns None,
     if list is none raises value error'''
    if int_list is None:
        raise ValueError
    if len(int_list) == 1:
        return None
    count = -1
    for i in range(len(int_list) // 2):
        val = int_list[i]
        val2 = int_list[count]
        int_list[i] = val2
        int_list[count] = val
        count -= 1
    return None

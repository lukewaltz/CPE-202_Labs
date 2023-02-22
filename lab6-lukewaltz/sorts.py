import random
import time


def selection_sort(list):
    comps = 0
    for i in range(len(list)):
        # find min in unsorted lst
        min_index = i
        for j in range(i + 1, len(list)):  # compares to the right of list[i]
            comps += 1
            if list[min_index] > list[j]:  # if list[min_index] is no longer the smallest
                min_index = j  # set min index to new smallest
        # switch the compared vals
        list[i], list[min_index] = list[min_index], list[i]
    nums = list
    return comps


def insertion_sort(list):
    comps = 0  # comparisons
    for i in range(1, len(list)):  # because index 0 should be None
        val = list[i]
        j = i - 1  # j prev spot in list
        while j >= 0:
            comps += 1  # comparison made
            if val < list[j]:
                # if val is less than previous switch them
                newj = j + 1
                list[newj] = list[j]
                list[j] = val
                j -= 1
            else:
                break  # ends current loop
    nums = list
    return comps


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time()
    #comps = selection_sort(randoms)
    # insertion sort
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()

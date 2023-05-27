# 1. The file contains all of the integers between 1 and 10,000 (inclusive,
# with no repeats) in unsorted order.  The integer in the ith row of the file gives you the ith entry of an input array.

# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you
# know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three
# different pivoting rules.

# You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length m,
# you should simply add m-1 to your running total of comparisons.  (This is because the pivot element is compared to
# each of the other m-1 elements in the subarray in this recursive call.)

# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can
# give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly
# as it is described in the video lectures (otherwise you might get the wrong answer).


# For the first part of the programming assignment, you should always use the first element of the array as the pivot
# element.

# ANSWER:
# 162085

# 2.
# Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot
# element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
# Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (
# i.e., the last element) with the first element.

# ANSWER:
# 164123

def main():
    # Read file
    with open('QuickSort.txt', 'r') as f:
        data = f.readlines()

    # Convert to list of integers
    data = [int(x.strip()) for x in data]

    # QuickSort
    comparisons = quick_sort(data, 0, len(data) - 1)
    print(comparisons)

def quick_sort(arr, l, r):
    if l >= r:
        return 0
    p = partition(arr, l, r)
    return r - l + quick_sort(arr, l, p - 1) + quick_sort(arr, p + 1, r)

def partition(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1

if __name__ == '__main__':
    main()
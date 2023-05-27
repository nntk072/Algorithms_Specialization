# The file contains all of the integers between 1 and 10,000 (inclusive,
# with no repeats) in unsorted order.  The integer in the ith row of the file gives you the ith entry of an input array.


# 3.
# Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary
# motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that
# are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first,
# middle, and final elements of the given array.  (If the array has odd length it should be clear what the "middle"
# element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6
# 7,  the "middle" element is the second one ---- 5 and not 6!)  Identify which of these three elements is the median
# (i.e., the one whose value is in between the other two), and use this as your pivot.  As discussed in the first and
# second parts of this programming assignment, be sure to implement Partition exactly as described in the video
# lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since
# 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

# SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three
# candidate elements.  You should NOT do this.  That is, as in the previous two problems, you should simply add m-1
# to your running total of comparisons every time you recurse on a subarray with length m.

# ANSWER:
# 138382


def main():
    # Read file
    with open("QuickSort.txt", "r") as f:
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
    # Find the middle index of arr (round down if odd)
    m = (l + r) // 2

    # Add the values of l, m, r in the list
    values = [arr[l], arr[m], arr[r]]

    # Find the median of the list values
    median = sorted(values)[1]
    # Swap the median with the first element in easy language
    if median == arr[m]:
        arr[m], arr[l] = arr[l], arr[m]
    elif median == arr[r]:
        arr[r], arr[l] = arr[l], arr[r]
    else:
        pass

    # Set the pivot to the median
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i - 1


if __name__ == "__main__":
    main()

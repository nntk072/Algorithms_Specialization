# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
# entry of an array. Because of the large size of this array, you should implement the fast divide-and-conquer
# algorithm covered in the video lectures. The numeric answer for the given input file should be typed in the space
# below. So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas
# / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

"""
# Traditional way
def main():
    # Read file IntegerArray.txt
    with open("IntegerArray.txt", "r") as f:
        arr = f.readlines()
    arr = [int(x.strip()) for x in arr]
    print(count_inversions(arr))

def count_inversions(arr):
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv
"""


def main():
    with open("IntegerArray.txt", "r") as f:
        arr = f.readlines()
    arr = [int(x.strip()) for x in arr]
    n = len(arr)
    u = count_inversions(arr)
    print(u[1])


def count_inversions(arr):
    n = len(arr)
    if n == 1:
        return arr, 0

    left = arr[: n // 2]
    right = arr[n // 2 :]

    left, left_inv = count_inversions(left)
    right, right_inv = count_inversions(right)
    split, split_inv = count_split_inv(left, right)

    return split, left_inv + right_inv + split_inv


def count_split_inv(left, right):
    split_inv = 0
    i = 0
    j = 0
    sorted_arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        elif left[i] == right[j]:
            sorted_arr.append(left[i])
            sorted_arr.append(right[j])
            i += 1
            j += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            split_inv += len(left) - i
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr, split_inv


if __name__ == "__main__":
    main()

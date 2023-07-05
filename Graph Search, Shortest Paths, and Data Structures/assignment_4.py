# The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash
# table applications).
#
# The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your
# array of integers, with the ith row of the file specifying the ith entry of the array.
#
# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are
# distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition
# to the algorithm from lecture.)
#
# Write your numeric answer (an integer between 0 and 20001) in the space provided.
#
# OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example,
# you could compare performance under the chaining and open addressing approaches to resolving collisions.
#
# ANSWER: 427

# Format of file: 2sum.txt
#
# 68037543430
# -21123414637
# 56619844751
# ...
#

import time
import numpy as np


def main():
    # Read the input file 2sum.txt
    with open("2sum.txt") as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]

    start_time = time.time()
    count = 0
    content = set(content)
    for t in range(-10000, 10001):
        for x in content:
            if t - x in content and t - x != x:
                count += 1
                break
    print("Method: set")
    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))

    # Or another way to do it using numpy
    start_time = time.time()
    count = 0
    content = np.array(content)
    for t in range(-10000, 10001):
        if np.any(np.in1d(t - content, content)):
            count += 1
    print("Method: numpy")
    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))

    # Or another way to do it using brute force
    start_time = time.time()
    count = 0
    for t in range(-10000, 10001):
        for i in range(len(content)):
            for j in range(i + 1, len(content)):
                if content[i] + content[j] == t:
                    count += 1
                    break
    print("Method: brute force")
    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

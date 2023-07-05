# The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap
# applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this
# as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is
# defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk;
# if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)
#
# In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That
# is, you should compute (m1+m2+m3+⋯+m10000)mod10000.
#
# OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the
# algorithm.
#
# ANSWER: 1213
#
# Format of file: Median.txt
#
# 6331
# 2793
# 1640
# 9290
# 225
# 625
# 6195
# 2303
# ...

import heapq

def main():
    # Read the input file Median.txt
    with open('Median.txt') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]

    # Code without algorithm
    sum = 0
    for i in range(1, len(content) + 1):
        if i % 2 == 0:
            sum += sorted(content[:i])[i // 2 - 1]
        else:
            sum += sorted(content[:i])[(i + 1) // 2 - 1]
    print(sum)
    print(sum % 10000)

    # Code with algorithm
    # sum = 0
    # min_heap = []
    # max_heap = []
    # for i in range(1, len(content) + 1):
    #     if len(max_heap) == 0 or content[i - 1] < -max_heap[0]:
    #         heapq.heappush(max_heap, -content[i - 1])
    #     else:
    #         heapq.heappush(min_heap, content[i - 1])
    #     if len(max_heap) > len(min_heap) + 1:
    #         heapq.heappush(min_heap, -heapq.heappop(max_heap))
    #     elif len(min_heap) > len(max_heap):
    #         heapq.heappush(max_heap, -heapq.heappop(min_heap))
    #     if i % 2 == 0:
    #         sum += -max_heap[0]
    #     else:
    #         sum += -max_heap[0]
    # print(sum%10000)

if __name__ == '__main__':
    main()
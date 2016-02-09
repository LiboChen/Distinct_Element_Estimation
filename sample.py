__author__ = 'libochen'

import math
import csv
from random import randint
from decimal import Decimal
import pylab as pl
import heapq
f0 = 12375


def estimate(M, a, b, mydict):
    min_value = M
    for key in mydict:
        hashed_value = (a * key + b) % M
        if hashed_value < min_value:
            min_value = hashed_value
    # print "min val is ", min_value
    if min_value == 0:
        result = 'infinity'
    else:
        result = Decimal(M) / Decimal(min_value) - 1
    return result

# find 5 smallest numbers
# def estimate(M, a, b, mydict):
#     h = []
#     for key in mydict:
#         hashed_value = (a * key + b) % M
#         val = - hashed_value
#         if len(h) < 10:
#             heapq.heappush(h, val)
#         else:
#             heapq.heappush(h, val)
#             heapq.heappop(h)
#
#     min_value = -min(h) / 10
#     # print "min val is ", min_value
#     if min_value == 0:
#         result = 'infinity'
#     else:
#         result = Decimal(M) / Decimal(min_value) - 1
#     return result

nips_dict = {}


# find 5 smallest numbers
with open('nips-word-stream.csv', 'rb') as nips_file:
    reader = csv.reader(nips_file)
    for row in reader:
        num = int(row[0])
        if num not in nips_dict:
            nips_dict[num] = 1
        else:
            nips_dict[num] += 1

    res_list = []
    for i in range(0, 10000):
        a = randint(0, 100002)
        b = randint(0, 100002)
        cur = estimate(100003, a, b, nips_dict)
        #print cur
        if cur == 'infinity':
            res_list.append(100000000)
        else:
            res_list.append(math.log(Decimal(cur) / Decimal(f0)))

    # plot the distribution of res_list
    for ele in range(0, len(res_list)-1):
        print res_list[ele]
    histogram = sorted(res_list)
    bins = range(-10, 10)
    n, bins, patches = pl.hist(histogram, bins, normed=1, histtype='bar', rwidth=0.8)
    pl.show()
    pl.savefig('bb.png')

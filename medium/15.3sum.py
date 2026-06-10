# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # O(n^2 log n) | Time Limit Exceeded

        # hashmap = {}
        # res = set()
        #
        # for i, num in enumerate(nums):
        #     hashmap[num] = i
        #
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if i == j:
        #             continue
        #         num3 = -(num1 + num2)
        #         if num3 in hashmap:
        #             k = hashmap[num3]
        #             if i != k and j != k:
        #                 triplet = tuple(sorted([num1, num2, num3]))
        #                 res.add(triplet)
        #
        # return [list(triplet) for triplet in res]
        
        # O(n^2) | WATCHED SOLUTION

        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0: break
            if i > 0 and n == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
# @leet end

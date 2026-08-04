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
    def search(self, nums: List[int], target: int) -> bool:

        # O(n) | FIRST APPROACH

        # l = 0
        # r = len(nums) - 1
        #
        # while l <= r:
        #     if nums[l] == target or nums[r] == target:
        #         return True
        #     else:
        #         l += 1
        #         r -= 1
        # return False

        # O(logn)

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1

            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
        
# @leet end

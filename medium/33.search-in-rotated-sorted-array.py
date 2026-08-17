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
    def search(self, nums: List[int], target: int) -> int:

        # O(logn)

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        
# @leet end

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
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # O(n)

        res = 0
        diff = float('inf')

        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                temp = nums[l] + nums[r] + nums[i]
                diff = min(diff, abs(target - temp))
                if diff == abs(target - temp):
                    res = temp 

                if temp == target:
                    return temp
                elif temp < target:
                    l += 1
                else:
                    r -= 1

        return res
        
# @leet end

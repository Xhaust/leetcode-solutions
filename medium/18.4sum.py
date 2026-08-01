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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # O(n^3) | WATHED SOLUTION

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                l = j + 1
                r = n - 1
                
                while l < r:
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                            
                        l += 1
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
                        
        return res
 
# @leet end

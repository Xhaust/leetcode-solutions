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
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # O(n^2)
        
        ans = []
        def backtrack(i, path):
            if i == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i + 1, path)

            path.pop()
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return ans

# @leet end

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
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:

        # O(n)

        counts = Counter()
        max_freq = 0
        l = 0
        
        for r, num in enumerate(nums):
            counts[num] += 1
            max_freq = max(max_freq, counts[num])
            
            if (r - l + 1) - max_freq > k:
                counts[nums[l]] -= 1
                l += 1
                
        return max_freq
        
# @leet end

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
    def findDuplicate(self, nums: List[int]) -> int:

        # O(n) | FIRST SOLUTION (SLOW)

        # seen = defaultdict(int)
        #
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen[num] += 1
        # return 0

        # O(n) | WATCHED SOLUTION

        fast = slow = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        
# @leet end

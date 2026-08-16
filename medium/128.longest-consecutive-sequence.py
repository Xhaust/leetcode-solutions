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
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n)

        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        longest = 1
        
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1
                temp = num
                while temp + 1 in nums_set:
                    temp += 1
                    streak += 1
                    longest = max(streak, longest)

        return longest
        
# @leet end

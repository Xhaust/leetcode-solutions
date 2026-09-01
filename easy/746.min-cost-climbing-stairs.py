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
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # # O(2^n) | FIRST ATTEMPT
        #
        # @lru_cache(None)
        # def step(i):
        #     if i >= len(cost):
        #         return 0
        #
        #     return cost[i] + min(step(i + 1), step(i + 2))
        #
        # return min(step(0), step(1))
        
        # O(n) | SECOND ATTEMPT

        memo = {}

        def step(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = min(step(i + 1), step(i + 2)) + cost[i]

            return memo[i]

        return min(step(0), step(1))
        
        # O(n) | WATCHED SOLUTION

        down1, down2 = 0, 0

        for i in range(len(cost) - 1, -1, -1):
            curr = cost[i] + min(down1, down2)
            down2 = down1
            down1 = curr

        return min(down1, down2)
        
# @leet end

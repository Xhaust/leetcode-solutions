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
    def largestRectangleArea(self, heights: List[int]) -> int:

        # O(n) | WATCHED SOLUTION

        stk = []
        ans = 0

        for i, height in enumerate(heights):

            while stk and height < heights[stk[-1]]:
                prev_i = stk.pop()
                
                # Added width to my solution, before was i - prev_i
                width = i if not stk else i - stk[-1] - 1
                ans  = max(width * heights[prev_i], ans)
            stk.append(i)
            
        while stk:
            prev_i = stk.pop()
            width = len(heights) if not stk else len(heights) - stk[-1] - 1
            ans  = max(width * heights[prev_i], ans)
        return ans
# @leet end

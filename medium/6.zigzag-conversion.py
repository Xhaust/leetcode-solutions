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
    def convert(self, s: str, numRows: int) -> str:
        
        # FIRST ATTEMPT
        # l = 0
        # r = diff = (numRows - 1) * 2
        # res = s[0]
        #
        # while len(res) < len(s):
        #     if r < len(s):
        #         res += s[r]
        #         r += diff
        #     else:
        #         diff -= 2
        #         l += 1
        #         r = l + diff
        #         res += s[l]
        # return res
        
        # SECOND ATTEMPT
        #
        # res = ""
        # row = 0
        # it = 0
        # curr = 0
        # direction = True
        #
        # while len(res) < len(s):
        #     if it == row:
        #         res += s[curr]
        #
        #     curr += 1
        #
        #     if curr == len(s):
        #         row += 1
        #         curr = row
        #         it = 0
        #         direction = True
        #         continue
        #
        #     if direction:
        #         it += 1
        #     else:
        #         it -= 1
        #
        #     if it == 0 or it == numRows - 1:
        #         direction = not direction
        #
        # return res

        # O(n) | WATCHED SOLUTION

        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        n = len(s)
        cycle_len = 2 * numRows - 2

        for row in range(numRows):
            for curr in range(row, n, cycle_len):
                res.append(s[curr])
                
                if 0 < row < numRows - 1:
                    diagonal_curr = curr + cycle_len - 2 * row
                    if diagonal_curr < n:
                        res.append(s[diagonal_curr])

        return "".join(res)

# @leet end

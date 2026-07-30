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
    def longestOnes(self, nums: List[int], k: int) -> int:

        # O(n)

        l = 0
        max_size = k
        counter0 = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                counter0 += 1

            if counter0 > k:
                while nums[l] != 0:
                    l += 1
                l += 1
                counter0 -= 1

            size = 1 + r - l
            max_size = max(size, max_size)

        return max_size
        
# @leet end

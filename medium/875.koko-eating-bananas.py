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
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # O(n log m) | WATCHED SOLUTION

        def valid_check(k: int) -> bool:
            hours_spent = 0
            for pile in piles:
                hours_spent += ceil(pile / k)
            return hours_spent <= h

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2
            if valid_check(mid):
                r = mid
            else:
                l =  mid + 1

        return l
        
# @leet end

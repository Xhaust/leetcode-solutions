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
    def maxArea(self, height: List[int]) -> int:

        # O(n)

        l,r = 0, len(height) - 1
        max = 0

        while l < r:
            curr = (r - l) * min(height[l],height[r])
            if curr > max:
                max = curr
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max
# @leet end

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
    def maxProduct(self, nums: List[int]) -> int:

        # O(n)

        dp_max = [float('-inf')] * (len(nums))
        dp_min = [float('inf')] * (len(nums))
        dp_max[0], dp_min[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])

        return max(dp_max)
        
# @leet end

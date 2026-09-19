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
    def maxProduct(self, nums: list[int]) -> int:

        # O(n) | WATCHED OPTIMAL SOLUTION

        res = nums[0]
        min_num = 1
        max_num = 1

        for num in nums:
            tmp = max_num * num
            max_num = max(num * max_num, num * min_num, num)
            min_num = min(num * min_num, tmp, num)
            res = max(res, max_num)

        return res
        
# @leet end

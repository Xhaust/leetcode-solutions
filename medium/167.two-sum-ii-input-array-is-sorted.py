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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n)

        l = 0
        r = len(numbers) - 1

        while l < r:
            two_sum = numbers[l] + numbers[r]

            if two_sum == target:
                return [l + 1, r + 1]
            if two_sum < target:
                l += 1
            else:
                r -= 1
        
# @leet end

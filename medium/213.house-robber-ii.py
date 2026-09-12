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
    def rob(self, nums: List[int]) -> int:

        # O(n)

        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, nums):
        one = 0
        two = 0

        for num in nums:
            curr = max(two, one + num)
            one = two
            two = curr

        return two

        
# @leet end

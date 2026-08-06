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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # O(2^n)

        res = []

        def backtrack(state, total, start):
            if total > target:
                return

            if total == target:
                res.append(list(state))
                return

            for i in range(start, len(candidates)):
                state.append(candidates[i])
                backtrack(state, total + candidates[i], i)
                state.remove(candidates[i])

        backtrack([], 0, 0)

        return res
            
# @leet end

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
    def generateParenthesis(self, n: int) -> List[str]:

        # O(4n/nsqrt(n))

        ans = []

        def backtrack(path, l, r):
            if len(path) == n * 2:
                if l == r:
                    ans.append("".join(path))

            if l < n:
                path += "("
                backtrack(path, l + 1, r)
                path.pop()

            if r < l:
                path += ")"
                backtrack(path, l, r + 1)
                path.pop()

        backtrack([], 0, 0)
        return ans

# @leet end

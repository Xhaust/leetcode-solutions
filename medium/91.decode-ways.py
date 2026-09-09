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
    def numDecodings(self, s: str) -> int:

        # O(n) | TOP DOWN APPROACH

        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            res = dfs(i + 1)

            if i + 1 < len(s):
                decimal = s[i:i+2]
                if "10" <= decimal <= "26":
                    res += dfs(i + 2)

            memo[i] = res

            return res

        return dfs(0)

        
# @leet end

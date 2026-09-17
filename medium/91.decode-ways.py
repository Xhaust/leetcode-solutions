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

        # O(n) | TOP DOWN APPROACH (WATCHED SOLUTION)

        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            memo[i] = res
            return res
        
        return dfs(0)
        
# @leet end

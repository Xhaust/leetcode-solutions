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
    def partition(self, s: str) -> List[List[str]]:

        # O(n!) | WATCHED SOLUTION

        res = []
        part = []

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(part[:])
                return 

            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    part.append(s[i:j + 1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)

        return res
        
# @leet end

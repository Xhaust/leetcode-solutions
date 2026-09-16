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
    def longestPalindrome(self, s: str) -> str:

        # O(n)

        start = 0
        max_len = 1

        def is_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1
            

        for i in range(len(s)):
            len1 = is_palindrome(i, i)
            len2 = is_palindrome(i, i + 1)

            curr = max(len1, len2)

            if curr > max_len:
                max_len = curr
                start = i - (curr - 1) // 2

        return s[start : start + max_len]

            
# @leet end

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

        longest = 0
        res = ""

        for i, char in enumerate(s):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res


        
# @leet end

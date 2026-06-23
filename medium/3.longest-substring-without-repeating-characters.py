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
    def lengthOfLongestSubstring(self, s: str) -> int:

        # O(n)

        l = maxLength = 0
        seen = {}

        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1
            maxLength = max((r - l) + 1, maxLength) 
            seen[s[r]] = 1

        return maxLength
        
# @leet end

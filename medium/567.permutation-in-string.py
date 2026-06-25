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
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # O(n)

        l = 0
        permutation = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == permutation:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            window[s2[l]] -= 1
            l += 1
            if window == permutation:
                return True

        return False

        
# @leet end

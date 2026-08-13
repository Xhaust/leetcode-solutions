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
    def letterCombinations(self, digits: str) -> List[str]:

        # O(3^n)

        res = []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(state, i):
            if len(state) == len(digits):
                combination = "".join(state)
                if combination not in res:
                    res.append(combination)
                return

            for letter in mapping[digits[i]]:
                state.append(letter)
                backtrack(state, i + 1)
                state.pop()

        backtrack([], 0)

        return res
        
# @leet end

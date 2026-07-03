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
    def calPoints(self, operations: List[str]) -> int:

        # O(n)

        stk = []
        res = 0

        for op in operations:
            match op:
                case "+":
                    stk.append(stk[-1] + stk[-2])
                case "D":
                    stk.append(stk[-1] * 2)
                case "C":
                    stk.pop()
                case _:
                    stk.append(int(op))

        while stk:
            res += int(stk.pop())

        return res

# @leet end

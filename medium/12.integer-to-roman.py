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
    def intToRoman(self, num: int) -> str:
        
        # O(n)

        res = []

        thousandth = num // 1000
        hundredth = (num // 100) % 10
        tenth = (num // 10) % 10
        unit = num % 10


        for _ in range(thousandth):
            res.append("M")

        if hundredth == 9:
            res.append("CM")
        elif hundredth == 4:
            res.append("CD")
        elif hundredth < 4:
            for _ in range(hundredth):
                res.append("C")
        else:
            res.append("D")
            for _ in range(hundredth - 5):
                res.append("C")

        if tenth == 9:
            res.append("XC")
        elif tenth == 4:
            res.append("XL")
        elif tenth < 4:
            for _ in range(tenth):
                res.append("X")
        else:
            res.append("L")
            for _ in range(tenth - 5):
                res.append("X")

        if unit == 9:
            res.append("IX")
        elif unit == 4:
            res.append("IV")
        elif unit < 4:
            for _ in range(unit):
                res.append("I")
        else:
            res.append("V")
            for _ in range(unit - 5):
                res.append("I")
        
        return "".join(res)



# @leet end

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
    def addBinary(self, a: str, b: str) -> str:

        # O(n)

        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        res = ""

        while p1 >= 0 or p2 >= 0 or carry:
            digit_a = int(a[p1]) if p1 >= 0 else 0
            digit_b = int(b[p2]) if p2 >= 0 else 0

            current_bit = digit_a ^ digit_b ^ carry
            res = str(current_bit) + res

            carry = digit_a & digit_b | digit_a & carry | digit_b & carry

            p1 -= 1
            p2 -= 1

        return res
        
# @leet end

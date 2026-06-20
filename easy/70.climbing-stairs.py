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
    @cache
    def climbStairs(self, n: int) -> int:
        
        # O(n) | WATCHED SOLUTION

        if n <= 2:
            return n
        else: return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
# @leet end

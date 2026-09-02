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
    def climbStairs(self, n: int) -> int:

        # O(n)

        one, two = 1, 1
        curr = 1

        for num in range(n - 1, 0, -1):
            curr = one + two
            two = one
            one = curr

        return curr
        
# @leet end

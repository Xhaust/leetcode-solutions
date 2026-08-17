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
    def maxProfit(self, prices: List[int]) -> int:

        # O(n)

        res = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(price, min_price)
            res = max(price - min_price, res)

        return int(res)
        
# @leet end

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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(nlogk)

        count = Counter(nums)
        count.most_common(k)
        res = []

        for num in count.most_common(k):
            res.append(num[0])

        return res
        
# @leet end

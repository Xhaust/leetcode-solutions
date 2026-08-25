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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # O(n+p) | WATCHED SOLUTION

        pre_map = defaultdict(list)
        visit = set()

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True
            
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)

            pre_map[crs] = []

            return True

        for crs in range(numCourses):
           if not dfs(crs):
               return False

        return True


        
# @leet end

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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # O(nm) | WATCHED SOLUTION

        res = []
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()

        def dfs(r, c, visited, prev):
            if ((r,c) in visited or
                r < 0 or c < 0 or r == rows or c == cols or
                heights[r][c] < prev):
                return

            visited.add((r, c))
            for df, dc in directions:
                row, col = df + r, dc + c
                dfs(row, col, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
                
                
        
# @leet end

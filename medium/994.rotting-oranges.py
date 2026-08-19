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
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # O(mn) | FIRST APPROACH
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # directions = ((1, 0),(-1, 0),(0, 1),(0, -1))
        # minutes = 0
        #
        # def bfs(r, c):
        #     q = deque()
        #     q.append((r,c))
        #     visited.add((r, c))
        #     levels = -1
        #
        #     while q:
        #         levels += 1
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             r, c = dr + row, dc + col
        #             if (r in range(rows) and
        #                 c in range(cols) and
        #                 grid[r][c] == 1 and
        #                 (r, c) not in visited):
        #                 grid[r][c] = 2
        #                 q.append((r, c))
        #                 visited.add((r, c))
        #     return levels
        #
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 2 and (r, c) not in visited:
        #             minutes = bfs(r, c)
        #
        # return minutes

        # O(mn) | WATCHED SOLUTION

        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0),(-1, 0),(0, 1),(0, -1))
        q = deque()
        fresh_oranges = 0
        minutes = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        while q:
            minutes += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh_oranges -= 1

        return minutes if fresh_oranges == 0 else -1
        
# @leet end

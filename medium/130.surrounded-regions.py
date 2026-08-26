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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # O(mn)

        rows, cols = len(board), len(board[0])
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visit.add((r, c))

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row in range(1, rows - 1) and
                    col in range(1, cols - 1) and
                    (row, col) not in visit and
                    board[row][col] == 'O'):
                    dfs(row, col)

        for r in range(rows):
            for c in range(cols):
                if ((r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and 
                    board[r][c] == 'O' and (r, c) not in visit):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and
                (r, c) not in visit):
                    board[r][c] = 'X'

# @leet end

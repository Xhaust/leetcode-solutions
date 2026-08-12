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
    def exist(self, board: List[List[str]], word: str) -> bool:

        # O(mn3^l) | WATCHED SOLUTION

        def backtrack(idx, i, j):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]:
                return False

            char = board[i][j]
            board[i][j] = '#'

            seen = (
                backtrack(idx + 1, i + 1, j) or
                backtrack(idx + 1, i - 1, j) or
                backtrack(idx + 1, i, j + 1) or 
                backtrack(idx + 1, i, j - 1)
            )

            board[i][j] = char

            return seen


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(0, i, j):
                    return True

        return False
        
# @leet end

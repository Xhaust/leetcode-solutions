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
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # O(n^2) | FIRST ATTEMPT

        # column = [[]]
        # for i, row in enumerate(board):
        #     for j, box in enumerate(row):
        #         column[j].append(box)
        #
        #     row = Counter(row)
        #
        #     element, cnt = row.most_common(2)[1]
        #     if cnt > 1:
        #         return False
        #
        # for i, col in enumerate(column):
        #
        #     Counter(col)
        #
        #     element, cnt = col[i].most_common(2)[1]
        #     if cnt > 1:
        #         return False
        #
        # return True

        # O(1)

        subboxes = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]

        for i, row in enumerate(board):
            for j, box in enumerate(row):
                if box == ".":
                    continue
                columns[j].append(box)
                rows[i].append(box)
                if i // 3 < 1:
                    if j // 3 < 1:
                        subboxes[0].append(box)
                    elif j // 3 >= 2:
                        subboxes[2].append(box)
                    else:
                        subboxes[1].append(box)
                elif i // 3 >= 2:
                    if j // 3 < 1:
                        subboxes[6].append(box)
                    elif j // 3 >= 2:
                        subboxes[8].append(box)
                    else:
                        subboxes[7].append(box)
                else:
                    if j // 3 < 1:
                        subboxes[3].append(box)
                    elif j // 3 >= 2:
                        subboxes[5].append(box)
                    else:
                        subboxes[4].append(box)
            if len(rows[i]) == 0:
                continue
            row_counter = Counter(rows[i])
            element, counter = row_counter.most_common(1)[0]
            if counter > 1:
                return False

        for column in columns:
            if len(column) == 0:
                continue
            column_counter = Counter(column)
            element, counter = column_counter.most_common(1)[0]
            if counter > 1:
                return False

        for subbox in subboxes:
            if len(subbox) == 0:
                continue
            subbox_counter = Counter(subbox)
            element, counter = subbox_counter.most_common(1)[0]
            if counter > 1:
                return False

        return True

# @leet end

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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # O(n) | FIRST ATTEMPT
        #
        # queue = deque([root])
        #
        # while queue:
        #
        #     level_size = len(queue)
        #
        #     for _ in range(level_size):
        #         node = queue.popleft()
        #
        #         if node.left:
        #             queue.append(node.left)
        #             if node.left.val >= node.val:
        #                 return False
        #
        #         if node.right:
        #             queue.append(node.right)
        #             if node.right.val <= node.val:
        #                 return False
        #
        # return True

        # O(n)

        def dfs(node, low, high):

            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            low = min(node.val, low)
            high = max(node.val, high)

            l = dfs(node.left, low, node.val)
            r = dfs(node.right, node.val, high)

            return l and r

        return dfs(root, float("-inf"), float("+inf"))

        
# @leet end

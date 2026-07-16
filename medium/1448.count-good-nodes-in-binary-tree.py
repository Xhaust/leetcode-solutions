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
    def goodNodes(self, root: TreeNode) -> int:
        
        # O(n)

        def dfs(node, max_num):
            if node is None:
                return 0

            if node.val >= max_num:
                max_num = node.val
                return 1 + dfs(node.left, max_num) + dfs(node.right, max_num)
            else:
                return dfs(node.left, max_num) + dfs(node.right, max_num)

        return dfs(root, float(-inf))
        
# @leet end

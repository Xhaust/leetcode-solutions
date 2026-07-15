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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # O(n)

        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res
        
# @leet end

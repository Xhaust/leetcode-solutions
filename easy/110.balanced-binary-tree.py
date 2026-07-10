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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # O(n) | FIRST ATTEMPT

        # if root is None:
        #     return True
        #
        # def max_height(node: Optional[TreeNode]) -> int:
        #     if node is None:
        #         return 0
        #
        #     l = max_height(node.left)
        #     r = max_height(node.right)
        #
        #     return 1 + max(l, r)
        #
        # return max_height(root.left) - max_height(root.right) <= 1

        # O(n)

        def check_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            l = check_height(node.left)
            if l == -1:
                return -1
                
            r = check_height(node.right)
            if r == -1:
                return -1
            
            if abs(l - r) > 1:
                return -1
                
            return 1 + max(l, r)
        
        return check_height(root) != -1
        
# @leet end

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # O(nm)

        if root is None or subRoot is None:
            return False

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        
# @leet end

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # O(n) | WATCHED SOLUTION

        self.max_diameter = 0
      
        def calculate_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
          
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
          
            current_diameter = left_height + right_height
          
            self.max_diameter = max(self.max_diameter, current_diameter)
          
            return 1 + max(left_height, right_height)
      
        calculate_height(root)
      
        return self.max_diameter
        
# @leet end

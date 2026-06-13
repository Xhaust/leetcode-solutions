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
    def trap(self, height: List[int]) -> int:

        # O(n + log n)

        # l, r = 0, 1
        # trapped = curr = 0
        # maxHeight = [0,0]
        #
        # while r < len(height):
        #     if height[r] < height[l]:
        #         curr += height[l] - height[r]
        #         if height[r] > maxHeight[0]:
        #             maxHeight[0] = height[r]
        #             maxHeight[1] = r
        #     else: 
        #         trapped += curr
        #         l = r
        #     r += 1
        # if maxHeight[0] < height[l]:
        #     height[l] = maxHeight[0]
        #     r = l + 1
        #     while r < maxHeight[1]:
        #         trapped += height[l] - height[r]
        #         r += 1
        #
        # return trapped
        
        # O(n)

        l, r = 0, len(height) - 1
        maxL = maxR = 0
        trapped = 0

        while l < r:
            if height[l] > maxL:
                maxL = height[l]
            if height[r] > maxR:
                maxR = height[r]
            if height[l] < maxL:
                trapped += maxL - height[l]
            if height[r] < maxR:
                trapped += maxR - height[r]
            if height[l] < height[r]:
                l += 1
            else: r -= 1

        return trapped
# @leet end

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
class RandomizedSet:

    # O(1)

    def __init__(self):
        self.nums = []
        self.i = {}
        

    def insert(self, val: int) -> bool:
        if val in self.i:
            return False
        self.nums.append(val)
        self.i[val] = len(self.nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.i:
            return False
        self.nums[self.i[val]] = self.nums[-1]
        self.i[self.nums[-1]] = self.i[val]
        self.nums.pop()
        del self.i[val]
        return True
        

    def getRandom(self) -> int:
        i = randint(0, len(self.nums) - 1)
        return self.nums[i]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @leet end

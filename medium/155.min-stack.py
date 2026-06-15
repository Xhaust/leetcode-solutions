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
class MinStack:

    # O(1)

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        elif value <= self.getMin():
            self.minStack.append(value)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end

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
    def numDecodings(self, s: str) -> int:

        # O(n) | WATCHED SOLUTION

        if s[0] == '0':
            return 0

        one, two = 1, 1

        for i in range(1, len(s)):
            curr = 0
            
            if s[i] != '0':
                curr += two

            decimal = int(s[i-1:i+1])
            if 10 <= decimal <= 26:
                curr += one

            if curr == 0:
                return 0
            
            one = two
            two = curr

        return two
            
# @leet end

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
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # O(n) | WATCHED SOLUTION

        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        while heap or queue:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1

                if count < 0:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time
        
# @leet end

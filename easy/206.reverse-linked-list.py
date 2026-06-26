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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # O(n) | FIRST TRY

        # dummy = ListNode(0)
        # dummy.next = head
        # curr = dummy
        # stk = []
        #
        # while curr.next:
        #     stk.append(curr.next.val)
        #     curr = curr.next
        #
        # curr = dummy
        # while curr.next and stk:
        #     curr.next.val = stk.pop()
        #
        # return dummy.next

        # O(n) | WATCHED SOLUTION

        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        
# @leet end

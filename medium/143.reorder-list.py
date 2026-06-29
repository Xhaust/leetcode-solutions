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
    def reorderList(self, head: Optional[ListNode]) -> None:

        # O(n) | WATCHED SOLUTION

        fast = slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        half2 = slow.next
        slow.next = None

        prev = None
        curr = half2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        reversed_half2 = prev
        half1 = head

        while reversed_half2:
            half1_nxt = half1.next
            half2_nxt = reversed_half2.next

            half1.next = reversed_half2
            reversed_half2.next = half1_nxt

            half1 = half1_nxt
            reversed_half2 = half2_nxt

        """
        Do not return anything, modify head in-place instead.
        """
        
# @leet end

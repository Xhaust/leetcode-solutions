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
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        # O(1)

        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp +=1

    def getNewsFeed(self, userId: int) -> List[int]:

        # O(nlogn) | WATCHED SOLUTION

        res = []
        max_heap = []
        
        for uId in (self.followers[userId] | {userId}):
            if uId in self.tweets:
                index = len(self.tweets[uId]) - 1
                timestamp, tweetId = self.tweets[uId][index]
                heapq.heappush(max_heap, (-timestamp, tweetId, uId, index - 1))
                
        while max_heap and len(res) < 10:
            neg_timestamp, tweetId, uId, next_index = heapq.heappop(max_heap)
            res.append(tweetId)
            
            if next_index >= 0:
                timestamp, prev_tweetId = self.tweets[uId][next_index]
                heapq.heappush(max_heap, (-timestamp, prev_tweetId, uId, next_index - 1))
                
        return res
    def follow(self, followerId: int, followeeId: int) -> None:

        # O(1)

        if followeeId != followerId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # O(1)

        self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @leet end

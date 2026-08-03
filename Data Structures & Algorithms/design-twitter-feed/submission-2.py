from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        self.followMap[userId].add(userId)

        heap = []

        # Collect all tweets
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                for tweet in self.tweetMap[followee]:
                    heap.append(tweet)

        # Convert list to heap
        heapq.heapify(heap)

        res = []

        while heap and len(res) < 10:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)
from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        maxHeap = []

        # User should follow himself
        self.followMap[userId].add(userId)

        # Put latest tweet of every followed user in heap
        for followee in self.followMap[userId]:

            if followee in self.tweetMap:

                index = len(self.tweetMap[followee]) - 1

                time, tweetId = self.tweetMap[followee][index]

                heapq.heappush(
                    maxHeap,
                    (-time, tweetId, followee, index - 1)
                )

        # Get 10 most recent tweets
        while maxHeap and len(res) < 10:

            negTime, tweetId, followee, index = heapq.heappop(maxHeap)

            res.append(tweetId)

            # Push older tweet of same user
            if index >= 0:

                time, tweetId = self.tweetMap[followee][index]

                heapq.heappush(
                    maxHeap,
                    (-time, tweetId, followee, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
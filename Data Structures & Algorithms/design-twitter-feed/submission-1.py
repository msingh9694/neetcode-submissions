from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store (-time, tweetId)
        self.tweetMap[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        minHeap = []
        res = []

        # User always follows himself
        self.followMap[userId].add(userId)

        # Add latest tweet of each followed user
        for followee in self.followMap[userId]:

            if followee in self.tweetMap:

                index = len(self.tweetMap[followee]) - 1

                time, tweetId = self.tweetMap[followee][index]

                heapq.heappush(
                    minHeap,
                    (time, tweetId, followee, index - 1)
                )

        # Extract 10 most recent tweets
        while minHeap and len(res) < 10:

            time, tweetId, followee, index = heapq.heappop(minHeap)

            res.append(tweetId)

            if index >= 0:

                nextTime, nextTweet = self.tweetMap[followee][index]

                heapq.heappush(
                    minHeap,
                    (nextTime, nextTweet, followee, index - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)
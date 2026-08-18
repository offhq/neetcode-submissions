import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets  = defaultdict(list)
        self.timer = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        all_sources = self.follows[userId] | {userId}

        for uid in all_sources:
            if uid in self.tweets:
                for timestamp, tweet_id in self.tweets[uid][-10:]:
                    heapq.heappush(heap, (timestamp, tweet_id))
                    # Keep only the 10 highest-timestamp (most recent) tweets
                    if len(heap) > 10:
                        heapq.heappop(heap)
        res = []
        while heap:
            popped = heapq.heappop(heap)[1]
            res.append(popped)
        return res[::-1]




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].discard(followeeId)
        

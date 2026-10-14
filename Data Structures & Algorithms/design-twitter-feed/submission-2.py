class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.followers[userId].add(userId)
        max_heap = []

        for followeeId in self.followers[userId]:
            if self.tweets[followeeId]:
                last_idx = len(self.tweets[followeeId]) - 1
                next_tweet_idx = last_idx - 1
                timestamp, tweetId = self.tweets[followeeId][last_idx]
                heapq.heappush(max_heap, (-timestamp, tweetId, followeeId ,next_tweet_idx))

        while max_heap and len(tweets) < 10:
            timestamp, tweetId, followeeId, next_tweet_idx = heapq.heappop(max_heap)
            tweets.append(tweetId)

            if next_tweet_idx >= 0:
                timestamp, tweetId = self.tweets[followeeId][next_tweet_idx]
                heapq.heappush(max_heap, (-timestamp, tweetId, followeeId, next_tweet_idx - 1))
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

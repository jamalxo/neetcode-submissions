class Twitter:

    def __init__(self):
        self.count = 0
        self.user_feed = {}
        self.user_follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_feed.setdefault(userId, []).append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.user_feed:
            feed += self.user_feed[userId][-10:]

        if userId in self.user_follows:
            for following in self.user_follows[userId]:
                feed+=self.user_feed[following][-10:]
        
        h = feed
        heapq.heapify(h)

        res = []

        while h and len(res) < 10:
            popped = heapq.heappop(h)
            print(popped)
            res.append(popped[1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)

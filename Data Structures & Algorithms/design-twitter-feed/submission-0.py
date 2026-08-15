class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)     # user -> tweets maxHeap [-time, tweets] UP: most rec
        self.following = defaultdict(set)   # user -> following 
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append( (self.time, tweetId) )   


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.following[userId].add(userId)
        for f in self.following[userId]:
            if f in self.tweets:    #se f ha almeno un tweet
                last = len(self.tweets[f]) - 1
                time, tweet = self.tweets[f][last]
                heapq.heappush(maxHeap, (time, tweet, f, last) ) # mi basterebbe solo time per sortare

        while maxHeap and len(res) < 10:
            time, tweet, f, last = heapq.heappop(maxHeap)
            res.append(tweet)
            if last >= 1:
                time, tweet = self.tweets[f][last-1]
                heapq.heappush(maxHeap, (time, tweet, f, last - 1)  )
        
        self.following[userId].remove(userId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

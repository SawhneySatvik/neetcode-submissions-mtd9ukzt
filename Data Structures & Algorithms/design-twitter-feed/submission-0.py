from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followers[userId].add(userId)
        for user in self.followers[userId]:
            for time, post in self.posts[user]:
                heap.append((-time, post))
        heapq.heapify(heap)
        news = []
        for i in range(min(10, len(heap))):
            time, post = heapq.heappop(heap)
            news.append(post)
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
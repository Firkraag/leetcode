class User(object):
    def __init__(self, userId):
        self.id = userId
        self.tweets = set()
        self.followees = set()
        self.followees.add(self)
    def addTweet(self, tweetId, time):
        self.tweets.add(Tweet(tweetId, time))
    
    def follow(self, user):
        self.followees.add(user)
    
    def unfollow(self, user):
        self.followees.discard(user)
        

class Tweet(object):
    def __init__(self, tweetId, time):
        self.id = tweetId
        self.time = time

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = dict()
        self.time = 1
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].addTweet(tweetId, self.time)
        self.time += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            self.users[userId] = User(userId)
        user = self.users[userId]
        tweets = [tweet for followee in user.followees for tweet in followee.tweets]
        tweets.sort(key = lambda tweet : tweet.time, reverse = True)
        return [tweet.id for tweet in tweets[:10]]
            
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].follow(self.users[followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """       
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        if followerId != followeeId:
            self.users[followerId].unfollow(self.users[followeeId])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

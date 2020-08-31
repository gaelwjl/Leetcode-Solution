// Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:
//
//
//
// postTweet(userId, tweetId): Compose a new tweet.
// getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
// follow(followerId, followeeId): Follower follows a followee.
// unfollow(followerId, followeeId): Follower unfollows a followee.
//
//
//
// Example:
//
// Twitter twitter = new Twitter();
//
// // User 1 posts a new tweet (id = 5).
// twitter.postTweet(1, 5);
//
// // User 1's news feed should return a list with 1 tweet id -> [5].
// twitter.getNewsFeed(1);
//
// // User 1 follows user 2.
// twitter.follow(1, 2);
//
// // User 2 posts a new tweet (id = 6).
// twitter.postTweet(2, 6);
//
// // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
// twitter.getNewsFeed(1);
//
// // User 1 unfollows user 2.
// twitter.unfollow(1, 2);
//
// // User 1's news feed should return a list with 1 tweet id -> [5],
// // since user 1 is no longer following user 2.
// twitter.getNewsFeed(1);
//
//


using pii = pair<int, int>;
class Twitter {
private:
    unordered_map<int, set<int>> followeesOf; // get id of the followees;
    unordered_map<int, vector<pii>> tweetsOf; // get (time, tweet id) of a user;
    int time; 
public:
    /** Initialize your data structure here. */
    Twitter():time(0){}
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        followeesOf[userId].insert(userId);
        tweetsOf[userId].push_back({time, tweetId});
        time--;
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<pii> all_tweets;
        for (int id: followeesOf[userId]){
            for (const pii tweetsid: tweetsOf[id]){
                all_tweets.push_back(tweetsid);
            }
        }
        sort(all_tweets.begin(), all_tweets.end());
        vector<int> ans;
        for (const pii tweet: all_tweets){
            ans.push_back(tweet.second);
            if (ans.size() >= 10)
                return ans;
        }
        return ans;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        followeesOf[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if (followeeId == followerId) return ;
        followeesOf[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */

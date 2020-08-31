// Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
//
// get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
// put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
//
// Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.
//
//  
//
// Follow up:
// Could you do both operations in O(1) time complexity?
//
//  
//
// Example:
//
//
// LFUCache cache = new LFUCache( 2 /* capacity */ );
//
// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.get(3);       // returns 3.
// cache.put(4, 4);    // evicts key 1.
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4
//
//
//  
//


class LFUCache {
private:
    struct CacheNode{
        int key;
        int val;
        int freq;
        list<int>::const_iterator it;
    };
    
    const int cap;
    int min_freq;
    unordered_map<int, CacheNode> n_;
    unordered_map<int, list<int>> l_;
    
    void touch(CacheNode& node){
        const int prev_freq = node.freq;
        const int freq = ++(node.freq);
        
        l_[prev_freq].erase(node.it);
        
        if (l_[prev_freq].empty() && prev_freq == min_freq){
            l_.erase(prev_freq);
            min_freq++;
        }
        
        l_[freq].push_front(node.key);
        node.it = l_[freq].cbegin();
    }
    
public:
    LFUCache(int capacity): cap(capacity), min_freq(0){}
    
    int get(int key) {
        auto u = n_.find(key);
        if (u == n_.cend())
            return -1;
        touch(u -> second);
        return u -> second.val;
    }
    
    void put(int key, int value) {
        if (cap == 0)
            return ;
        auto it = n_.find(key);
        if (it != n_.cend()){
            it -> second.val = value;
            touch(it -> second);
            return ;
        }
        if (n_.size() == cap){
            const int key_to_remove = l_[min_freq].back();
            l_[min_freq].pop_back();
            n_.erase(key_to_remove);
        }
        min_freq = 1;
        const int freq = 1;
        l_[freq].push_front(key);
        n_[key] = {key, value, freq, l_[freq].cbegin()};
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

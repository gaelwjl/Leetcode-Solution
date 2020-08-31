// Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
//
// get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
// put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
//
// The cache is initialized with a positive capacity.
//
// Follow up:
// Could you do both operations in O(1) time complexity?
//
// Example:
//
//
// LRUCache cache = new LRUCache( 2 /* capacity */ );
//
// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.put(4, 4);    // evicts key 1
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4
//
//
//  
//


class LRUCache
{
private:
    int cap_;
    list<pair<int, int>> cache_;
    unordered_map<int, list<pair<int, int>>::iterator> map_;
public:
    LRUCache(int capacity){
        cap_ = capacity;
    }

    int get(int key) {
        const auto it = map_.find(key);
        int res = -1;
        if (it != map_.end()){
            res = it -> second -> second;
            cache_.splice(cache_.begin(), cache_, it -> second);
        }
        return res;
    }
    
    void put(int key, int value) {
        const auto it = map_.find(key);
        if (it != map_.end()){
            it -> second -> second = value;
            cache_.splice(cache_.begin(), cache_, it -> second);
            return; 
        }
        if (cache_.size() == cap_){
            const auto& node = cache_.back();
            map_.erase(node.first);
            cache_.pop_back();
        }
        cache_.emplace_front(make_pair(key, value));
        map_[key] = cache_.begin();
    }

};

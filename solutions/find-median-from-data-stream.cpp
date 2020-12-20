// Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
// For example,
//
// [2,3,4], the median is 3
//
// [2,3], the median is (2 + 3) / 2 = 2.5
//
// Design a data structure that supports the following two operations:
//
//
// 	void addNum(int num) - Add a integer number from the data stream to the data structure.
// 	double findMedian() - Return the median of all elements so far.
//
//
//  
//
// Example:
//
//
// addNum(1)
// addNum(2)
// findMedian() -> 1.5
// addNum(3) 
// findMedian() -> 2
//
//
//  
//
// Follow up:
//
//
// 	If all integer numbers from the stream are between 0 and 100, how would you optimize it?
// 	If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
//
//


class MedianFinder {
    priority_queue<int> pqs;
    priority_queue<int, vector<int>, greater<>> pqm;
public:
    /** initialize your data structure here. */
    MedianFinder() {}
    
    void addNum(int num) {
        if (pqm.size() && num > pqm.top())
            pqm.push(num);
        else
            pqs.push(num); 
        
        while ( (pqm.size() && pqm.top() < pqs.top()) || pqs.size() < pqm.size()){
            auto t = pqm.top(); 
            pqm.pop();
            pqs.push(t); 
        }

        while (pqs.size() > pqm.size()){
            auto t = pqs.top(); 
            pqs.pop(); 
            pqm.push(t);
        }
    }
    
    double findMedian() {
        if (pqs.size() == pqm.size()){
            return (double) (pqs.top() + pqm.top())/2.0;
        }
        return pqm.top(); 
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

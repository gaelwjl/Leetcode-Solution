//
// Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.
//
// A subsequence of a string S is obtained by deleting 0 or more characters from S.
//
// A sequence is palindromic if it is equal to the sequence reversed.
//
// Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
//
//
// Example 1:
//
// Input: 
// S = 'bccb'
// Output: 6
// Explanation: 
// The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
// Note that 'bcb' is counted only once, even though it occurs twice.
//
//
//
// Example 2:
//
// Input: 
// S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
// Output: 104860361
// Explanation: 
// There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
//
//
//
// Note:
// The length of S will be in the range [1, 1000].
// Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
//


int memo[1001][1001][4];
class Solution {
public:
	string S;
	int MOD = 1000000007;

	int dp(int start,int end,int alpha){
		//base case
		if(start>end)return 0;
		if(start==end){
			if(S[start] == (alpha+'a') )return 1;
			return 0;
		}
		
		if(memo[start][end][alpha]!=-1)return memo[start][end][alpha];
		
		int dev=0;
		if(S[start]==S[end] && S[start]==(alpha+'a')){
			dev=2;
			for(int i=0;i<4;i++)
				dev=(dev + dp(start+1,end-1,i) )%MOD;
		}else{
			dev= (dev + dp(start,end-1,alpha))%MOD;
			dev= (dev + dp(start+1,end,alpha))%MOD;
			dev= (dev - dp(start+1,end-1,alpha))%MOD;
			if(dev<0)dev+=MOD;
		}
		
		memo[start][end][alpha]=dev;
		return dev;
	}
	
	int countPalindromicSubsequences(string _S) {
		S=_S;
		memset(memo,-1,sizeof(memo));
		int ans=0;
		
		for(int i=0;i<4;i++)
			ans= (ans + dp(0, S.size()-1, i))%MOD;
		
		return ans;        
	}
};

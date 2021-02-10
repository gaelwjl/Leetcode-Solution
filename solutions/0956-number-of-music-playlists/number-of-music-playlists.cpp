// Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  You create a playlist so that:
//
//
// 	Every song is played at least once
// 	A song can only be played again only if K other songs have been played
//
//
// Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.
//
//  
//
//
//
//
// Example 1:
//
//
// Input: N = 3, L = 3, K = 1
// Output: 6
// Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
//
//
//
// Example 2:
//
//
// Input: N = 2, L = 3, K = 0
// Output: 6
// Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
//
//
//
// Example 3:
//
//
// Input: N = 2, L = 3, K = 1
// Output: 2
// Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
//
//
//
//
//  
//
// Note:
//
//
// 	0 <= K < N <= L <= 100
//
//
//
//


class Solution {
public:
    int numMusicPlaylists(int N, int L, int K) {
        long long dp[N + 1][L + 1]; 
        long long fac[101], mod=1e9 + 7; 
        fac[0] = 1; 
        for (int i = 1; i <= 100; i++){
            fac[i] = (fac[i - 1] * i) % mod; 
        }
        for (int i = K + 1; i <= N; i++){
            for (int j = i; j <= L; j++){   
                if (i == j || i == K + 1)
                    dp[i][j] = fac[i]; 
                else
                    dp[i][j] = (dp[i - 1][j - 1] * i + dp[i][j - 1]*(i - K))%mod; 
            }
        }
        return dp[N][L];
    }
};

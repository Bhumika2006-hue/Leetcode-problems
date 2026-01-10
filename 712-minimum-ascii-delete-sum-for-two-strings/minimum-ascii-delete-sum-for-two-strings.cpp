#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();
        
        // dp[i][j] is the min ASCII sum to make s1[0...i-1] and s2[0...j-1] equal
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Base case: s2 is empty, delete all chars of s1
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i-1][0] + (int)s1[i-1];
        }
        
        // Base case: s1 is empty, delete all chars of s2
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j-1] + (int)s2[j-1];
        }
        
        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i-1] == s2[j-1]) {
                    // Characters match, no deletion cost added
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    // Delete from s1 OR delete from s2, pick minimum cost
                    dp[i][j] = min(dp[i-1][j] + (int)s1[i-1], 
                                   dp[i][j-1] + (int)s2[j-1]);
                }
            }
        }
        
        return dp[m][n];
    }
};
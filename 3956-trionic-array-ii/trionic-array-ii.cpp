class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {

        long long ans = -1e18;

        long long prev = nums[0];
        int n = nums.size();

        long long a = -1e17;
        long long b = -1e17;
        long long c = -1e17;
        for (int i = 1; i < n; i++) {
            long long new_a = -1e17;
            long long new_b = -1e17;
            long long new_c = -1e17;

            long long curr = nums[i];
            if (curr > prev) {
                new_a = max(a, prev) + curr;
                new_c = max(b, c) + curr;
            } else if (curr < prev) {
                new_b = max(b, a) + curr;
            }

            a = new_a;
            b = new_b;
            c = new_c;

            ans = max(ans, c);
            prev = curr;
        }

        return ans;
    }
};
class Solution {
public:
    int minOperations(string s, int k) {
        int n = s.size();
        int start = 0;

        for (char c : s) {
            if (c == '0') start++;
        }

        if (start == 0) return 0;

        vector<int> dist(n + 1, -1);
        set<int> evenSet, oddSet;
        queue<int> q;

        // Insert all states except start
        for (int i = 0; i <= n; i++) {
            if (i == start) continue;
            if (i % 2 == 0) evenSet.insert(i);
            else oddSet.insert(i);
        }

        q.push(start);
        dist[start] = 0;

        while (!q.empty()) {
            int m = q.front();
            q.pop();

            int c1 = max(k - n + m, 0);
            int c2 = min(m, k);

            int lnode = m + k - 2 * c2;
            int rnode = m + k - 2 * c1;

            lnode = max(0, lnode);
            rnode = min(n, rnode);

            set<int>& targetSet = (lnode % 2 == 0) ? evenSet : oddSet;

            auto it = targetSet.lower_bound(lnode);

            while (it != targetSet.end() && *it <= rnode) {
                int next = *it;
                dist[next] = dist[m] + 1;
                q.push(next);
                it = targetSet.erase(it);
            }
        }

        return dist[0];
    }
};
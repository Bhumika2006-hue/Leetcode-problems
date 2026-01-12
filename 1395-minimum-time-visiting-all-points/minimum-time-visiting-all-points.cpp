class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int totalTime = 0;
        
        // Iterate through the points starting from the second point
        for (int i = 0; i < points.size() - 1; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            int x2 = points[i+1][0], y2 = points[i+1][1];
            
            // Calculate the absolute difference in coordinates
            int dx = abs(x2 - x1);
            int dy = abs(y2 - y1);
            
            // The time taken is the maximum of the two differences
            totalTime += max(dx, dy);
        }
        
        return totalTime;
    }
};
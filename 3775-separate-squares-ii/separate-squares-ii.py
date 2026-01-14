class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 1. Coordinate Compression for X
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        m = len(sorted_x)
        
        # Lengths of intervals between compressed x-coordinates
        diffs = [sorted_x[i+1] - sorted_x[i] for i in range(m - 1)]
        
        # Segment Tree to track union length of x-intervals
        # count[v]: how many squares cover interval v
        # length[v]: total length of interval v covered by at least one square
        count = [0] * (4 * m)
        length = [0.0] * (4 * m)

        def update(v, tl, tr, l, r, add):
            if l > r: return
            if l == tl and r == tr:
                count[v] += add
            else:
                tm = (tl + tr) // 2
                update(2*v, tl, tm, l, min(r, tm), add)
                update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
            
            if count[v] > 0:
                length[v] = sorted_x[tr+1] - sorted_x[tl]
            else:
                if tl != tr:
                    length[v] = length[2*v] + length[2*v+1]
                else:
                    length[v] = 0

        # 2. Collect Y events
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        # 3. Calculate Total Union Area
        total_area = 0
        last_y = events[0][0]
        for y, type, x1, x2 in events:
            total_area += length[1] * (y - last_y)
            update(1, 0, m - 2, x_map[x1], x_map[x2] - 1, type)
            last_y = y
        
        # 4. Find the Y that splits the area in half
        target_area = total_area / 2
        current_area = 0
        last_y = events[0][0]
        
        # Reset Segment Tree for second pass
        count = [0] * (4 * m)
        length = [0.0] * (4 * m)
        
        for y, type, x1, x2 in events:
            segment_area = length[1] * (y - last_y)
            if current_area + segment_area >= target_area:
                # The line lies within this y-interval
                remaining = target_area - current_area
                return last_y + (remaining / length[1])
            
            current_area += segment_area
            update(1, 0, m - 2, x_map[x1], x_map[x2] - 1, type)
            last_y = y
            
        return float(last_y)
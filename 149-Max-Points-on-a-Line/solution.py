# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        Point.__eq__ = lambda point1, point2: (point1.x == point2.x) and (point1.y == point2.y)
        Point.__hash__ = lambda point: hash((point.x, point.y))
        Point.__repr__ = lambda point: str((point.x, point.y))
        from collections import Counter
        counter = Counter(points) 
        #print counter
        points = list(set(points))
        #print [(point.x, point.y) for point in points]
        segments = dict()
        number = dict()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                point1 = points[i]
                point2 = points[j]
                x1 = point1.x
                y1 = point1.y
                x2 = point2.x
                y2 = point2.y
                if x1 == x2:
                    pair = (float("Inf"), x1)
                else:
                    gradient = (y2 - y1) / (1.0 * x2 - x1)
                    y = y1 - gradient * x1
                    pair = (gradient, y)
                if pair in segments:
                    segment = segments[pair]
                    if point1 not in segment:
                        segment.add(point1)
                        number[pair] += counter[point1]
                    if point2 not in segment:
                        segment.add(point2)
                        number[pair] += counter[point2]
                else:
                    segments[pair] = {point1, point2}
                    number[pair] = counter[point1] + counter[point2]
        #print segments, number
        return max(number.itervalues())
                
# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
#
#  
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
#
#
#
# Example 2:
#
#
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
#
# Even you only have trees in a line, you need to use rope to enclose them. 
#
#
#  
#
# Note:
#
#
# 	All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
# 	All input integers will range from 0 to 100.
# 	The garden has at least one tree.
# 	All coordinates are distinct.
# 	Input points have NO order. No order required for output.
# 	input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#
#


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        points = map(tuple, points)
        points = sorted(set(points))
 
        # Boring case: no points or a single point, possibly repeated multiple times.
        if len(points) <= 2:
            return points

        # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        # Returns a positive value, if OAB makes a counter-clockwise turn,
        # negative for clockwise turn, and zero if the points are collinear.
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Build lower hull 
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the beginning of the other list. 
        return list(set(map(tuple, lower[:-1] + upper[:-1])))

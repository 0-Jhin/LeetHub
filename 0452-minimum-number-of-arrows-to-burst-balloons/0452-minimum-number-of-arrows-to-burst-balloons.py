class Solution(object):
    def findMinArrowShots(self, points):

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):
            # 현재 화살로 터뜨릴 수 없는 경우
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]

        return arrows
        
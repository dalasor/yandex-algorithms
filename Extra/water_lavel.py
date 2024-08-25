# Почему то не рабочее решение (pitcraft)
def isleflood(self, height: list[int]) -> int:
    maxpos = 0
    for i in range(len(height)):
        if height[i] > height[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if height[i] > nowm:
            nowm = height[i]
        ans += nowm - height[i]
    nowm = 0
    for i in range(len(height) - 1, maxpos, -1):
        if height[i] > nowm:
            nowm = height[i]
        ans += nowm - height[i]

    return ans


# Ищется максимально возможное (решение с leetcode)
def maxArea(self, height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea
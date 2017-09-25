class Solution:
    """
    @param: pages: an array of integers
    @param: k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages:
            return 0
        total = sum(pages)
        left, right = max(pages), total
        while left < right:
            mid = (left + right) / 2
            time = 0
            count = 1
            for p in pages:
                if time + p > mid:
                    count += 1
                    time = 0
                time += p
                if count > k:
                    left = mid + 1
                    break
            else:
                right = mid
        return left

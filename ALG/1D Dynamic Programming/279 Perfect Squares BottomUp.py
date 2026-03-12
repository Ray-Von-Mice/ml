class Solution:
    def isPerfectSqr(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num // 2
        while left <= right:
            mid = left + (right - left) //  2
            guess_sqr = mid * mid
            if guess_sqr == num:
                return True
            elif guess_sqr > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def numSquares(self, n: int) -> int:
        square_nums = [i for i in range(1, n + 1) if self.isPerfectSqr(i)]
        solutions = [float("inf")] * (n + 1)

        solutions[0] = 0
        for num in range(1, n + 1):
            for sqn in square_nums:
                remain = num - sqn
                if remain >= 0:
                    solutions[num] = min(1 + solutions[remain], solutions[num])
        
        return solutions[-1]
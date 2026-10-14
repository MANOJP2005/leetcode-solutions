
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""

        nines, remainder = divmod(sum, 9)

        ans = "9" * nines

        if remainder:
            ans += str(remainder)

        ans += "0" * (num - len(ans))

        return ans

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """[summary]
            Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
            Return the quotient after dividing dividend by divisor.
            The integer division should truncate toward zero, which means losing its fractional part.
            For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

            Note:
            Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
            For this problem, assume that your function returns 231 − 1 when the division result overflows.

        Args:
            dividend (int): -231 <= dividend, divisor <= 231 - 1
            divisor (int): divisor != 0

        Returns:
            int: quotient after dividing dividend by divisor.

        Result:
            Runtime: 24 ms, faster than 97.98% of Python3 online submissions for Divide Two Integers.
            Memory Usage: 14.2 MB, less than 83.72% of Python3 online submissions for Divide Two Integers.
        """

        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1

            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1

            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

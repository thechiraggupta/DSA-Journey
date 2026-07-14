class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        digit_sum = 0

        while n > 0:
            digit = n % 10
            product *= digit
            digit_sum += digit
            n //= 10

        return product - digit_sum
class PrimeFactors:
    def of(self, num):
        factors = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1

        return factors

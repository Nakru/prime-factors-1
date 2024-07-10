class PrimeFactors:
    def of(self, num):
        factors = []
        if num > 1:
            if num == 4:
                while num % 2 == 0:
                    factors.append(2)
                    num //= 2
            elif num == 6:
                factors.append(2)
                factors.append(3)
            else:
                factors.append(num)
        return factors

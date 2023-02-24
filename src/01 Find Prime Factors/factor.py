def get_prime_factors(number):
    factors = []
    product = 1
    for divisor in range(2, number + 1):
        if number % divisor == 0 and product <= number:
            factors.append(divisor)
            product = product * divisor
    return factors


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]

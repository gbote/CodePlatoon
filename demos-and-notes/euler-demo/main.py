# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def largest_prime(n):
    factors = []
    return next((n / i for i in range(1, (int(n / 2) + 1)) if n % i == 0 and is_prime(n / i)), factors)

def list_factors(n):
    return [i for i in range(1, (int(n/2) + 1)) if n % i == 0]

def is_prime(n):
    return len(list_factors(n)) == 1

# def largest_prime_factor(n):
#     factors_of_n = list_factors(n)
#     factors_of_n.reverse()
#     for factor in factors_of_n:
#         if is_prime(factor):
#             return factor


# print(largest_prime_factor(600475143))

print(largest_prime(600851475143))
import math


def sieve_of_eratosthenes(limit):
    output = [True] * (limit + 1)
    output[0] = False
    output[1] = False

    for i in range(2, limit + 1):
        if output[i]:
            j = i * 2
            while j <= limit:
                output[j] = False
                j = j + i
    return find_true_indices(output)


def find_true_indices(inputs):
    true_indices = []
    [true_indices.append(i) for i, v in list(enumerate(inputs)) if v]
    return true_indices


def sieve_of_eratosthenes_optimized(limit):
    if limit <= 1:
        return []

    output = [True] * (limit + 1)
    output[0] = False
    output[1] = False

    for i in range(2, math.floor(math.sqrt(limit))):
        if output[i]:
            j = i ** 2
            while j <= limit:
                output[j] = False
                j += i

    output_with_indices = list(enumerate(output))
    trues = [idx for (idx, value) in output_with_indices if value]
    return trues


print(sieve_of_eratosthenes(13))
print(sieve_of_eratosthenes_optimized(13))

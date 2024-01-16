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
    [true_indices.append(i) for i, v in enumerate(inputs) if v]
    return true_indices


print(sieve_of_eratosthenes(13))

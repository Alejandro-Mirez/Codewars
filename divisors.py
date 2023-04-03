def divisors(integer):
    list_of_divisors = []
    for i in range(2, integer):
        if integer%i == 0:
            list_of_divisors.append(i)
    if len(list_of_divisors) == 0:
        return f'{integer} is a prime number'
    else:
        return list_of_divisors

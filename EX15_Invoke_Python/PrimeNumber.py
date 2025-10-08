def prime_check():
    num = 13   # static input

    if num <= 1:
        return str(num) + " is not a prime number."
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return str(num) + " is not a prime number."
        return str(num) + " is a prime number."

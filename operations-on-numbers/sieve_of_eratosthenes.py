from operations_on_numbers import NumberOperations

if __name__ == '__main__':
    no = NumberOperations()
    num = input("Enter the upper limit for determining prime numbers: ")

    while not (no.is_integer(num) and int(num) > 0):
        num = input("Your value is not correct. Please try again: ")

    print("Prime numbers in range from 1 to {}: {}.".format(num, no.sieve_of_eratosthenes(int(num))))

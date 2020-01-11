from operations_on_numbers import NumberOperations

if __name__ == '__main__':
    no = NumberOperations()
    num = input("How many Fibonnaci numbers do you want to generate? ")

    while not (no.is_integer(num) and int(num) > 0):
        num = input("Your value is not correct. Please try again: ")

    num = int(num)

    print("Fibonnaci sequence: {}.".format(no.fibonnaci(num)))

from operations_on_numbers import NumberOperations

if __name__ == '__main__':
    num_list = input('Enter integer numbers separated by a comma: ')
    num_list = num_list.replace(" ", "").split(",")

    no = NumberOperations()
    if no.are_all_elements_integer(num_list):
        int_list = [int(num) for num in num_list]
        sorted_list = no.bubble_sort(int_list)
        print('The sorted list: {}'.format(sorted_list))
    else:
        print('Sorry, your list is not correct.')

from operations_on_numbers import NumberOperations

if __name__ == '__main__':
    num_list = input('Enter integer numbers separated by a comma: ')
    num_list = num_list.replace(" ", "").split(",")

    no = NumberOperations()
    if no.are_all_elements_integer(num_list):
        int_list = [int(num) for num in num_list]
        sorted_list = no.bubble_sort(int_list)
        num = input('Enter integer number for search: ')
        if no.is_integer(num):
            num = int(num)
            if no.search_number(int_list, num):
                print('The number {} is in list of numbers.'.format(num))
            else:
                print('The number {} is not in list of numbers.'.format(num))
        else:
            print('Sorry, your value is not correct.')
    else:
        print('Sorry, your list is not correct.')

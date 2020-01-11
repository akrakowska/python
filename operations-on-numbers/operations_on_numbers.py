import math
from typing import List, Any


class NumberOperations:
    def is_integer(self, num: Any) -> bool:
        """
        Checks if element is integer
        :param num: element to check
        :return: True if element is integer or False if not
        """
        try:
            int(num)
            return True
        except ValueError:
            return False

    def are_all_elements_integer(self, num_list: list) -> bool:
        """
        Checks if all list elements are integers
        :param num_list: list to check
        :return: True if all list elements are integers or False if not
        """
        try:
            for number in num_list:
                int(number)
            return True
        except ValueError:
            return False

    def bubble_sort(self, num_list: List[int]) -> List[int]:
        """
        Sorts list of integers
        :param num_list: list of integers to sort
        :return: Sorted list of integers
        """
        num_sorted = False
        while not num_sorted:
            num_sorted = True
            for i in range(0, len(num_list) - 1):
                if num_list[i] > num_list[i + 1]:
                    temp = num_list[i]
                    num_list[i] = num_list[i + 1]
                    num_list[i + 1] = temp
                    num_sorted = False
        return num_list

    def max_of_numbers(self, num_list: List[int]) -> int:
        """
        Finds maximum element in list of integers
        :param num_list: list of integers
        :return: Maximum integer in list
        """
        max_num = num_list[0]
        for number in num_list:
            if number > max_num:
                max_num = number
        return max_num

    def moda(self, num_list: List[int]) -> int:
        """
        Finds element with the highest occurence in list of integers, if more elements have the same occurence then
        function finds first element with this occurence
        :param num_list: list of integers
        :return: The highest occurence integer in list
        """
        return max(set(num_list), key=num_list.count)

    def search_number(self, num_list: List[int], search_num: int) -> bool:
        """
        Checks if integer is part of list
        :param num_list: list of integers
        :param search_num: integer to find in list
        :return: True if search_num is in list or False if not
        """
        if len(num_list) == 1:
            return search_num == num_list[0]

        central_element_index = int(len(num_list) / 2)

        if search_num == num_list[central_element_index]:
            return True
        elif search_num > num_list[central_element_index]:
            return self.search_number(num_list[central_element_index + 1:], search_num)
        elif search_num < num_list[central_element_index]:
            return self.search_number(num_list[:central_element_index], search_num)

    def fibonnaci(self, num: int) -> List[int]:
        """
        Create list with Fibonnaci sequence including given number of elements
        :param num: number of elements in Fibonnaci sequence
        :return: list with Fibonnaci sequence
        """
        i = 1
        fib = []
        if num == 1:
            fib = [0]
        elif num == 2:
            fib = [0, 1]
        elif num > 2:
            fib = [0, 1]
            while i < num - 1:
                fib.append(fib[i] + fib[i - 1])
                i += 1
        return fib

    def sieve_of_eratosthenes(self, num: int) -> List[int]:
        """
        Creates list with prime numbers in given range
        :param num: last number in range to check
        :return: list with prime numbers in given range
        """
        sq = int(math.sqrt(num))
        divisor = 2
        num_list = list(range(1, num + 1))
        nonprime_numbers = []

        while divisor <= sq:
            for number in num_list:
                if number % divisor == 0 and number != divisor and number not in nonprime_numbers:
                    nonprime_numbers.append(number)
            divisor += 1
        prime_numbers = [number for number in num_list if number not in nonprime_numbers]
        return prime_numbers

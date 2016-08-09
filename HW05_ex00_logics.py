#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
# def even_odd():
#     """ Print even or odd:
#         Takes one integer from user
#             accepts only non-word numerals
#             must validate
#         Determines if even or odd
#         Prints determination
#         returns None
#     """
    # evenodd_input = int(input("Please enter a number "))
    # if ((evenodd_input) % 2) == 0:
    #     determination = 'Even'
    # else:
    #     determination = 'Odd'
    # print(determination)
    # return None
    # pass


# def ten_by_ten():
#      """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
#     count = 1
#     while count <= 100:
#         if count % 10 == 0:
#             print(count)
#         else:
#             print(count, end = " ")
#         count +=1
# pass


def find_average():
    entering_values = True
    list_user_inputs = []
    count = 0
    while entering_values == True:
        user_input = (input("Please enter a number or type done: "))

        if user_input == 'done':
            entering_values == False
            numerator = (sum(list_user_inputs))
            denominator = count
            print(numerator/denominator)
            return

        float_input = float(user_input)
        list_user_inputs.append(float_input)
        count += 1

#     """ Takes numeric input (non-word numerals) from the user, one number
#     at a time. Once the user types 'done', returns the average.
#     """

#     pass


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    # pass

# even_odd()
# ten_by_ten()
find_average()

if __name__ == '__main__':
    main()

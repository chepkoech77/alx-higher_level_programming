#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                el_1 = my_list_1[i]
                el_2 = my_list_2[i]
                result = el_1 / el_2
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except (TypeError, ValueError):
                result = 0
                print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                result_list.append(result)
    finally:
        return result_list
